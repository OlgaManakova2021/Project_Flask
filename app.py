from flask import Flask

app = Flask(__name__)

@app.route("/")   # 127.0.0.1:5000 + /  =  127.0.0.1:5000/
def index():
    return "Главная страница"

@app.route("/example")
def example():
    return "Hello example!"


if __name__ == "__main__":
    app.run()