import zipfile
import os

raw_path = "data/raw"
extract_path = "data/raw/extracted"

os.makedirs(extract_path, exist_ok=True)

for file in os.listdir(raw_path):
    if file.endswith(".zip"):
        zip_path = os.path.join(raw_path, file)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

        print(f"Extraído: {file}")
