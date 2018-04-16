import sqlite3
from flask import Flask, jsonify
import hashlib
import time

app = Flask(__name__)
connection= sqlite3.connect('data.db')



def shorten(link):

    h = hashlib.new('sha1')
    h.update(str.encode(link+str(time.time())))
    shorted=h.hexdigest()[4:10]
    print(shorted)
    return shorted




cursor=connection.cursor()
create_table="CREATE TABLE IF NOT EXISTS URLS (id CHARACTER(6) PRIMARY KEY, url TEXT )"
cursor.execute(create_table)
# url=('check','www.google.com')
# insert_query="INSERT into urls VALUES(?,?)"
# cursor.execute(insert_query,url)

def insertIntoDB(short, link):
    url = (short, link)
    insert_query = "INSERT into urls VALUES(?,?)"
    cursor.execute(insert_query, url)
    print("entered into DB")

def findLink(short):
    query="SELECT * FROM urls WHERE id=?"
    result=cursor.execute(query,(short,))
    row=result.fetchone()
    if row:
        return row[1]
    return "Not Found"


# api=Api(app)
#
#
# class Url(Resource):
#     def get(self):
#         return "Cannot Get"
#

@app.route('/<string:lols>')
def hello_world(lols):

    return "<h1>"+findLink(lols)+"</h1>"

@app.route('/create/<string:link>')
def insertDB(link):
    short=shorten(link)
    insertIntoDB(shorten(link), link)
    return jsonify({'short':short})


if __name__ == '__main__':
    app.run()
