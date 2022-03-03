from flask import Flask
from public import public
from admin import admin
from doctor import doctor
from api import api

app=Flask(__name__)
app.secret_key="abc"
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(doctor,url_prefix='/doctor')
app.register_blueprint(api,url_prefix='/api')
app.run(debug=True,port=5083,host="192.168.43.19")
# app.run(debug=True,port=5081)
