from flask import Flask, render_template, request, flash, redirect
from CarController import CarController
from Level import LevelController
import serial
import time

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#cmd to start project
#set FLASK_APP=WebPortal
#flask run

#instantiate new car
car=CarController("1001","123456")
conn = car.openConnection()

#index page
@app.route('/', methods=['GET', 'POST'])
def index():
    data=1
    if request.method == 'POST':
        car.closeConnection()
        flash("Close Connection")
    return render_template('index.html',data=data)


#main page
#calling connection() from carCOntroller before redirect
@app.route('/main')
def main():
    # if conn[0]:
    if True:
        flash("Robot Car is connected")
        car.setCarStat(0,0,"Connected","idle")
        data = car.getCarStat()
        return render_template('main.html',data=data) #data = what u want to pass to html page eg. see main.html
    else:
        print(conn[1])
        flash("Connection fail")
        return render_template('index.html')

@app.route('/selectlevel')
def selectlevel():
    return render_template('selectlevel.html')
@app.route('/customlevel')
def customlevel():
    return render_template('Customlevelpage.html')

@app.route('/Configlevelpage')
def Configlevelpage():
    return render_template('Configlevelpage.html')

@app.route('/gamepage', methods=['GET', 'POST'])
def game():
    car.setCarStat("10m/h", "12m", "Connected", "Idle")
    if request.method == 'POST':
        back = request.referrer
        level = request.form['level']
        print(level)
        if int(level) > 6 and int(level) != 71:
            level= "6"
            flash("Max level reached")
        map = LevelController().getMapSetUp(level)
        if map!=False:
            data = car.getCarStat()
            data["map"] = map.getMap()
            data["start"] = map.getStart()
            data["end"] = map.getEnd()
            data['level'] = map.getName()
            data['levelNum'] = map.getLevelNumber()+1
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