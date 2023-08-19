from src.components.data_ingestion import DataIngestion, DataIngestionConfig
from src.components.data_validation import DataValidation
# from src.components.data_transformation import DataTransformation
# from src.components.model_training import Modeltrainer
class TrainingPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_validation = DataValidation()
        # self.data_transformation = DataTransformation()
        # self.model_training = Modeltrainer()
    def start_training_pipeline(self):
        self.data_ingestion.initiate_data_ingestion()
        self.data_validation.initiate_data_validation()
        # self.data_transformation.initiate_data_transformation()
        # self.model_training.initiate_model_training()