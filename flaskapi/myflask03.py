#!/usr/bin/python3
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/audri")
def hello_admin():
    return "Hello Audri, how are you feeling this morning?"

@app.route("/jason")
def hello_guest():
    return f"Hello Jason"
    #V2 FORMATTER - return "Hello {} Guest".format(guesty)
    #OLD FORMATTER - return "Hello %s as Guest" % guesty

@app.route("/user")
def hello_user():
    ## if you go to hello_user with a value of admin
    if name =="lost":
        # return a 302 response to redirect to /admin
        return redirect(url_for("hello_admin"))
    else:
        # return a 302 response to redirect to /guest/<guesty>
        return redirect(url_for("hello_guest",guesty = name))

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

