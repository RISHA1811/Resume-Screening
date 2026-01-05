from huggingface_hub import login, upload_folder

login()

upload_folder(
    folder_path="model",
    repo_id="Risha1811/Resume-Screener",
    repo_type="model"
)
