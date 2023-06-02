#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route("/hello/tlg")
def hello_tlg():
    return f"Hello TLG"
    ## V2 STYLE STRING FORMATTER - return "Hello {}".format(name)
    ## OLD STYLE STRING FORMATTER - return "Hello %s!" % name

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

