from flask import *
import fetchBackendData as fdb
import random as r
import json
import sendOtp
import success

app = Flask(__name__)


@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = str(request.form.get("username"))
        password = str(request.form.get("password"))
        usernames = fdb.fetchAllUserName()
        if username in usernames:
            credentials = fdb.fetchCreds()
            passwordFromBackend = credentials[username]
            if password == passwordFromBackend:
                return render_template("success.html")
            else:
                return render_template("wrongPassword.html")
        else :
            return render_template("wrongUsername.html")
    return render_template("index.html")

@app.route("/register", methods = ["GET", "POST"])
def register():
    otp_object = {}
    userObject = {}
    if request.method == "POST":
        firstname = str(request.form.get("regfirstname"))
        username = str(request.form.get("regUser"))
        password = str(request.form.get("regPass"))
        email = str(request.form.get("regEmail"))
        GeneratedOTP = r.randint(100000,999999)
        if firstname is not None:
            otpFile = open("otpFile.txt", "w")
            otpFile.write(str(GeneratedOTP))
            otpFile.close()
            sendOtp.sendEmail(email, GeneratedOTP)
            userObject["firstname"] = firstname
            userObject["username"] = username
            userObject["password"] = password
            userObject["email"] = email
            userDataFile = open("userData.txt", "w")
            userDataFile.write(str(userObject))
            userDataFile.close()
            return redirect("/otpVerification")
    return render_template("register.html")

@app.route("/otpVerification", methods = ["GET", "POST"])
def otpVerification():
    otpFromFile = open("otpFile.txt", "r")
    otpActual = otpFromFile.read().strip()
    otpFromFile.close()

    userDataFile = open("userData.txt", "r")
    userData = userDataFile.read().strip()
    userDataFile.close()
    k = userData.replace("'", '"')
    userObject = json.loads(k)

    if request.method == "POST":
        otpValue = str(request.form.get("otpVal"))
        if otpValue is not None:
            print(otpValue)
            if otpActual == otpValue:
                fdb.enterData( userObject["firstname"], userObject["username"],userObject["password"],userObject["email"])
                success.sendEmail(userObject["email"], userObject["username"], userObject["password"])
                return render_template("registrationSuccessful.html")
            else:
                return render_template("OTP_verification.html")
          
    return render_template("OTP_verification.html")



app.run(debug=True, port=3333)