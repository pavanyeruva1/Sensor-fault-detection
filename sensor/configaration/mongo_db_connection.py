from http import client
import pymongo
from sensor.constant.database import DATABASE_NAME
from sensor.constant.env_variable import MANGODB_URL_KEY
import certifi
import os

ca=certifi.where()

class MangoDBclient:
    client=None
    def __init__(self,database_name=DATABASE_NAME):
        try:
            if MangoDBclient.client is None:
                mango_db_url=os.getenv(MANGODB_URL_KEY)
                MangoDBclient.client=pymongo.MongoClient(mango_db_url,tlsCAFile=ca)
            self.client=MangoDBclient.client
            self.database=self.client[database_name]
            self.database_name=database_name
        except Exception as e:
            raise e