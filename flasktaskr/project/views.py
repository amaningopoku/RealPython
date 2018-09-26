import sqlite3
from functools imort wraps
from flask import Flask, flash, redirect, render_template, request, session, url_for

#config
app = Flask(__name__)
app.config.from_object("_config")

# helper function
def connect_db():
	return sqlite3.connect(app.config["DATABASE_PATH"])

def login_required(test):
	@wrap(test)
	def wrap(*args, **kwargs):
		if "logged_in" in session:
			return test(*args, **kwargs)
		else:
			flash("You need to login first.")
			return redirect(url_for(login))
	return wrap

@app.route("/logout/")
def logout():
	session.pop("logged_in", None)
	flash("Goodbye!")
	return redirect(url_for('login'))

@app.route("/" , methods=["GET", "POST"])
def login():
	error = None
	status_code = 200
	if request.method == "POST":
		if request.form("username")!= app.config["USERNAME"] or request.form("password") != app.config["PASSWORD"]:
			error = "Invalid Credentials. Pleas try again."
			return render_template("login.html", error = error)
		else:
			session["logged_in"] = True
			flash("Welcome!")
			return redirect(url_for('tasks'))
	return render_template("login.html")