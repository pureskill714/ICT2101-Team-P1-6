
from flask import Flask, render_template, request, flash
from CarController import CarController
import serial
import time

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#cmd to start project
#set FLASK_APP=WebPortal
#flask run

#index page
@app.route('/')
def index():
    return render_template('index.html')

#instantiate new car
car=CarController("1001","123456")
conn = car.openConnection()
#main page
#calling connection() from carCOntroller before redirect
@app.route('/main')
def main():
    # if conn[0]:
    if True:
        flash("Connect successfully")
        car.setCarStat(0,0,"connected","idle")
        data= car.getCarStat()
        return render_template('main.html',data=data) #data = what u want to pass to html page eg. see main.html
    else:
        print(conn[1])
        flash("Connection fail")
        return render_template('index.html')

@app.route('/selectlevel')
def selectlevel():
    return render_template('selectlevel.html')

@app.route('/Configlevelpage')
def Configlevelpage():
    return render_template('Configlevelpage.html')

@app.route('/gamepage', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        cmd = request.form['cmdList']
    car.setCarStat("10m/h","12m","Connected","Idle")
    data = car.getCarStat()
    data["map"] = [[1,1,0],[1,0,0],[0,0,1]]
    data["start"] = [0,2]
    data["end"] = [2,0]
    # print(data["speed"])
    return render_template('gamepage.html',data=data)

#background process happening without any refreshing
@app.route('/sendcommand')
def background_process_test():
    cmd = request.args.get('cmd')
    print(f"cmd received={cmd}")
    # connected = car.testConnection(conn)
    # if connected[0]:
    #     result = car.sendCommand(connected[1],cmd)
    # # flash(result)
    #     print(result[1])
    # else:
    #     print(connected[1])
    # if(result[0]):
    #     flash("success"+result[1])
    # else:
    #     flash("failed"+result[1])
    return ("nothing")

if __name__ =="__main__":
    app.run(debug=True)