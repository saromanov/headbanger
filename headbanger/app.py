from flask import Flask, jsonify, request, send_from_directory
from flask_expects_json import expects_json
from flask_cors import CORS
from core.git import Git
import os

# https://tproger.ru/translations/developing-app-with-flask-and-vue-js/
# https://ru.vuejs.org/v2/guide/index.html

schema_create_branch = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'}
    }
}
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
    
    @app.route('/api/commits', methods=['GET'])
    def commits():
        branch_name = request.args.get('branch_name')
        return jsonify({"commits": list(map(lambda x: {'message': x.message}, gt.get_commits(branch_name)))})
    
    @app.route('/api/branches', methods=['POST', 'DELETE'])
    @expects_json(schema_create_branch)
    def handle_branches():
        if request.method == 'POST':
            return create_branch(gt, request)
        if request.method == 'DELETE':
            return delete_branches(gt, request)

def create_branch(gt:Git, req:request):
    gt.create_branch(request.json['name'])
    return jsonify({"status": "ok"})

def delete_branches(gt:Git, req:request):
    gt.delete_branches(request.json['branches'])
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    create_app()