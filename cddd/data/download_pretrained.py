import os
import requests
import zipfile
from appdirs import user_data_dir

FILE_ID = "1oyknOulq_j0w9kzOKKIHdTLo5HphT99h"
PRETRAINED_MODEL_DIR = user_data_dir("cddd")

def download_file_from_google_drive(id, destination):
    URL = f"https://drive.google.com/uc?id={id}&confirm=t"

    session = requests.Session()

    response = session.get(URL, stream=True)

    save_response_content(response, destination)

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def download_pretrained_model():
    destination = os.path.join(PRETRAINED_MODEL_DIR, "default_model.zip")
    if not os.path.isdir(PRETRAINED_MODEL_DIR):
        os.mkdir(PRETRAINED_MODEL_DIR)
    download_file_from_google_drive(FILE_ID, destination)
    with zipfile.ZipFile(destination, 'r') as zip_ref:
        zip_ref.extractall(PRETRAINED_MODEL_DIR)