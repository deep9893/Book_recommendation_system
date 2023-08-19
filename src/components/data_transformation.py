import os,sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException
import pickle
from src.config.configuration import *
from src.utils.utils import read_yaml_file


 
class DataTransformation:
    def __init__(self,app_config = Configuration):
        try:
            self.data_transformation_config = app_config.get_data_transformation_config()
            self.data_validation_config = app_config.get_data_validation_config()
            
        except Exception as e:
            raise CustomException(e,sys) from e
        
        
    def get_data_transformer(self):
        try:
            df = pd.read_csv(self.data_transformation_config.clean_data_file_path)
            
        
            # create complete pivot table
            book_pivot = df.pivot_table(index = 'titles',columns = 'user_id',values='rating')
            book_pivot.fillna(0,inplace=True)
            
            # saving pivot table in data transformation
            
            os.makedirs(self.data_transformation_config.transformed_data_dir, exist_ok=True)
            pickle.dump(book_names, open(os.path.join(self.data_transformation_config.transformed_data_dir,'transfomation_data.pickle'),'wb'))
            
            book_names = book_pivot.index
            
            # this is for our book table
            
            os.makedirs(self.data_validation_config.serialized_objects_dir, exist_ok=True)
            pickle.dump(book_names, open(os.path.join(self.data_validation_config.serialized_objects_dir,'book_names.pickle'),'wb'))
            
            logging.info('save our book names under our serialized object directory')
            
            # this is for pivot table
            
            os.makedirs(self.data_validation_config.serialized_objects_dir, exist_ok=True)
            pickle.dump(book_names, open(os.path.join(self.data_validation_config.serialized_objects_dir,'book_pivot.pickle'),'wb'))     
        
            logging.info('save our book_pivot names under our serialized object directory')

        
        
        except Exception as e:
            raise CustomException(e,sys) from e
        
        
    def initiate_data_transformation(self):
        try:
            self.data_transformation()
            logging.info('data transformation completed successfully')

        except Exception as e:
            raise CustomException(e,sys) from e