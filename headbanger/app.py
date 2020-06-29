from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from core.git import Git
import os

# https://tproger.ru/translations/developing-app-with-flask-and-vue-js/
# https://ru.vuejs.org/v2/guide/index.html

def create_app(congig=None):
    gt = Git(os.environ['HEADBANGER_REPO'])
    app = Flask(__name__, static_folder='static/dist')
    configure_api(app, gt)
    CORS(app)
    app.run()

def configure_api(app:Flask, gt:Git):

    @app.route('/api/branch_names', methods=['GET'])
    def branch_names():
        return jsonify({"branches": list(map(lambda x: {'name': x.name}, gt.get_branches()))})
    
    @app.route('/api/branches', methods=['POST'])
    def create_branch():
        data = request.json
        print(data)
        return jsonify({"status": "ok"})

if __name__ == '__main__':
    create_app()