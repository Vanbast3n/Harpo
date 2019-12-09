import unittest
import sqlite3
from main.db.DBManagement import DBService

class DataBaseTesting(unittest.TestCase):

    def test_addFilm(self):
        db = DBService()
        film = "RAN"
        db.addFilm(film)
        connection = sqlite3.connect("D:\Python\Proyectos\Harpo\main\db/filmoteca.db")
        c = connection.cursor()
        c.execute("SELECT * FROM FILMS_MAIN WHERE FILM_NAME = ?", (film,))
        print (c.fetchall())
        connection.close()

    def test_addSameFilmSeveralTimes(self):
        db = DBService()
        film = "DIRTY DANCING"
        db.addFilm(film)
        db.addFilm(film)