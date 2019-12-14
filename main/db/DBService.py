import sqlite3
from main.common.Constants import Constans

cte = Constans()

class DBService():
    """Data base management service class"""

    """Method to insert a film record into any film table"""
    def addFilm(self,film,table):
        connection = sqlite3.connect(cte.DATABASE_PATH)
        c = connection.cursor()
        c.execute("SELECT MAX(FILM_ID) +1 FROM {}".format(table))
        idMax = c.fetchone()[0]
        c.execute("INSERT INTO {} (FILM_ID,FILM_NAME) VALUES (?,?)".format(table),(idMax,film))
        connection.commit()
        connection.close()

    """Remove a film record from the any film table"""
    def deleteFilm(self,film,table):
        connection = sqlite3.connect(cte.DATABASE_PATH)
        c = connection.cursor()
        c.execute("DELETE FROM {} WHERE FILM_NAME = ?".format(table),(film,))
        connection.commit()
        connection.close()

    """Method to check if a film is in the table"""
    def checkIfIsIn(self,film,table):
        connection = sqlite3.connect(cte.DATABASE_PATH)
        c = connection.cursor()
        c.execute("SELECT COUNT(*) FROM {} WHERE FILM_NAME LIKE '{}'".format(table,film))
        response = c.fetchone()[0]
        connection.close()
        return response

    def getAllFilms(self, table):
        response = []
        connection = sqlite3.connect(cte.DATABASE_PATH)
        c = connection.cursor()
        c.execute("SELECT  FILM_NAME FROM {} ".format(table))
        rawList = c.fetchall()
        for item in rawList:
            response.append(item[0])
        connection.close()
        return response




