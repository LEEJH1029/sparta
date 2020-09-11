from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbproject


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['get'])
def result():
    selected_date = request.args.get('selected_date')
    selected_place = request.args.get('selected_place')
    return render_template('result.html', selected_date=selected_date, selected_place=selected_place)


@app.route('/places', methods=['get'])
def places():
    selected_place = request.args.get('selected_place')
    inside = request.args.get('inside')
    if inside == '0':
        inside = None
    else:
        inside = int(inside)
    places = list(db.places.find({'areaCode': selected_place, 'inside': inside}, {'_id': False, 'areaCode': False}))
    return jsonify({'result': 'success', 'places': places})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)