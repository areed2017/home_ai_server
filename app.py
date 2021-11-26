import os.path

from flask import Flask, send_file, abort

app = Flask(__name__)


@app.route('/install/<project>', methods=['GET'])
def hello_world(project):
    path = os.getcwd() + f'\\static\\{project}.zip'
    print(path)
    if os.path.exists(path):
        return send_file(path)
    abort(404)


if __name__ == '__main__':
    app.run()
