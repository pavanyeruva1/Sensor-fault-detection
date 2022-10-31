from sensor.configaration.mongo_db_connection import MangoDBclient


if __name__=="__main__":
    mangodb_client=MangoDBclient()
    print(mangodb_client.database.list_collection_names())