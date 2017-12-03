#!/usr/bin/env python3
from flask import Flask, url_for, request
from flask import make_response
app = Flask(__name__)

class Sanitize:
    def __init__(self):
        return
    def xss(self, data):
        return data.replace('<', '&lt;').replace('>', '&gt;')
sanitize = Sanitize()

def setHeaders(resp):
    resp.headers['server'] = 'Flask'
    resp.headers['x-powered-by'] = 'open source'
    return resp


@app.route('/search')

def search():
    resp = make_response('This is the search page: ' + sanitize.xss(request.args.get('index')))
    resp = setHeaders(resp)
    return resp