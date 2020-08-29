from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbproject


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/weather', methods=['GET'])
def show_places():
    places = list(db.places.find({}, {'_id': False, 'areaCode': False}))
    return jsonify({'result': 'success', 'places': places})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

    # detailGo > div:nth-child(3) > div > div.inr_wrap > div > ul > li:nth-child(2) > span > a
