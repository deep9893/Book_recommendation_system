
import os, sys
from src.logger import logging
from src.exception import CustomException
from src.entity.config_entity import *
from src.constant import *
from src.utils.utils import *
from src.config.configuration import Configuration
import urllib.request
# import request
import zipfile

class DataIngestion:
    def __init__(self,app_config = Configuration()):
        try:
            self.data_ingestion_config = app_config.get_data_ingestion_config()
            
        except Exception as e:
            raise CustomException (e,sys) from e


    def download_data(self):
        try:
            dataset_url = self.data_ingestion_config.dataset_download_url
            zip_download_dir = self.data_ingestion_config.raw_data_dir
            logging.info(f"Dataset download url: {dataset_url}")
            
            logging.info(f"Zip download url: {zip_download_dir}")
             
            os.makedirs(zip_download_dir, exist_ok=True)
            data_file_name = os.path.basename(dataset_url)
            zip_file_path = os.path.join(zip_download_dir, data_file_name)
            
            logging.info(f"Zip file path: {zip_file_path}")

            urllib.request.urlretrieve(dataset_url, zip_file_path)

            return zip_file_path

        except Exception as e:
            raise CustomException(e, sys) from e
        
    def extract_zip_file(self,zip_file_path: str):
        try:
            ingested_dir = self.data_ingestion_config.ingested_dir
            os.makedirs(ingested_dir, exist_ok=True)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(ingested_dir)
                
            logging.info(f"Extracting zip file: {zip_file_path} into dir: {ingested_dir}")
            
        except Exception as e:
            raise CustomException(e,sys) from e 

    
    def initiate_data_ingestion(self):
        try:
            zip_file_path = self.download_data()
            self.extract_zip_file(zip_file_path=zip_file_path)
            
            logging.info(f"{'='*20}Data Ingestion log completed.{'='*20} \n\n")
            
        except Exception as e:
            raise CustomException(e, sys) from e

# src\components\data_ingestion.py