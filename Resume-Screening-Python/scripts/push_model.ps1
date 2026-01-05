param(
  [string]$Repo = "Risha1811/Resume-Screener"
)

if (-not $env:HF_TOKEN) {
  Write-Error "Environment variable HF_TOKEN is not set. See README."
  exit 1
}

Write-Host "Authenticating..."
hf auth login --token $env:HF_TOKEN

Write-Host "Uploading files..."
hf upload $Repo .

Write-Host "Upload complete."
