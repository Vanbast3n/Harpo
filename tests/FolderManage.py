import unittest
import os
from main.core.FolderManagement import FolderManagement
from main.common.Constants import Constans

class FolderManage(unittest.TestCase):

    def test_getMovieList(self):
        cte = Constans()
        fm = FolderManagement()
        directory = cte.FAKE_FILMS_PATH
        path, dirs, files = next(os.walk(directory))

        numberOfMovies = len(fm.getMovieList(directory))
        self.assertEqual(numberOfMovies,len(files)-1,"There is no all the movies of the directory in the list {a}".format(a=numberOfMovies))


    def test_getFolderList(self):
        cte = Constans()
        fm = FolderManagement()
        directory = cte.FAKE_FILMS_PATH
        path, dirs, files = next(os.walk(directory))

        numberOfFolders = len(fm.getFolderList(directory))
        self.assertEqual(numberOfFolders,len(dirs),"There is no all the folders of the directory in the list {a}".format(a=numberOfFolders))

    def test_extractAllMovies(self):
        cte = Constans()
        fm = FolderManagement()
        directory = cte.FAKE_FILMS_PATH

        numberOfMoviesTotal = len(fm.getAllMoviesInTheDirectory(directory))
        self.assertEqual(numberOfMoviesTotal, 190,"There is no all the movies of the directory in the list {a}".format(a=numberOfMoviesTotal))