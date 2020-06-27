from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder='static/dist')


@app.route('/')
def index():
    return app.send_static_file("index.html")

@app.route('/dist/<path:path>')
def static_dist(path):
    return send_from_directory("static/dist", path)


@app.route('/api/data')
def languages():
    return jsonify({
        'languages': [
            'assembly',
            'c#',
            'c',
            'c++',
            'go',
            'java',
            'javascript',
            'object c',
            'pascal',
            'perl',
            'php',
            'python',
            'R',
            'ruby',
            'SQL',
            'swift',
            'visual basic',
        ]
    })

if __name__ == '__main__':
    app.run()