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
	markers = {}
	path = "app/static/json/driver_details.json"
	with open(path, "r+") as driver_data:
		drivers = json.load(driver_data)
	for values in drivers.values():
		print values
		if "available" in values:
			markers[values["call_number"]] = [values["drp"],values["rate"], values["location"]]
	print markers
	return render_template("grabcar.html",markers=markers)


@app.route("/sobrietytest")
def sobrietytest():
    return render_template("sobrietytest.html")

@app.route("/current_drivers")
def current_drivers():
    drivers = get_drivers()
    return render_template("current_drivers.html", drivers=drivers)

@app.route("/test")
def test():
    drivers = get_drivers()
    return render_template("test.html", drivers=drivers)

def get_drivers():
    fp = open("app/static/json/driver_details.json", "r")
    store = json.load(fp)
    fp.close()
    return store
