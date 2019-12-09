import sqlite3

class DBService():
    """Method to insert a film record into bbdd"""
    def addFilm(self,film):
        connection = sqlite3.connect("D:\Python\Proyectos\Harpo\main\db/filmoteca.db")
        c = connection.cursor()
        c.execute("SELECT MAX(FILM_ID) +1 FROM FILMS_MAIN")
        idMax = c.fetchone()[0]

        c.execute("INSERT INTO FILMS_MAIN (FILM_ID,FILM_NAME) VALUES (?,?)",(idMax,film))
        connection.commit()
        connection.close()


