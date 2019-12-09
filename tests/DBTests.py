import unittest
import sqlite3
from main.db.DBManagement import DBService

class DataBaseTesting(unittest.TestCase):

    def test_addFilm(self):
        db = DBService()
        film = "RAN"
        db.addFilmToMain(film)
        connection = sqlite3.connect("D:\Python\Proyectos\Harpo\main\db/filmoteca.db")
        c = connection.cursor()
        c.execute("SELECT * FROM FILMS_MAIN WHERE FILM_NAME = ?", (film,))
        filmName = c.fetchone()[1]
        self.assertEqual(film,filmName,"Incorrect data record")
        connection.close()


    def test_addSameFilmSeveralTimes(self):
        db = DBService()
        film = "DIRTY DANCING"
        db.addFilmToMain(film)
        db.addFilmToMain(film)

    def test_deleteFilm(self):
        db = DBService()
        film = "RAN"
        db.deleteFilmFromMain(film)
        connection = sqlite3.connect("D:\Python\Proyectos\Harpo\main\db/filmoteca.db")
        c = connection.cursor()
        c.execute("SELECT * FROM FILMS_MAIN WHERE FILM_NAME = ?", (film,))
        filmName = c.fetchone()[1]
        print(filmName)
        #self.assertEqual(None,filmName,"The record shouldn't exist")
        connection.close()

