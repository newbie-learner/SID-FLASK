# import flask class from the flask module
from flask import Flask, render_template, redirect, request, url_for

# Create the application as a Object
app = Flask(__name__)


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
    if request.method == "POST":
        #import pdb;pdb.set_trace()
        print("Hello")
        if (request.form.get('username') != 'admin' or request.form.get('password') != 'admin'):
             print("Hello1")
             #return redirect(url_for('home'))
             error = 'Invalid Credentials. Please try again.'
        else:
            print("Hi")
            return redirect(url_for('welcome'))
    return render_template('login-1.html', error=error)

# Start the server with run method
if __name__ == '__main__':
    app.run(debug=True)
