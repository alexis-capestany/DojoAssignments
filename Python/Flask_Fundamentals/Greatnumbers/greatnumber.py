from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
def setSession():
    session['number'] = randon,randint(1,100)

@app.route('/')
def index():
    if session['number'] == None:
        setSession()
    else:
        pass
    print session['number']
    return render_template('greatnumber.html', methods=['POST'])


@app.route('/guess', methods=['POST'])
def checkNumber():
    error = None
    success = None
    guess = request.form['guess']
    if request.method == 'POST':
        if guess.isdigit():
        numguess = int(guess)
        if numguess == session ['number']:
            flash('Correct', 'success')
            return redirect('/')
        elif numguess > session['number']:
            flash('Too high', 'error')
        else:
            flash('Too low', 'error')
        else:
            flash('Not a valid guess', 'error')
        return redirect('/')
@app.route('/reset', methods=['GET', 'POST'])
def reset():
    setSession()
    return redirect('/')

app.run(debug=True)
