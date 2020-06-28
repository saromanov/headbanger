from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

# https://tproger.ru/translations/developing-app-with-flask-and-vue-js/
# https://ru.vuejs.org/v2/guide/index.html
app = Flask(__name__, static_folder='static/dist')
CORS(app)

@app.route('/')
def index():
    return app.send_static_file("index.html")

@app.route('/dist/<path:path>')
def static_dist(path):
    return send_from_directory("static/dist", path)


@app.route('/api/data', methods=['GET'])
def languages():
    return jsonify({
        'branches': [
            {'name': 'assembly'},
            {'name': 'c#'},
        ]
    })

if __name__ == '__main__':
    app.run()