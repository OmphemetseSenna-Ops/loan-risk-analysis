import os
import shutil
import kagglehub

def download_and_copy(dataset: str, dest_folder: str = "."):
    #Download dataset
    path = kagglehub.dataset_download(dataset)
    print(f"Downloaded to: {path}")

    # Copy files into destination folder
    for item in os.listdir(path):
        src = os.path.join(path, item)
        dst = os.path.join(dest_folder, item)

        if os.path.isdir(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dst)

    print(f"Dataset copied to: {os.path.abspath(dest_folder)}")

if __name__ == "__main__":
    download_and_copy("datawitharyan/financial-loan-dataset")
