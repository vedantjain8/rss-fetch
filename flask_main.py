from flask import Flask,render_template, url_for
from flask_fetch import post

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title = "Home", posts = post)

@app.route("/about")
def about():
    return render_template('about.html',title = "About")


if __name__ == '__main__':
    app.run(debug=True)