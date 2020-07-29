from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

db.users.update_one({'name': '덤블도어'}, {'$set': {'age': 19}})

db.users.delete_one({'name': '론'})

user = db.users.find_one({'name': '론'})
print(user)

