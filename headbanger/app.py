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
    
    @app.route('/api/branches', methods=['POST', 'DELETE'])
    def create_branch():
        if request.method == 'POST':
            return create_branch_post(gt, request)
    

def create_branch_post(gt, req):
      data = request.json
      if 'name' not in data:
          return jsonify({"status": "fail", "error": "branch name is not defined"})
      gt.create_branch(data['name'])
      return jsonify({"status": "ok"})

if __name__ == '__main__':
    create_app()