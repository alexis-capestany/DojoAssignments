from flask import Flask, render_template, request, redirect,flash
app = Flask(__name__)
app.secret_key = "I<3Secrets"

@app.route('/')

def hello_flask():
    return render_template("index.html", greeting="hello welcome to Flask", other=4)

@app.route('/users',methods=['POST'])
def users():
    print request.form['first_name']
    print type(request.form['number'])

    flash("user name entered ok.")
    flash("user name entered not okay")
    flash("user name entered kindofok")
    flash("username entered yes!")

    return redirect('showusers')
@app.route('/showusers')
def show():
    return render_template("users.html")
@app.route('clear')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True, port=int("5555"))
