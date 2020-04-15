import pymongo

client = pymongo.MongoClient('localhost', 27017)

db = client['DiscordMessageDatabase']

messages = db.messages

message_data = {
    'user': 'Vector_Bubbs',
    'content': 'hello'
}

result = messages.insert_one(message_data)
print('One post: {0}'.format(result.inserted_id))
