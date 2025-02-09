from flask import Flask , render_template

#flask instance
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

#run the app
app.run(debug=True, port=5001)