from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "hola mochis!"
@app.route("index")
    return open("index.html").read()
if __name__ == "__main__":
    app.run()
