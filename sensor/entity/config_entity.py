import os
from datetime import datetime
from typing_extensions import Self
from sensor.constant.training_pipeline import PIPELINE_NAME,ARTIFACT_DIR, TRAIN_FILE_NAME
from sensor.constant.training_pipeline import DATA_INGESTION_DIR_NAME,DATA_INGESTION_FEATURE_STORE_DIR,FILE_NAME,DATA_INGESTION_INGESTED_DIR
from sensor.constant.training_pipeline import TEST_FILE_NAME,TEST_FILE_NAME,DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO,DATA_INGESTION_COLLECTION_NAME

class TrainingPipelineConfig:

    def __init__(self,timestamp=datetime.now()):
        timestamp=timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipelinename=PIPELINE_NAME
        self.artifact_dir=os.path.join(ARTIFACT_DIR,timestamp)
        self.timestamp=timestamp


class DataIngestionConfig:
    def __init__(self,training_pipeline_config=TrainingPipelineConfig):
        self.training_pipeline_config = training_pipeline_config
        self.data_ingestion_dir=os.path.join(training_pipeline_config.artifact_dir,DATA_INGESTION_DIR_NAME)
        self.feature_store_file_path=os.path.join(self.data_ingestion_dir,DATA_INGESTION_FEATURE_STORE_DIR,FILE_NAME)
        self.training_file_path=os.path.join(self.data_ingestion_dir,DATA_INGESTION_INGESTED_DIR,TRAIN_FILE_NAME)
        self.testing_file_path=os.path.join(self.data_ingestion_dir,DATA_INGESTION_INGESTED_DIR,TEST_FILE_NAME)
        self.train_test_ratio=DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name= DATA_INGESTION_COLLECTION_NAME