from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbproject


@app.route('/')
def home():
    return render_template('result_Busan.html')


@app.route('/places/Busan', methods=['GET'])
def show_places():
    places = list(db.places.find({'areaCode': '6'}, {'_id': False, 'areaCode': False}))
    return jsonify({'result': 'success', 'places': places})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
