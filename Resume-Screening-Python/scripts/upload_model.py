#!/usr/bin/env python3
import os
import sys
from huggingface_hub import HfApi, upload_folder

HF_TOKEN = os.environ.get("HF_TOKEN")
if not HF_TOKEN:
    print("Error: HF_TOKEN environment variable is not set. See README.", file=sys.stderr)
    sys.exit(1)

REPO = sys.argv[1] if len(sys.argv) > 1 else "Risha1811/Resume-Screener"
api = HfApi(token=HF_TOKEN)
print(f"Uploading current folder to {REPO} ...")
upload_folder(folder_path=".", repo_id=REPO)
print("Upload complete.")
