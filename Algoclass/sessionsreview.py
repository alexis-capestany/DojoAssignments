from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
        return render_template("index.html")
@app.route('/users', methods=['POST'])
def create_user():
    print "GOT THE POST INFO"
    name = request.form['name']
    email = request.form['email']
    return redirect('/')
@app.route('show')
    return render_template('user.html',name='Jay', email="esgjfngsf")
app.run(debug=True)
