import pymongo


# A mongoDB collection connection
class MongoCollection:

    def __init__(self, dbstr, colstr):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client[dbstr]
        self.col = self.db[colstr]

    # saves a dictionary to mongoDB
    def save(self, bson):
        result = self.col.insert_one(bson)
        print('One post: {0}'.format(result.inserted_id))



