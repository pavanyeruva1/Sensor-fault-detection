from genericpath import exists
import sys,os
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity.artifact_entity import Dataingestionartifact
#from sensor.constant.database import DATABASE_NAME,COLLECTION_NAME
from pandas import DataFrame
from sensor.data_access.sensor_data import SensorData




class Dataingestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise SensorException(e,sys)


    def export_data_into_feature_store(self):
        """
        Export Mangodb Data To Dataframe to Future Store

        """
        try:
            logging.info("data export from Mongodb to Feature Store Started")
            sensor_data=SensorData()
            dataframe=sensor_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)
            feature_file_path=self.data_ingestion_config.feature_store_file_path
            #creating Folder
            dir_path=os.path.dirname(feature_file_path)
            os.mkdir(dir_path,exist_ok=True)

            dataframe.to_csv(feature_file_path,index=False,header=True)
            return dataframe



        except Exception as e:
            raise SensorException(e,sys)

    def split_data_as_train_test(self,dataframe=DataFrame):

        """
        Split data from Dataframe into Train Test Files
        """
        pass




    def initiate_data_ingestion(self) ->Dataingestionartifact:
        try:
            dataframe=self.export_data_into_feature_store()
            self.split_data_as_train_test(dataframe=dataframe)
            data_ingestion_artifact=Dataingestionartifact(trained_file_path=self.data_ingestion_config.training_file_path,test_file_path=self.data_ingestion_config.testing_file_path)
            return data_ingestion_artifact
        except Exception as e:
            raise SensorException(e,sys)

    

