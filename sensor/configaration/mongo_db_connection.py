from http import client
import pymongo
from sensor.constant.database import DATABASE_NAME
import certifi

ca=certifi.where()

class MangoDBclient:
    client=None
    def __init__(self,database_name=DATABASE_NAME):
        try:
            if MangoDBclient.client is None:
                mango_db_url="mongodb+srv://pavanyeruva:pavan123@cluster0.sl6blsw.mongodb.net/?retryWrites=true&w=majority"
                MangoDBclient.client=pymongo.MongoClient(mango_db_url,tlsCAFile=ca)
            self.client=MangoDBclient.client
            self.database=self.client[database_name]
            self.database_name=database_name
        except Exception as e:
            raise e