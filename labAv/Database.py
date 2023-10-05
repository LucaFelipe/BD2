import pymongo

class Database:
    def __init__(self, db_url, db_name):
        self.client = pymongo.MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection_name = 'Motoristas'  

    def get_motoristas_collection(self):
        return self.db[self.collection_name]

    def close_connection(self):
        self.client.close()
