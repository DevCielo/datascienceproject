import os
import urllib.request as request # Handles file downloads
from src.datascience import logger 
import zipfile # Extracts ZIP Files
from src.datascience.entity.config_entity import (DataIngestionConfig)

## Data Ingestion Component
class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config=config

    # Downloading the zip file
    def download_files(self):
        if not os.path.exists(self.config.local_data_file):
            # Downloads the file and log its metadata
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists")

    # Extracting the zip file into a given directory
    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)