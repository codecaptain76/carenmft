from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session as browser_session

app = Flask(__name__)
app.secret_key = "abc123"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
	"""render homepage """
	return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/fees')
def fees():
	return render_template("fees.html")

@app.route('/contact')
def contact():
	return  render_template("contact.html")






























if __name__ == '__main__':


	app.debug = False



	app.run()