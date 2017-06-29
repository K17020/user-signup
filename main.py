from flask import Flask, request, redirect,render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/signup", methods=['POST'])
def welcome():
# getting user information from form
    username = request.form['username']
    password = request.form['password']
    verifypwd = request.form['verify_password']
    email = request.form['userEmail']

# empty string for error message
    username_error = ''
    password_error = ''
    verifypwd_error = ''
    email_error = ''

# checks to see if the username and password is vaild base off these requirments
    if len(username) < 4 or len(username) > 20 or ' ' in username:
        username_error = "That's not a vaild username"
        return render_template('index.html', username=username, username_error=username_error,)

    if len(password) < 4 or len(password) > 20 or ' ' in password:
        password_error = "That's not a vaild password"
        return render_template('index.html', username=username, password_error=password_error)

    if password != verifypwd:
        verifypwd_error = "That password didn't match"
        return render_template('index.html', username=username, verifypwd_error=verifypwd_error)
    if len(email) > 1:
        if len(email) < 4 or len(email) > 20 or '' in email or '@' not in email:
            email_error = 'enter a valid email'
            return render_template('index.html', username=username, userEmail=email, email_error=email_error)
    
    return render_template('welcome.html', username=username)
app.run()