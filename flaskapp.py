from flask import Flask, render_template, url_for, app, flash, request, session, redirect, send_from_directory, \
    make_response
import pymysql

app = Flask(__name__)
# app.secret_key = '\xdc\x9c\x91\x7fK\x13\xaf\x9c\x05\x86zj\xe0\xa9?\xd8\xf4\xccS\x97\x8cb,\xc5'

host="awsfirstdb.ccglhhwleoca.us-east-2.rds.amazonaws.com"
port=3306
dbname="awsfirstdb"
user="atheer123"
password="Deem12345"
conn = pymysql.connect(host, user=user,port=port,
                           passwd=password, db=dbname)
cur = conn.cursor()

@app.route('/')
def hello_world():
    cur.execute("SELECT * FROM awsfirstdb.classes ")
    x= cur.fetchall()
    print x
    return render_template('index.html')#,x=x)

@app.route('/query1', methods=['POST'])
def query1():
    cur.execute("SELECT * FROM awsfirstdb.classes")
    x = cur.fetchall()
    print x
    return render_template('query1.html')  # ,x=x)
if __name__ == '__main__':
    app.run()
