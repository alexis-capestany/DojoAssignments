from flask import Flask, render_template,redirect, request
import random
import datetime

app = Flask(__name__)
app.secret_key = "I <3Secrets"

def randomNum(start,end):
    num = random.randomrange(start,end)
    return num

def earnOrAdd():
    chance = randomNum(0,2)
    if chance ==1:
        return True
    else:
        return False
def addActivity(num,action,location):
    timestamp= datetime.datetime.now()
    if location == 'casino':
        if action == 'earned':
            earned = 'YES you Earned %d from the CASINO!! %s' % (num, timestamp)
            session['activity'].append (['earn',earned])
        elif action == 'lost':
            lost = 'Oops! You entered the casino and then you lost %d gold...oh no  %s' (num, timestamp)
            session['activity'].append(['lost',lost])

    elif location == 'farm':
        session['activity'].append(['earn','Earned %d from the %s! %s' % (num,location,timestamp)])
    elif location == 'cave':
            session['activity'].append(['earn','Earned %d from the %s! %s' % (num,location,timestamp)])
    elif location == 'house':
                session['activity'].append(['earn','Earned %d from the %s! %s' % (num,location,timestamp)])
    # else
    #     print "error"

@app.route('/')
def index():
    if session['total'] == None:
        session['total'] =0
    if session['activity'] ==None:
        session['activity'] =[]

return render_template("ninjagold.html", total= session['total'], activities=session['activity'])

@app.route('/process_money',methods=['POST'])
def calculateMoney():
    hiddenInput = request.form['hidden']
    if hiddenInput == 'farm':
        farmNum= randomNum(10,21)
        session['total'] += farmNum
        addActivity(farmNum,'earned', 'farm')
    elif hiddenInput == 'cave':
        caveNum = randomNum(5,10)
        session['total'] += caveNum
        addActivity(caveNum,'earned','cave')
    elif hiddenInput == 'house':
        houseNum = randomNum(2,5)
        session['total'] += houseNum
        addActivity(houseNum,'earned','house')
    elif hiddenInput == 'casino':
        casinoNum = randomNum(0,50)
        chance = earnOrAdd()
        if chance ==True:
            session['total'] += casinoNum
            addActivity(casinoNum,'earned','casino')
        elif chance == False:
            session['total'] -= casinoNum
            addActivity(casinoNum, 'lost', 'casino')
        else:
            print "Error"
# else:
#     print "Error"

# @app.route('/clear', methods=['POST'])
#     def clear():
#         session['total'] = 0
#         session['activity'] =[]
#         return redirect('/')

app.run(debug=True)
