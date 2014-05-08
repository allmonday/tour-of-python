from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return open('content.html','r').read()

@app.route("/name")
def say_name():
    content = open("log",'r').read()
    return content

if __name__ == "__main__":
    app.run()
