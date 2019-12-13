import os
from main.common.Constants import Constans

cte = Constans()

class FolderManagement():
    """This class has folder management methods"""

    """Get a list of movies in the input directory"""
    def getMovieList(self,directory):
        listWithFolders = os.listdir(directory)
        listWithoutFolders = []

        for item in listWithFolders:
            if ".mkv" in item:
                listWithoutFolders.append(item.replace(".mkv",""))
            if ".avi" in item:
                listWithoutFolders.append(item.replace(".avi",""))

        return listWithoutFolders

    """Get a list of folder in the input directory"""
    def getFolderList(self,directory):

        listWithMovies = os.listdir(directory)
        listWithoutMovies = []

        for item in listWithMovies:
            if ".mkv" not in item and ".avi" not in item and ".db" not in item:
                listWithoutMovies.append(item)
        return listWithoutMovies

    def getAllMoviesInTheDirectory(self, directory):

        movieList = self.getMovieList(directory)
        folderList = self.getFolderList(directory)

        if len(folderList) > 0:
            movieList1 = []
            for item in folderList:
                movieList1 = self.getMovieList(directory + "/" + item)
                print(directory + "/" + item)
                print(len(movieList1))
                for movie in movieList1:
                    movieList.append(movie)

        return movieList




