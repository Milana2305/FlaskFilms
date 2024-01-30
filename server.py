from flask import Flask, render_template, g
import sqlite3
import Base
import forms

app = Flask(__name__)
app.config['DATABASE'] = "static/bd/films.db"
app.secret_key = "1qaz2wsx"

def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con

def connect_db_forms():
    con = sqlite3.connect(app.config['DATABASE'])
    return con

def get_connect():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

def get_connect_forms():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db_forms()
    return g.link_db

navMenu = [
    {"link": "/index", "name": "Главная"},
    {"link": "/add", "name": "Добавить фильм"}
]

@app.route("/film/1")
def film_1():
    base = Base.FilmDB(get_connect())
    return render_template("film.html", cards=base.getAllFilms())

@app.route("/film/2")
def film_2():
    base = Base.FilmDB(get_connect())
    return render_template("film1.html", cards=base.getAllFilms())

@app.route("/film/3")
def film_3():
    base = Base.FilmDB(get_connect())
    return render_template("film2.html", cards=base.getAllFilms())

@app.route("/film/4")
def film_4():
    base = Base.FilmDB(get_connect())
    return render_template("film3.html", cards=base.getAllFilms())

@app.route("/film/5")
def film_5():
    base = Base.FilmDB(get_connect())
    return render_template("film4.html", cards=base.getAllFilms())

@app.route("/film/6")
def film_6():
    base = Base.FilmDB(get_connect())
    return render_template("film5.html", cards=base.getAllFilms())

@app.route("/index")
@app.route("/")
def index():
    base = Base.FilmDB(get_connect())
    return render_template("index.html", menu=navMenu, cards=base.getAllFilms())

@app.route("/add", methods= ["POST", "GET"])
def add():
    addForm = forms.AddFilmsForm()
    base = Base.FilmDB(get_connect_forms())
    render_template("add_form.html", menu=navMenu, form =addForm)
    listForm = [addForm.nameFilm.data,
            addForm.year.data,
            addForm.country.data,
            addForm.genre.data,
            addForm.premiere.data,
            addForm.age.data,
            addForm.review.data,
            addForm.img.data]
    flag = True
    for i in listForm:
        if i == None:
            flag = False
    if (flag==True):
        base.addFilms(
            addForm.nameFilm.data,
            addForm.year.data,
            addForm.country.data,
            addForm.genre.data,
            addForm.premiere.data,
            addForm.age.data,
            addForm.review.data,
            addForm.img.data)
    return render_template("add_form.html", menu=navMenu, form =addForm)

@app.teardown_appcontext
def close_connect(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

if __name__ == "__main__":
    app.run()
