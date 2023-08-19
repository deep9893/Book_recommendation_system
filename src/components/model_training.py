import os,sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException
import pickle
from src.config.configuration import *
from src.utils.utils import read_yaml_file
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors


class Modeltrainer:
    def __init__(self, app_config = Configuration()):
        try:
            self.model_training_config = app_config.get_model_trainer_config()
        
        except Exception as e:
            raise CustomException (e,sys)from e
        
        
        
    def train_model(self):
        try:
            book_pivot = pickle.load(self.model_training_config.transformed_data_file_dir,'rb')
            book_sparse = csr_matrix(book_pivot)
            
            model = NearestNeighbors(algorithm='brute')
            model.fit(book_sparse)
            
            os.makedirs(self.model_training_config.trained_model_dir, exist_ok=True)
            file_name = os.path.join(self.model_training_config.trained_model_dir,self.model_training_config.trained_model_name)
            pickle.dump(model,open(file_name),'wb')
            
            
            logging.info('saving model trained')
        
        
        except Exception as e:
            raise CustomException (e,sys)from e
        
    def initiate_model_training(self):
        try:
            self.train_model()
        except Exception as e:
            raise CustomException (e,sys)from e