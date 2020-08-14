from flask import Flask, jsonify, request, send_from_directory
from flask_expects_json import expects_json
from flask_cors import CORS
from core.git import Git
import os
from collections import Counter

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
        return jsonify({"branches": gt.get_branches()})
    
    @app.route('/api/fetch', methods=['GET'])
    def checkout_branch():
        branch_name = request.args.get('branch_name')
        gt.checkout_branch(branch_name)
        return jsonify({'status': 'ok'})

    @app.route('/api/commits', methods=['GET'])
    def commits():
        branch_name = request.args.get('branch_name')
        commits = gt.get_commits(branch_name)
        authors_total = map(lambda x: str(x.author.name), commits)
        author_stats = Counter(list(authors_total))
        print(author_stats)
        return jsonify({"authors":list(set(authors_total)), "commits": list(map(lambda x: {'id': x.hexsha, 'file_stats':x.stats.files, 'stats': x.stats.total, 'message': x.message, 'committed_datetime': x.committed_datetime, 'author': str(x.committer)}, commits))})
    
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