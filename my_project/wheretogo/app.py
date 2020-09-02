from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbproject


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    selected_date = request.form['selected_date']
    selected_place = request.form['selected_place']
    print(selected_place, selected_date)
    return render_template('result.html', selected_date=selected_date, selected_place=selected_place)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

# @app.route('/result', methods=['POST', 'GET'])
# def result():
#     if request.method == 'POST':
#         # selected_place = request.form['selected_place']
#         selected_date = request.form['selected_date']
#         print(selected_date)
#         return render_template('result.html', selected_date=selected_date)


# @app.route('/', methods=['POST'])
# def home() -> 'index.html':
#     selected = request.form['selected']
#     print(selected)
#     return render_template('result.html', selected_place=selected)


# if selected_place == '1':
#     @app.route('/places/Seoul', methods=['GET'])
#     def show_places():
#         places = list(db.places.find({'areaCode': '1'}, {'_id': False, 'areaCode': False}))
#         return jsonify({'result': 'success', 'places': places})
#
# if selected == '2':
#     @app.route('/places/Busan', methods=['GET'])
#     def show_places():
#         places = list(db.places.find({'areaCode': '6'}, {'_id': False, 'areaCode': False}))
#         return jsonify({'result': 'success', 'places': places})

# @app.route('/Seoul')
# def home():
#     return render_template('result_Seoul.html')
#
#
# @app.route('/places/Seoul', methods=['GET'])
# def show_places():
#     places = list(db.places.find({'areaCode': '1'}, {'_id': False, 'areaCode': False}))
#     return jsonify({'result': 'success', 'places': places})
#
#
# @app.route('/Busan')
# def home():
#     return render_template('result_Busan.html')
#
#
# @app.route('/places/Busan', methods=['GET'])
# def show_places():
#     places = list(db.places.find({'areaCode': '6'}, {'_id': False, 'areaCode': False}))
#     return jsonify({'result': 'success', 'places': places})
