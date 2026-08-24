#!/usr/bin/env python3
"""
Telemetry Ingestion Engine for fi-imbalance-s1 with Rate-Limit Backoff.
Fetches canonical time-series from Fingrid Open Data API.
"""

import os
import sys
import json
import time
import hashlib
import datetime
import urllib.request
import urllib.error

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(REPO_DIR, 'data')
os.makedirs(DATA_DIR, exist_ok=True)

api_key = ''
env_path = os.path.join(REPO_DIR, '.env')
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            if line.strip().startswith('FINGRID_API_KEY'):
                api_key = line.split('=', 1)[1].strip().strip('\"\'')
            elif '=' not in line and len(line.strip()) > 10:
                api_key = line.strip().strip('\"\'')

if not api_key:
    print("FATAL: Fingrid API key could not be resolved from .env")
    sys.exit(1)

TARGET_DATASETS = [
    319, 75, 245, 246, 369, 375, 376, 377, 378, 379, 381, 385, 390,
    347, 348, 349, 350, 353, 354, 398, 399, 400, 401, 402, 403, 404
]

START_TIME = "2026-08-02T00:00:00.000Z"
END_TIME = "2026-08-06T00:00:00.000Z"

def compute_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

manifest = {
    "manifest_version": "1.0.0",
    "instance": "fi-imbalance-s1",
    "target_start_utc": START_TIME,
    "target_end_utc": END_TIME,
    "portal": "https://data.fingrid.fi",
    "datasets": []
}

print("================================================================================")
print("FETCHING FINGRID OPEN DATA TELEMETRY WITH RATE-LIMIT CONTROL")
print("================================================================================")

for ds_id in TARGET_DATASETS:
    url = f"https://data.fingrid.fi/api/datasets/{ds_id}/data?startTime={START_TIME}&endTime={END_TIME}&pageSize=20000"
    raw_path = os.path.join(DATA_DIR, f"raw_ds_{ds_id}.json")
    retrieved_at = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    success = False
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={'x-api-key': api_key, 'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=20) as resp:
                content_bytes = resp.read()
                with open(raw_path, 'wb') as f:
                    f.write(content_bytes)

                data_json = json.loads(content_bytes.decode('utf-8'))
                records = data_json.get('data', [])
                sha256_hash = compute_sha256(raw_path)

                min_ts = min([r['startTime'] for r in records]) if records else None
                max_ts = max([r['endTime'] for r in records]) if records else None

                print(f"Dataset {ds_id:3d}: Status 200 | Records: {len(records):5d} | SHA256: {sha256_hash[:16]}... | Min: {min_ts} | Max: {max_ts}")

                manifest["datasets"].append({
                    "dataset_id": ds_id,
                    "status_code": 200,
                    "record_count": len(records),
                    "sha256": sha256_hash,
                    "raw_file": f"data/raw_ds_{ds_id}.json",
                    "retrieved_at_utc": retrieved_at,
                    "min_start_time_utc": min_ts,
                    "max_end_time_utc": max_ts
                })
                success = True
                break
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait_time = 4.0 * (attempt + 1)
                print(f"Dataset {ds_id:3d}: Rate limited (HTTP 429). Retrying in {wait_time:.1f}s...")
                time.sleep(wait_time)
            else:
                print(f"Dataset {ds_id:3d}: HTTP Error {e.code} -> {e}")
                manifest["datasets"].append({
                    "dataset_id": ds_id,
                    "status": "ERROR",
                    "error": str(e),
                    "retrieved_at_utc": retrieved_at
                })
                success = True
                break
        except Exception as e:
            print(f"Dataset {ds_id:3d}: Error -> {e}")
            time.sleep(2.0)

    if not success:
        print(f"Dataset {ds_id:3d}: FAILED after retries.")
    
    # Pace requests to stay within rate limit (approx 3 sec delay)
    time.sleep(2.5)

manifest_path = os.path.join(REPO_DIR, 'data_manifest.json')
with open(manifest_path, 'w') as f:
    json.dump(manifest, f, indent=2)

print("\n================================================================================")
print(f"DATA ACQUISITION COMPLETE. Manifest written to: {manifest_path}")
print("================================================================================")
