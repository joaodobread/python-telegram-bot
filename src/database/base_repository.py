from src.database.client import Database


class Repository(Database):
    def __init__(self, database: str, collection: str):
        super().__init__()
        self.__database = database
        self.__collection = collection

    def db_collection(self):
        return self.get_database(self.__database).get_collection(
            self.__collection)

    def find_one(self, filters=None):
        return self.db_collection().find_one(filters)

    def find_all(self, *args, **kwargs):
        return self.db_collection().find(*args, **kwargs)
