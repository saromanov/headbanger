from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from core.git import Git

# https://tproger.ru/translations/developing-app-with-flask-and-vue-js/
# https://ru.vuejs.org/v2/guide/index.html

def create_app(congig=None):
    app = Flask(__name__, static_folder='static/dist')
    CORS(app)

def configure_api(app:Flask):

    @app.route('/api/data', methods=['GET'])
    def languages():
        return jsonify({
            'branches': [
                {'name': 'assembly'},
                {'name': 'c#'},
                ]
            })

#'/home/motorcode/headbanger_repo')

if __name__ == '__main__':
    create_app()