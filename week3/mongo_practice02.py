from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

movie = db.movies.find_one({'title': '월-E'})
target_star = movie['star']

target_movies = list(db.movies.find({'star': target_star}))
for target_movie in target_movies:
    print(target_movie['title'])
db.movies.update_many({'star': target_star}, {'$set': {'star': '0'}})

print("hello git")