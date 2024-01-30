from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import length


class AddFilmsForm(FlaskForm):
    nameFilm = StringField("Название фильма")
    year = IntegerField("Год производства")
    country = StringField("Старана")
    genre = StringField("Жанр")
    premiere = StringField("Примьера")
    age = StringField("Возраст")
    review = StringField("Обзор на фильм")
    img = StringField("Название картинки")
    sub = SubmitField("Добавить")
