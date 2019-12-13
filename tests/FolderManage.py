import unittest
from main.core.FolderManagement import FolderManagement
from main.common.Constants import Constans

class FolderManage(unittest.TestCase):

    def test_getMovieList(self):
        cte = Constans()
        fm = FolderManagement()
        directory = cte.FAKE_FILMS_PATH

        numberOfMovies = len(fm.getMovieList(directory))
        self.assertEqual(numberOfMovies,37,"There is no all the movies of the directory in the list {a}".format(a=numberOfMovies))


    def test_getFolderList(self):
        cte = Constans()
        fm = FolderManagement()
        directory = cte.FAKE_FILMS_PATH

        numberOfFolders = len(fm.getFolderList(directory))
        self.assertEqual(numberOfFolders,15,"There is no all the folders of the directory in the list {a}".format(a=numberOfFolders))
