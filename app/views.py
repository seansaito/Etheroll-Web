from flask import flash, Flask, render_template, redirect, url_for, jsonify, request
from app import app
import json

app.secret_key = 'some_secret'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/connect", methods=["POST"])
def connect():
	error = None
	if request.method=="POST":
		name = request.form["name"]
		password = request.form["password"]
		path = "app/static/json/users.json"
		with open(path, "r+") as login_data:
			auth = json.load(login_data)
		if name in auth.keys():	
			if auth[name] == password:
				redirect_to_index = redirect('/grabcar')
				response = app.make_response(redirect_to_index)  
				response.set_cookie('username',value=name)
				response.set_cookie('password',value=password)
				return response
			else:
				error ='Invalid credentials!'
		else:
			error = 'Invalid credentials!'

		return render_template("index.html",error=error)

@app.route('/grabcar')
def grabcar():
	user_id = request.cookies.get('username')
	user_pw = request.cookies.get('password')
	print user_id
	print user_pw
	return render_template("grabcar.html")



