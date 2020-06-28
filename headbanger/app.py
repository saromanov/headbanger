from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from core.git import Git
import os

# https://tproger.ru/translations/developing-app-with-flask-and-vue-js/
# https://ru.vuejs.org/v2/guide/index.html

def create_app(congig=None):
    gt = Git(os.environ['HEADBANGER_REPO'])
    app = Flask(__name__, static_folder='static/dist')
    CORS(app)
    app.run()

def configure_api(app:Flask, gt:Git):

    @app.route('/api/branch_names', methods=['GET'])
    def branch_names():
        return jsonify(map(lambda x: {'name': x.name}, git.get_branches()))

if __name__ == '__main__':
    create_app()