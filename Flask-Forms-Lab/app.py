from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "lynne"
password = "136"
facebook_friends=["Ahmad","Zain","Adan", "Fouad", "Lourd", "Nuran", "Farid", ]


@app.route('/', methods= ['GET','POST'])  # '/' for the default page
def login():
	if request.method=='POST':
		 if username==request.form['username'] and password==request.form['password']:
		 	return render_template('home.html')
		 else:
		 	return render_template('login.html')
	else:
		return render_template('login.html')

@app.route('/home')
def home():
	return render_template('home.html', friends=facebook_friends)

@app.route('/friend_exists/<string:name>',methods= ['GET','POST'])
def friend_exists(name):
	isfriend = False
	if name in facebook_friends:
		isfriend=True
	return render_template("friend_exists.html",isfriend=isfriend)





if __name__ == "__main__":  # Makes sure this is the main process
	app.run(debug=True)