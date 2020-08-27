from flask import Flask
from flask import url_for

app=Flask(__name__)

@app.route('/route_name')
def method_name():
   pass