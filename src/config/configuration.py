import os, sys
from src.logger import logging
from src.exception import CustomException
from src.entity.config_entity import DataIngestionConfig
from src.constant import *
from src.utils.utils import read_yaml_file

class Configuration:
    def __init__(self,config_file_path: str = CONFIG_FILE_PATH):
        try:
            self.configs_info = read_yaml_file(file_path=config_file_path)
        except Exception as e: 
            raise CustomException(e, sys) from e
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            logging.info(f"{'='*20}create artifact dir.{'='*20} \n\n")

            data_ingestion_config = self.configs_info['data_ingestion_config']
            artifact_dir = self.configs_info['artifacts_config']['artifact_dir']
            dataset_dir = data_ingestion_config['dataset_dir']
            


            ingested_data_dir = os.path.join(artifact_dir,dataset_dir, data_ingestion_config['ingested_dir'])
            raw_data_dir = os.path.join(artifact_dir,dataset_dir,  data_ingestion_config['raw_data_dir'])


            response = DataIngestionConfig(
                dataset_download_url = data_ingestion_config['dataset_download_url'],
                raw_data_dir = raw_data_dir,
                ingested_dir = ingested_data_dir
            )
            
            logging.info(f"Data Ingestion Config: {response}")
            return response

        except Exception as e: 
            raise CustomException(e, sys) from e
            
            
            
            
            
            
            
            
            
            
# # data validation

#     def get_data_validation_config(self) -> DataValidationConfig:
#         try:
#             data_ingestion_config = self.config_info['data_ingestion_config']
#             data_validation_config = self.config_info['data_validation_config']
#             dataset_dir = data_ingestion_config['dataset_dir']
#             artifact_dir = self.config_info['artifact_config']['artifact_dir']
#             books_csv_file = data_validation_config['books_csv_files']  
#             ratings_csv_file = data_validation_config['rating_csv_files']
            
#             books_csv_file_dir = os.path.join(artifact_dir,dataset_dir,data_ingestion_config['ingested_dir'],books_csv_file)
#             ratings_csv_file_dir = os.path.join(artifact_dir,dataset_dir,data_ingestion_config['ingested_dir'],ratings_csv_file)
#             cleand_data_path = os.path.join(artifact_dir,dataset_dir,data_validation_config['clean_data_dir'])
#             objects_dir = os.path.join(artifact_dir,dataset_dir,data_validation_config['objects_dir'])

#             response = DataValidationConfig(
#                 books_csv_files= books_csv_file_dir,
#                 rating_csv_files= ratings_csv_file_dir,
#                 clean_data_dir= cleand_data_path,
#                 objects_dir= objects_dir)
                                            
        
#             return response
    
#         except Exception as e:
#             raise CustomException (e,sys)