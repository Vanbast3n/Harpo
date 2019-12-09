import sqlite3
from main.common.Constants import Constans

cte = Constans()
class DBService():
    """Data base management service class"""

    """Method to insert a film record into FILMS_MAIN table"""
    def addFilmToMain(self,film):
        connection = sqlite3.connect("D:\Python\Proyectos\Harpo\main\db/filmoteca.db")
        c = connection.cursor()
        c.execute("SELECT MAX(FILM_ID) +1 FROM FILMS_MAIN")
        idMax = c.fetchone()[0]
        c.execute("INSERT INTO FILMS_MAIN (FILM_ID,FILM_NAME) VALUES (?,?)",(idMax,film))
        connection.commit()
        connection.close()

    """Remove a film record from the FILMS_MAIN table"""
    def deleteFilmFromMain(self,film):
        connection = sqlite3.connect("D:\Python\Proyectos\Harpo\main\db/filmoteca.db")
        c = connection.cursor()
        c.execute("DELETE FROM FILMS_MAIN WHERE FILM_NAME = ?",(film,))
        connection.commit()
        connection.close()

    """Method to insert a film record into FILMS_FAKE table"""
    def addFilmToFake(self,film):
        connection = sqlite3.connect("D:\Python\Proyectos\Harpo\main\db/filmoteca.db")
        c = connection.cursor()
        c.execute("SELECT MAX(FILM_ID) +1 FROM FILMS_FAKE")
        idMax = c.fetchone()[0]
        c.execute("INSERT INTO FILMS_FAKE (FILM_ID,FILM_NAME) VALUES (?,?)",(idMax,film))
        connection.commit()
        connection.close()

    """Remove a film record from the FILMS_FAKE table"""
    def deleteFilmFromFake(self,film):
        connection = sqlite3.connect("D:\Python\Proyectos\Harpo\main\db/filmoteca.db")
        c = connection.cursor()
        c.execute("DELETE FROM FILMS_FAKE WHERE FILM_NAME = ?",(film,))
        connection.commit()
        connection.close()


