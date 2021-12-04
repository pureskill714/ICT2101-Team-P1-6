from flask import Flask, render_template
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
        return render_template('main.html', data=data) #data = what u want to pass to html page eg. see main.html
    else:
        return render_template('index.html')

@app.route('/selectlevel')
def selectlevel():
    return render_template('selectlevel.html')

@app.route('/Configlevelpage')
def Configlevelpage():
    return render_template('Configlevelpage.html')

if __name__ =="__main__":
    app.run(debug=True)