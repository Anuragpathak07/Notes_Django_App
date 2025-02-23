from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/products")
def products():
    return "<p>Hello, this is the product page</p>"

@app.route("/home")
def home_page():
    return "<p>Hello, this is the home page, tell me more about you</p>"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
