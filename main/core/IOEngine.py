from main.core.FolderManagement import FolderManagement
from main.db.DBService import DBService
from main.common.Constants import Constans

cte = Constans()
fm = FolderManagement()
db = DBService()

class IOEngine():

    def refreshRepositoryDeleting(self, repository):

        if repository == 'FAKE':
            table = cte.FILMS_FAKE
            directory = cte.FAKE_FILMS_PATH
        else:
            table = cte.FILMS_MAIN
            directory = cte.MAIN_FILMS_PATH

        recordedMovieList = db.getAllFilms(table)
        movieList = fm.getAllMoviesInTheDirectory(directory)

        for record in recordedMovieList:
            if record not in movieList:
                db.deleteFilm(record,table)

    def refreshRepositoryAdding(self, repository):

        if repository == 'FAKE':
            table = cte.FILMS_FAKE
            directory = cte.FAKE_FILMS_PATH
        else:
            table = cte.FILMS_MAIN
            directory = cte.MAIN_FILMS_PATH

        self.refreshRepositoryDeleting(repository)
        movieList = fm.getAllMoviesInTheDirectory(directory)

        for movie in movieList:
            isRecorded = db.checkIfIsIn(movie,table)
            if isRecorded == 0:
                db.addFilm(movie,table)


