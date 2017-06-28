from flask import Flask, request, redirect,render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    password = request.form['password']
    verify_pwd = request.form['verify_password']

    if len(username) == 0:
        return render_template('welcome.html', username=username)
app.run()