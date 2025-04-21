from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "규현이 지금 뭐해"

if __name__ == "__main__":
    app.run(debug=True)
