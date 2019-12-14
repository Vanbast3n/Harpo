import unittest
import sqlite3
from main.db.DBService import DBService

class DataBaseTesting(unittest.TestCase):

    def test_addFilm(self):
        db = DBService()
        film = "THE LAST SAMURAI"
        table = 'FILMS_FAKE'
        db.addFilm(film,table)
        connection = sqlite3.connect("D:\Python\Proyectos\Harpo\main\db/filmoteca.db")
        c = connection.cursor()
        c.execute("SELECT * FROM FILMS_FAKE WHERE FILM_NAME = ?", (film,))
        filmName = c.fetchone()[1]
        self.assertEqual(film,filmName,"Incorrect data record")
        connection.close()

    def test_addSameFilmSeveralTimes(self):
        db = DBService()
        film = "DIRTY DANCING"
        table = 'FILMS_FAKE'
        db.addFilm(film,table)
        db.addFilm(film,table)

    def test_deleteFilm(self):
        db = DBService()
        film = "RAN"
        table = 'FILMS_FAKE'
        db.deleteFilm(film,table)
        filmOutCheck = db.checkIfIsIn(film, table)

        self.assertEqual(0,filmOutCheck,"The record shouldn't exist")


    def test_checkIfIsIn(self):
        db = DBService()
        filmIn = "THE LAST samurai"
        filmIn2 = "RAN"
        filmOut = "AVATAR"
        table = 'FILMS_FAKE'
        filmInCheck = db.checkIfIsIn(filmIn,table)
        filmInCheck2 = db.checkIfIsIn(filmIn2, table)
        filmOutCheck = db.checkIfIsIn(filmOut,table)

        self.assertEqual(1,filmInCheck,"The film {} is not in the table {}".format(filmIn,table))
        self.assertEqual(1,filmInCheck2,"The film {} is not in the table {}".format(filmIn2,table))
        self.assertEqual(0,filmOutCheck,"The film {} is in the data table {}".format(filmOut,table))

    def test_getAllFilms(self):
        db = DBService()
        table = 'FILMS_FAKE'
        movieList = db.getAllFilms(table)
        print(movieList)