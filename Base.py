import sqlite3

class FilmDB:
    def __init__(self, connect: sqlite3.Connection) -> None:
        self.__connect = connect
        self.__cursor = connect.cursor()

    def getAllFilms(self):
        sql = "SELECT id, nameFilm, year, country, genre, premiere, age, review, img FROM films"
        try:
            self.__cursor.execute(sql)
            return self.__cursor.fetchall()
        except:
            print("Ошибка чтения из БД")
            return []
        
    def addFilms(self, nameFilm, year, country, genre, premiere, age, review, img): #
        
        try:
            sql = "INSERT INTO films(nameFilm, year, country, genre, premiere, age, review, img) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            self.__cursor.execute(sql, tuple([nameFilm, year, country, genre, premiere, age, review, img])) #
            self.__connect.commit()
            
            return self.__cursor.fetchall()
        except:
            price("ошибка добавления данных")
            return False