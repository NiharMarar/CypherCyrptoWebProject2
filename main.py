#imports

from flask import Flask, render_template, request, redirect
import rsa

#create "Flask"
app = Flask(__name__)

#links dictionary
links = {
    'index': 'Home',
    'rsa': "RSA",
    'resources': 'GitHub',
    'test': 'test'}

def Binary_to_Text(binary):

    binary1 = binary
    decimal, d, n = 0, 0 , 0
    while (binary != 0):
        deci = binary % 10
        decimal = decimal + deci * pow(2, d)
        binary = binary//10
        d += 1
    return(decimal)

#home
@app.route('/')
def home():
    return render_template("homepage.html")

#rsa demonstration
#default RSA (rsa encrypt)
@app.route ("/rsa", methods = ["POST", "GET"])
def rsaEncrypt ():
    if request.method == "POST":
        #get message
        message = request.form["msg"]
        #get keys
        pubKey1 = int(request.form["pubKey1"])
        pubKey2 = int(request.form["pubKey2"])
        #get encrypted and make into useable output
        encrypted = rsa.rsa(message, pubKey1, pubKey2)
        encrypted = encrypted[0]
        encrypted = ''.join(encrypted)
        #render page with output
        return render_template ("rsa.html", output = encrypted, op1 = "KeyGenerator", op2 = "Decrypt")
    #render page without output
    else:
        return render_template ("rsa.html", output = "pending", op1 = "KeyGenerator", op2 = "Decrypt")


#rsa info
@app.route('/rsa/about')
def rsaAbout():
    return render_template("rsaAbout.html")

#CeaserCipher game
@app.route('/CeaserCipher')
def CeaserCipher():
    return render_template("CeaserCipher.html", links = links)

#---------------------------------------------------------------------------
#runs CeaserCipher Game encryption
@app.route("/CeaserCipher_encrypt", methods=['GET','POST'])
def encryptionCC():
    if request.method == 'POST':
        form = request.form
        text1 = form["CeaserCipher1"]
        s = int(form["s"])
        def encryptionCC1(text1,s):
            result = []
        # transverse the plain text

        # for letter in text1:
            for i in range(0,len(text1)):
                char = text1[i]
        # Encrypt uppercase characters in plain text

                if (char.isupper()):
                    L = chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
                elif (char.islower()):
                    L = chr((ord(char) + s - 97) % 26 + 97)
                else:
                    L = chr(ord(char))
                result.append(L)
            return result
        result1=encryptionCC1(text1,s)
        encrypted="".join(result1)
        return render_template("CeaserCipher.html", display = encrypted)
    return redirect("/CeaserCipher")
#----------------------------------------------------------------------------------------------------------
#runs CeaserCipher Game decryption
@app.route("/CeaserCipher_decrypt", methods=['GET','POST'])
def decryptionCC():

    if request.method == 'POST':
        form = request.form
        encrp_msg = form["CeaserCipher1"]
        decrp_key = int(form["s"])

        decrypted_text = []

        for i in range(len(encrp_msg)):
            if ord(encrp_msg[i]) == 32:
                decrypted_text += chr(ord(encrp_msg[i]))

            elif ((ord(encrp_msg[i]) - decrp_key) < 97) and ((ord(encrp_msg[i]) - decrp_key) > 90):
            # subtract key from letter ASCII and add 26 to current number
                temp = (ord(encrp_msg[i]) - decrp_key) + 26
                decrypted_text += chr(temp)

            elif (ord(encrp_msg[i]) - decrp_key) < 65:
                temp = (ord(encrp_msg[i]) - decrp_key) + 26
                decrypted_text += chr(temp)

            else:
                decrypted_text += chr(ord(encrp_msg[i]) - decrp_key)

        decrypted="".join(decrypted_text)
        return render_template("CeaserCipher.html", display = decrypted)
    return redirect("/CeaserCipher")

#Caesar Cipher Information Page
@app.route('/CaesarCipherInfo')
def CaesarCipherInfo():
    return render_template("CaesarCipherInfo.html", links = links)
#------------------------------------------------------------------------------------------------------------
#binary game
@app.route('/binary')
def binaryEX():
    return render_template("Binary.html", links = links)

#runs Binary Cipher encryption
@app.route("/bin_encrypt", methods=['GET','POST'])
def encryption():
    if request.method == 'POST':
        form = request.form
        B_text = form["bin1"]
        result = ''.join(format(ord(i), 'b') for i in B_text)
        return render_template("Binary.html", display = result)
    return redirect("/binary")

#runs Binary Cipher decryption
@app.route("/bin_decrypt", methods=['GET','POST'])
def decryption():
    if request.method == 'POST':
        form = request.form
        B_text = form["bin1"]
        string = ' '
        for d in range(0, len(B_text), 7):
            temporary = int(B_text[d:d + 7])
            decimal_data = Binary_to_Text(temporary)
            string = string + chr(decimal_data)
        return render_template("Binary.html", display = string)
    return redirect("/binary")

@app.route("/BinaryInfo")
def BinaryInfo():
    return render_template("BinInfo.html")

#run file
if __name__ == "__main__":
    app.run(host = '127.0.0.1', debug = True)
