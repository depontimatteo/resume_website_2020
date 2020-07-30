from flask import Flask, Response, render_template, Blueprint, request
from flask_cors import CORS
from api_v1 import parse_json_data


html_v1 = Blueprint('html_v1', __name__, template_folder='templates/resume')

@html_v1.route('/', methods = ['GET'])
@html_v1.route('/index.html', methods = ['GET'])
def index():

    lang_id_p = request.args.get('lang_id_p')

    if not lang_id_p:
        lang_id_p = 'it'

    bio = parse_json_data(lang_id_p)

    return render_template("index.html",
                            lang=lang_id_p,
                            bio=bio)