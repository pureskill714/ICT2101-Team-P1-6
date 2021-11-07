from flask import Flask, render_template
app = Flask(__name__)
#index page
@app.route('/')
def hello_word():
    return render_template('index.html')

if __name__ =="__main__":
    app.run(debug=True)

#robot car connection page
@app.route('/connect')
def connection():
    return render_template('connect.html')