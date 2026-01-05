#!/usr/bin/env bash
set -euo pipefail

: "${HF_TOKEN:?Environment variable HF_TOKEN must be set (see README)}"
REPO=${1:-Risha1811/Resume-Screener}

echo "Authenticating to Hugging Face..."
hf auth login --token "$HF_TOKEN"

echo "Uploading files from current directory to $REPO..."
hf upload "$REPO" .

echo "Upload complete."
