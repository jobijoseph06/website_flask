from datetime import datetime


from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message


#flask instance
app = Flask(__name__)

#default
app.config["SECRET_KEY"] = "myapplication123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "bear062005@gmail.com"
app.config["MAIL_PASSWORD"] = "xoqn lztg noag ktdh"

#database instance
db = SQLAlchemy(app)

#mail instance
mail = Mail(app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.String(80))
    occupation = db.Column(db.String(80))

@app.route("/", methods=["GET", "POST"])
def index():
    print(request.method)
    if request.method == "POST":
        #getting the datas from the page
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        og_date = datetime.strptime(date, "%Y-%m-%d")
        occupation = request.form["occupation"]

        form = Form(first_name=first_name, last_name=last_name,
                    email=email,date= og_date, occupation=occupation)
        db.session.add(form)
        db.session.commit()
        #mail part
        message_body = f"Thank you for your submission, {first_name}"\
                       f"Here are your data:\n{first_name}\n{last_name}\n{date}\n"\
                       f"Thank you!"
        message = Message(subject="New form submission",
                          sender=app.config["MAIL_USERNAME"],
                          recipients=[email],
                          body=message_body)
        mail.send(message)

      #message
        flash(f"{first_name},Your form was submitted successfully!", "success")


    return render_template("index.html")

#run the app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)