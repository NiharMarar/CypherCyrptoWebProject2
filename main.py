#import "Flask"
from flask import Flask, render_template, url_for, request, redirect

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

@app.route("/bin_encrypt", methods=['GET','POST'])
def encryption():
    if request.method == 'POST':
        form = request.form
        B_text = form["bin1"]
        result = ''.join(format(ord(i), 'b') for i in B_text)
        return render_template("home.html", display = result)
    return redirect("/home")

@app.route("/bin_decrypt", methods=['GET','POST'])
def decryption():
    if request.method == 'POST':
        form = request.form
        def Binary_to_Text(binary):

            binary1 = binary
            decimal, d, n = 0, 0 , 0
            while (binary != 0):
                deci = binary % 10
                decimal = decimal + deci * pow(2, d)
                binary = binary//10
                d += 1
            return(decimal)
        B_text = form["bin1"]
        string = ' '
        for d in range(0, len(B_text), 7):
            temporary = int(B_text[d:d + 7])
            decimal_data = Binary_to_Text(temporary)
            string = string + chr(decimal_data)
        return render_template("home.html", display = string)
    return redirect("/home")

#run file
if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)
