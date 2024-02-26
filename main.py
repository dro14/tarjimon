from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer
from translate import translate

# INIT APP
app = Flask(__name__)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


# Config app
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///translation.db"
db = SQLAlchemy(model_class=Base)
# Init app with Extension
db.init_app(app)


# CREATE TABLE
class Translation(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    uzb: Mapped[str] = mapped_column(String, nullable=False)
    eng: Mapped[str] = mapped_column(String, nullable=False)


# Create Table Schema in DB
with app.app_context():
    db.create_all()


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# About Page
@app.route("/biz-haqimizda")
def about():
    print(request)
    return render_template("about.html")


@app.route("/kontakt")
def contact():
    print(request)
    return render_template("contact.html")


@app.route("/translate", methods=["POST"])
def translate_endpoint():
    text_data = request.form["eng-field"]
    translated_text = translate(text_data)
    translation = Translation(uzb=text_data, eng=translated_text)
    db.session.add(translation)
    db.session.commit()
    return translated_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)

# #006C80 --> Color Primary
