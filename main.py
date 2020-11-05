#Import
from flask import Flask, render_template

#Create Flask
app = Flask(__name__)

#home
@app.route('/')
def home():
    return render_template("home.html")

#RSA Demonstration Page
@app.route('/rsa')
def rsaEx():
    return render_template('rsa.html')
#RSA Info Page
@app.route('/rsa/about')
def rsaAbout():
    return render_template('rsaAbout.html')

if __name__ == "__main__":
    app.run(debug=True)