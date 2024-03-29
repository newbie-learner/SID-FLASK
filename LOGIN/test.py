from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route("/")
def greeting():
    return "<h1 style='color:green'>Hello World!</h1>"
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('greeting'))
    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run()
