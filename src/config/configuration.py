import os, sys
from src.logger import logging
from src.exception import CustomException
from src.entity.config_entity import DataTransformerConfig,DataIngestionConfig 
from src.entity.config_entity import  DataValidationConfig,Model_TrainerConfig
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
             
            
            
# data validation

    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            data_validation_config = self.configs_info['data_validation_config']
            data_ingestion_config = self.configs_info['data_ingestion_config']
            dataset_dir = data_ingestion_config['dataset_dir']
            artifacts_dir = self.configs_info['artifacts_config']['artifact_dir']
            books_csv_file = data_validation_config['books_csv_file']
            ratings_csv_file = data_validation_config['ratings_csv_file']

            books_csv_file_dir = os.path.join(artifacts_dir, dataset_dir, data_ingestion_config['ingested_dir'], books_csv_file)
            ratings_csv_file_dir = os.path.join(artifacts_dir, dataset_dir, data_ingestion_config['ingested_dir'], ratings_csv_file)
            clean_data_path = os.path.join(artifacts_dir, dataset_dir, data_validation_config['clean_data_dir'])
            serialized_objects_dir = os.path.join(artifacts_dir, data_validation_config['serialized_objects_dir'])

            response = DataValidationConfig(
                clean_data_dir = clean_data_path,
                books_csv_file = books_csv_file_dir,
                ratings_csv_file = ratings_csv_file_dir,
                serialized_objects_dir = serialized_objects_dir
            )

            logging.info(f"Data Validation Config: {response}")
            return response

        except Exception as e:
            raise CustomException(e, sys) from e
        
    # data transformation
    
    def get_data_transformation_config(self)->DataTransformerConfig:  
        try:
            data_transformation_config = self.configs_info['data_transformation_config']
            data_validation_config = self.configs_info['data_validation_config'] 
            data_ingestion_config = self.configs_info['data_ingestion_config'] 
            dataset_dir = data_ingestion_config['dataset_dir']
            artifact_dir = self.configs_info['artifacts_config','artifact_dir']

            cleaned_data_file_path = os.path.join(artifact_dir,dataset_dir,data_validation_config['clean_data_dir'],['clean_data.csv'])
            transformed_data_dir = os.path.join(artifact_dir,dataset_dir,data_transformation_config['transformed_data_dir'])

            response = DataTransformerConfig(
                clean_data_file_path = cleaned_data_file_path,
                transformed_data_dir= transformed_data_dir
            )
            
            logging.info(f'Data Transformer Config:{response}')
            return response

        except Exception as e:
            raise CustomException (e,sys) from e         
      
      
        
    # model training 
    
    def get_model_trainer_config(self)-> Model_TrainerConfig:
        try:
            model_trainer_config = self.configs_info['model_trainer_config']
            data_transformation_config = self.configs_info['data_transformation_config'] 
            data_ingestion_config = self.configs_info['data_ingestion_config'] 
            dataset_dir = data_ingestion_config['dataset_dir']
            artifact_dir = self.configs_info['artifacts_config']['artifact_dir']
        
        
            transformed_data_file_path = os.path.join(artifact_dir,dataset_dir,data_transformation_config['transformed_data_dir'],['transformed_data.pkl'])
            trained_model_dir = os.path.join(artifact_dir,model_trainer_config['trained_model_dir'])
            trained_model_name=model_trainer_config['trained_model_name']
            
            response = Model_TrainerConfig(
                transformed_data_file_path = transformed_data_file_path,
                trained_model_dir= trained_model_dir,
                trained_model_name= trained_model_name
                
            )
            logging.info(f'model trainer Config:{response}')

            return response
            
        
        except Exception as e:
            raise CustomException (e,sys) from e    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
   
            
            
