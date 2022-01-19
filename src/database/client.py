import pymongo
from src.config.environment import env


class Database(pymongo.MongoClient):
    def __init__(self):
        super().__init__(env("MONGO_URI"))
