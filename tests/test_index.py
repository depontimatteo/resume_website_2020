
import flask
import pytest
import time
from selenium import webdriver

def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200

    with app.test_request_context('/?lang_id_p=it'):
        assert flask.request.path == '/'
        assert flask.request.args['lang_id_p'] == 'it'

    with app.test_request_context('/?lang_id_p=en'):
        assert flask.request.path == '/'
        assert flask.request.args['lang_id_p'] == 'en'

