import os
import zipfile
from urllib.request import urlretrieve

def download(url, filename):
    print(f"Downloading {filename}...")
    urlretrieve(url, filename)
    print("Download complete.")

def extract_file(zip_path, file_name, output_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file_info in zip_ref.infolist():
            if file_name in file_info.filename:
                extracted_filename = os.path.basename(file_info.filename)
                extracted_path = os.path.join(output_path, extracted_filename)
                with open(extracted_path, 'wb') as extracted_file:
                    extracted_file.write(zip_ref.read(file_info.filename))
                return True
    return False
