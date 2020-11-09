#import "Flask"
from flask import Flask, render_template

#create "Flask"
app = Flask(__name__)

#links dictionary
links = {
    'index': 'Home',
    'rsa': "RSA",
    'resources': 'GitHub',
    'test': 'test'}

#home
@app.route('/')
def home():
    return render_template("Index2.0.html")

#binary game
@app.route('/binary')
def binaryEX():
    return render_template("home.html", links = links)
#rsa demonstration
@app.route('/rsa')
def rsaEX():
    return render_template("rsa.html", links = links)
#rsa info
@app.route('/rsa/about')
def rsaAbout():
    return render_template("rsaAbout.html")

#run file
if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)
