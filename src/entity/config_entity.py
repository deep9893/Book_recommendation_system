from collections import namedtuple

DataIngestionConfig = namedtuple("DatasetConfig",["dataset_download_url",
                                                  "raw_data_dir",
                                                  "ingested_dir"])


DataValidationConfig = namedtuple("DataValidationConfig", ["clean_data_dir",
                                                         "books_csv_file",
                                                         "ratings_csv_file",
                                                         "serialized_objects_dir"])     

DataTransformerConfig = namedtuple("DataTransformerConfig",['transformed_data_dir',
                                                            'clean_data_file_path'])

Model_TrainerConfig = namedtuple("Model_TrainerConfig",['transformed_data_file_dir',
                                                        'trained_model_dir',
                                                        'trained_model_name'])