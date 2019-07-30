from flask import Flask, abort
from flask import Response
import json
app = Flask(__name__)

@app.route('/')
def unauthorized():
    return abort(401)


@app.route('/get_bio/<string:language_id>', methods = ['GET'])
def get_bio(language_id):

    with open('json/bio_' + language_id + '.json') as json_file:
        data = json.load(json_file)
        resp = Response(json.dumps(data), status=200, mimetype='application/json')
        return resp

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')