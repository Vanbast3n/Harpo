import unittest
import os
from main.core.FolderManagement import FolderManagement
from main.common.Constants import Constans
from main.core.IOEngine import IOEngine
from main.db.DBService import DBService

class IOEngin(unittest.TestCase):

    def test_refreshRepositoryDeleting(self):
        io = IOEngine()
        cte = Constans()
        fm = FolderManagement()
        db = DBService()
        repository = 'FAKE'
        table = table = 'FILMS_FAKE'

        io.refreshRepositoryDeleting(repository)
        filmOut = db.checkIfIsIn('RAN',table)
        self.assertEqual(0,filmOut,"The record should'n exist")

    def test_refreshRepositoryAdding(self):
        io = IOEngine()
        cte = Constans()
        fm = FolderManagement()
        repository = 'FAKE'

        io.refreshRepositoryAdding(repository)

