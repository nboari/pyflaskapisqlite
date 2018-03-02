
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
import sqlite3
import json

app = Flask(__name__)

@app.route('/')
def index():
    get = request.url_root + "gimnasio/api/v1.0/clientes"
    get1 = get + "/1"
    return "GET ALL: <a href='" + get + "'>"+ get + "</a><BR>GET 1: <a href='" + get1 + "'>" + get1 + "</a>"

@app.route('/gimnasio/api/v1.0/clientes', methods=['GET'])
def get_all():
    con = sqlite3.connect("gimnasio.db")
    con.row_factory = sqlite3.Row # This enables column access by name: row['column_name']
    cur = con.cursor()
    cur.execute("select * from cliente")
    rows = cur.fetchall()
    dic = [dict(ix) for ix in rows]
    resp = json.dumps(dic)
    con.close()
    return '{ "clientes": ' + resp + '}'

@app.route('/gimnasio/api/v1.0/clientes/<id>', methods=['GET'])
def get_one(id):
    con = sqlite3.connect("gimnasio.db")
    con.row_factory = sqlite3.Row # This enables column access by name: row['column_name']
    cur = con.cursor()
    cur.execute("select * from cliente where id="+id)
    rows = cur.fetchall()
    resp = json.dumps([dict(ix) for ix in rows])
    con.close()
    return '{ "clientes": ' + resp + '}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)