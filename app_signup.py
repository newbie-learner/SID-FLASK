from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route("/signup", methods=["GET", "POST"])
def SignuPage():
    if request.method == "POST":
        import pdb;pdb.set_trace()
        fullname = request.form.get('fullname')
        emailadr = request.form.get('emailadd')
        passw = request.form.get('password1')
        phnmbr1 = request.form.get('phnmbr')
        print(fullname, emailadr, passw, phnmbr1)
        return "<h1> Signup Successfull {} : {} :{} :{}</h1>".format(fullname, emailadr, passw, phnmbr1)
    return render_template("SignUp.html")

# Start the server with run method
if __name__ == '__main__':
    app.run(debug=True)
