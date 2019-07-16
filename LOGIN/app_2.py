# import flask class from the flask module
from flask import Flask, render_template, redirect, request, url_for
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, AnyOf

# Create the application as a Object
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisismysecretkey'

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(message="A username is required"), Length(min=5, max=10, message="Input required 5 and 10")])
    password = PasswordField('password', validators=[InputRequired(message="A password is required"), AnyOf(values=['password','secret'])])
# Use decorator to link the function to a URL
@app.route("/")
def home():
    return "Hello SID" # return a String

@app.route("/welcome")
def welcome():
    return render_template('welcome.html') # render a template

# Route for handling the login page logic
@app.route("/login", methods=['GET', 'POST'])
def login():
    # import pdb;pdb.set_trace()
    error = None
    form3 = LoginForm()
    if form3.validate_on_submit():
    #if request.method=="POST":
        return "<h1>The username is {}. The password is {} </h1>".format(form3.username.data, form3.password.data)
    return render_template('login-3.html', error=error,form=form3)

# Start the server with run method
if __name__ == '__main__':
    app.run(debug=True)
