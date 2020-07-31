from flask import Flask, render_template
from flask_cors import CORS
from flask_babel import *
from api_v1 import api_v1 as api_v1_blueprint
from html_v1 import html_v1 as html_v1_blueprint

app = Flask(__name__)
app.config.from_pyfile('../conf/i18n/flask_babel.conf')

CORS(app)
babel = Babel(app)

# blueprint for auth parts of app
app.register_blueprint(api_v1_blueprint)

# blueprint for admin parts of app
app.register_blueprint(html_v1_blueprint)

# Managing i18n
@babel.localeselector
def get_locale():
    # if a user is logged in, use the locale from the user settings
    #user = getattr(g, 'user', None)
    #if user is not None:
    #    return user.locale
    # otherwise try to guess the language from the user accept
    # header the browser transmits.  We support de/fr/en in this
    # example.  The best match wins.
    #return request.accept_languages.best_match(['it', 'en', 'de', 'fr'])
    return 'it'

@babel.timezoneselector
def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone

@app.errorhandler(400)
def error_handler(error):
    return render_template("error_handler.html",
                            code=400), 400

@app.errorhandler(403)
def error_handler(error):
    return render_template("error_handler.html",
                            code=403), 403

@app.errorhandler(404)
def error_handler(error):
    return render_template("error_handler.html",
                            code=404), 404

@app.errorhandler(500)
def error_handler(error):
    return render_template("error_handler.html",
                            code=500), 500

@app.errorhandler(503)
def error_handler(error):
    return render_template("error_handler.html",
                            code=503), 503


