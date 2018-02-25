
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
import sqlite3
import json

app = Flask(__name__)

@app.route('/empresa/api/v1.0/clientes', methods=['GET'])
def get_tasks():
    con = sqlite3.connect("empresa.db")
    con.row_factory = sqlite3.Row # This enables column access by name: row['column_name']
    cur = con.cursor()
    cur.execute("select * from cliente")
    rows = cur.fetchall()
    resp = json.dumps([dict(ix) for ix in rows])
    con.close()
    return resp

if __name__ == '__main__':
    app.run(debug=True)