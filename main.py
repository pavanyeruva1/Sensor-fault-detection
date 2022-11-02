from sensor.configaration.mongo_db_connection import MangoDBclient
from sensor.constant import training_pipeline
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.pipeline.training_pipeline import Training_Pipeline

if __name__=="__main__":
    training_pipeline_data=Training_Pipeline()
    training_pipeline_data.run_pipeline()