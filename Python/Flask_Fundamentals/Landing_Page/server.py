from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    print "this works"
    return render_template('index.html', greeting="hello welcome to flask")


@app.route('/ninjas')
def world2():
    return render_template('ninjas.html', stuff="NOWAY")


@app.route('/dojo')
def world3():
    return render_template('dojo.html',name="no" )


app.run(debug=True)
