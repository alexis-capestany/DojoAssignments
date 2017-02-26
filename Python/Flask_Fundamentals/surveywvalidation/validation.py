from flask import Flask, render_template, request, redirect
app= Flask(__name__)

@app.route('/')
def hello_flask():
    return render_template("survey.html",greeting="hello welcome!")

@app.route('/results', methods =['POST'])
def results():
        print request.form ['name']
        print request.form ['location']
        print request.form ['language']
        print request.form ['description']
        return redirect('/')

app.run(debug=True)
