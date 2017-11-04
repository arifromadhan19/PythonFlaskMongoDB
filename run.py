from flask import Flask

app = Flask(__name__)

@app.route("/")
def hallo():
    return "Hallo Python"

if __name__ == '__main__':
    app.run()