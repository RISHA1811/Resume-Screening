# Scripts for uploading to Hugging Face

All scripts read `HF_TOKEN` from the environment and upload the current directory to the specified Hugging Face repo.

Usage examples:

Bash (temporary session):
```bash
export HF_TOKEN="YOUR_TOKEN"
./scripts/push_model.sh Risha1811/Resume-Screener
```

PowerShell (session):
```powershell
$env:HF_TOKEN = "YOUR_TOKEN"
./scripts/push_model.ps1 -Repo Risha1811/Resume-Screener
```

Python:
```bash
export HF_TOKEN="YOUR_TOKEN"
python scripts/upload_model.py Risha1811/Resume-Screener
```

Notes:
- Revoke any exposed tokens immediately. Do not commit tokens to the repository or paste them in chat.
- Ensure the `hf` CLI is installed (`pip install --upgrade huggingface_hub` or use the official installer).