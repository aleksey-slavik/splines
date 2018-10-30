from tomanova.splines.core.split.Splitter import Splitter
from edu.tomanova.splines.utils.DataHelper import loadFromFile


class DefaultSplitter(Splitter):

    def __init__(self):
        super().__init__()

    def fromFile(self, directoryName, fileName):
        """
        Get triangulation saved in file
        File must consist list of Triangle objects

        Parameters
        ----------
        directoryName: str
            directory name
        fileName: str
            file name

        Return
        ------
        triangles: list
            list of triangles
        """
        self.triangles = loadFromFile(directoryName, fileName)
        return self.triangles