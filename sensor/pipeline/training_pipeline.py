from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.exception import SensorException
import sys,os
from sensor.logger import logging
from sensor.entity.artifact_entity import Dataingestionartifact
from sensor.components.data_ingestion import Dataingestion


class Training_Pipeline:

    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()
        
        #self.training_pipeline_config = TrainingPipelineConfig()



    def start_data_ingestion(self)->Dataingestionartifact:
        try:
            self.data_ingested_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting Data Ingestion")
            data_ingestion=Dataingestion(data_ingestion_config=self.data_ingested_config)
            file_store=data_ingestion.export_data_into_feature_store()
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info("Data Ingestion Completed")
            return data_ingestion_artifact
        except Exception as e:
            raise SensorException(e,sys)



    def start_data_validation(self):
        try:

            pass
        except Exception as e:
            raise SensorException(e,sys)



    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)                


    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)


    def start_model_evaluation(self):
        try:

            pass
        except Exception as e:
            raise SensorException(e,sys)

    def start_model_pusher(self):
        try:

            pass
        except Exception as e:
            raise SensorException(e,sys)



    def run_pipeline(self):
        try:

            data_ingestion_artifact:Dataingestionartifact=self.start_data_ingestion()
        except Exception as e:
            raise SensorException(e,sys)



