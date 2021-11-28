from flask import Flask, render_template, request
from CarController import CarController
app = Flask(__name__)

#cmd to start project
#set FLASK_APP=WebPortal
#flask run

#index page
@app.route('/')
def index():
    return render_template('index.html')

#instantiate new car
car=CarController("1001","123456")

#main page
#calling connection() from carCOntroller before redirect
@app.route('/main')
def main():
    if car.connection():
        car.setCarStat(0,0,"connected","idle")
        data= car.getCarStat()
        return render_template('main.html',data=data) #data = what u want to pass to html page eg. see main.html
    else:
        return render_template('index.html')

@app.route('/gamepage', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        cmd = request.form['cmdList']
    car.setCarStat("10m/h","12m","Connected","Idle")
    data = car.getCarStat()
    data["map"]=[0,1,0,0,1,1,0,0,0]
    # print(data["speed"])
    return render_template('gamepage.html',data=data)
@app.route('/maze')
def maze():
    return render_template('maze.html')
if __name__ =="__main__":
    app.run(debug=True)