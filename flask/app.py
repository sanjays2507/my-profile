from flask import Flask,render_template
import jinja2

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("about.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")


if __name__ == '__main__':
    app.run(debug=True)