from flask import Flask, render_template, url_for, app, flash, request, session, redirect, send_from_directory, \
    make_response
import pymysql

app = Flask(__name__)
app.secret_key = '\xdc\x9c\x91\x7fK\x13\xaf\x9c\x05\x86zj\xe0\xa9?\xd8\xf4\xccS\x97\x8cb,\xc5'

# host="awsdbtest.csndrp6z6xh7.us-east-2.rds.amazonaws.com"
# port=3306
# dbname="awsfirstdb"
# user="atheer123"
# password="Deem12345"
# 
# conn = pymysql.connect(host, user=user,port=port,
#                            passwd=password, db=dbname)
# cur = conn.cursor()

# cur.execute("CREATE TABLE all_local_road (rdna VARCHAR(200)) ")
# print ('done create tale')
# cur.execute("insert into all_local_road values ('test5') ")
# conn.commit()
# print ('done insert')
# cur.execute("select * from  all_local_road ")
# print(cur.fetchall())

app = Flask(__name__)
@app.route('/')
def hello_world():
#     cur.execute("select * from   all_local_road ")
# 
#     x= cur.fetchall()
    x= 'hello world'
    return render_template('index.html',x=x)
# print a nice greeting.
# def say_hello(username = "World"):
#     return '<p>Hello %s!</p>\n' % username
# 
# some bits of text for the page.
# header_text = '''
#     <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
# instructions = '''
#     <p><em>Hint</em>: This is a RESTful web service! Append a username
#     to the URL (for example: <code>/Thelonious</code>) to say hello to
#     someone specific.</p>\n'''
# home_link = '<p><a href="/">Back</a></p>\n'
# footer_text = '</body>\n</html>'
# 
# EB looks for an 'application' callable by default.
# application = Flask(__name__)
# 
# add a rule for the index page.
# application.add_url_rule('/', 'index', (lambda: header_text +
#     say_hello() + instructions + footer_text))
# 
# add a rule when the page is accessed with a name appended to the site
# URL.
# application.add_url_rule('/<username>', 'hello', (lambda username:
#     header_text + say_hello(username) + home_link + footer_text))
# 
# run the app.
if __name__ == '__main__':
    # app.run()
#     
# if __name__ == "__main__":
#     # Setting debug to True enables debug output. This line should be
#     # removed before deploying a production app.
    app.debug = True
    app.run(host='0.0.0.0',port=80)