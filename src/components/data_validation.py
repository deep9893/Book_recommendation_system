import os, sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from src.config.configuration import Configuration


class DataValidation:
    def __init__(self,app_config = Configuration()):
        try:
            self.data_validation_config = app_config.get_data_validation_config()
            
        except Exception as e:
            raise CustomException (e, sys) from e
        
    def prepare_data(self):
        try:
            
            logging.info("data validation started")
            
            ratings = pd.read_csv(self.data_validation_config.rating_csv_files)
            books = pd.read_csv(self.data_validation_config.books_csv_files)
            
            logging.info(f"shape of our ratings data: {ratings.shape}")
            
            logging.info(f"shape of our books data: {books.shape}")

            books = books['ISBN','Book-Title','Book-Author','Publisher','Year-Of-Publication','Publisher','Image-URL-L']


            
        except Exception as e:
            raise CustomException (e, sys) from e