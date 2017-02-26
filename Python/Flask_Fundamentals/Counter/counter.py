from flask import Flask, render_template,redirect, request, session

app = Flask(__name__)
app.secret_key = "I <3Secrets"

@app.route('/')
def hello_flask():
    return render_template("counter.html",message="This is a counter!")
    sumSessionCount()
    return render_template('counter.html')

def count(methods=['POST']):
    if "count" not in session:
        session["count"]+=1
    else:
        session["count"]=1
    return render_template("counter.html")



app.run(debug=True)
