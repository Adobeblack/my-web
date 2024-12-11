from flask import Flask,render_template,request
from flask_mysqldb import MySQL 
from flask import url_for,redirect,session
from flask_session import Session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/aboutme')
def aboutme():
    return render_template("aboutme.html")

@app.route('/product')
def products():
    return render_template("product.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/layout')
def layout():
    return render_template("layout.html")

@app.route('/sendData')
def signupFrom():
    fname=request.args.get('fname')
    description=request.args.get('description')
    return render_template("thankyou.html",data={"name":fname,"description":description})

@app.route('/hello/<user>/<int:passw>')
def hello_name(user,passw):
    return render_template('hello.html', name = user, passw = passw)

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html', status = '')


if __name__ == "__main__":
    app.run(debug=True)

