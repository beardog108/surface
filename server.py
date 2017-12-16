#!/usr/bin/env python3
from flask import Flask, url_for, request
from flask import make_response
import sqlite3
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
    resp.headers['access-control-allow-origin'] = '*'
    return resp


@app.route('/search')

def search():
    try:
        search = request.args.get('index')
    except:
        search = '0'
    if search == None:
        search = '0'
    resp = make_response('This is the search page: ' + sanitize.xss(search))
    resp = setHeaders(resp)
    return resp

@app.route('/submit', methods=['POST'])

def submit():
    resp = make_response('test')
    resp = setHeaders(resp)
    return resp

@app.route('/getsites', methods=['GET'])

def getsites():
    #t = ('RHAT',)
    conn = sqlite3.connect('sites.db')
    c = conn.cursor()
    retData = ''
    count = 1
    try:
        offset = int(request.args.get('offset'))
    except:
        offset = 0

    for row in c.execute('SELECT * FROM Sites where ID BETWEEN ? and ?', (offset, offset + 10)):
        #retData += '<div class="col c' + str(count) + '">' + sanitize.xss(str(row[1])) + '</div><div class="col c' + str(count) + "'>" + sanitize.xss(row[2]) + "</div></div><div class='site row'>"
        retData += '<div class="site row"><h2>' + row[1] + '</h2><div class="col c' + str(count) + '">Onion: <input type="text" readonly  class="item" value="' + sanitize.xss(row[2]) + '"></div>'
        if row[3] != '':
            count += 1
            retData += '<div class="col c' + str(count) + '">ZeroNet: <input type="text" readonly  class="item" value="' + sanitize.xss(row[3]) + '"></div>'
        if row[4] != '':
            count += 1
            retData += '<div class="col c' + str(count) + '">I2P (base32): <input type="text" readonly  class="item" value="' + sanitize.xss(row[4]) + '"></div>'
        if row[5] != '':
            count += 1
            retData += '<div class="col c' + str(count) + '">I2P (hostname): <input type="text" readonly  class="item" value="' + sanitize.xss(row[5]) + '"></div>'
        if row[6] != '':
            count += 1
            retData += '<div class="col c' + str(count) + '">Freenet: <input type="text" readonly  class="item" value="' + sanitize.xss(row[6]) + '"></div>'
        if row[7] != '':
            count += 1
            retData += '<div class="col c' + str(count) + '">IPFS: <input type="text" readonly  class="item" value="' + sanitize.xss(row[7]) + '"></div>'
        if row[8] != '':
            count += 1
            retData += '<div class="col c' + str(count) + '">Dat: <input type="text" readonly  class="item" value="' + sanitize.xss(row[8]) + '"></div>'
        
        retData += '</div>'
        if count == 12:
            count = 1
        else:
            count += 1
    resp = make_response(retData)
    resp = setHeaders(resp)
    conn.close()
    return resp