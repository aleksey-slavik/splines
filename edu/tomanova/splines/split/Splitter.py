import matplotlib.pyplot as plt
from edu.tomanova.splines.utils.DataHelper import loadFromFile
"""
Contains methods for split area and plot triangulation

@author: iryna.tomanova  
"""


class Splitter:

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

    def plot(self, size=(12, 9)):
        """
        Plot triangulation
        Important! Need to create list of triangles before call this method

        Parameters
        ----------
        size: tuple
            plot dimensions

        Return
        ------
        fig: object
            plot data
        """
        fig = plt.figure(figsize=size)

        for i in range(len(self.triangles)):
            plt.plot(
                [self.triangles[i].apex1.x, self.triangles[i].apex2.x, self.triangles[i].apex3.x, self.triangles[i].apex1.x],
                [self.triangles[i].apex1.y, self.triangles[i].apex2.y, self.triangles[i].apex3.y, self.triangles[i].apex1.y],
                'k-')

        plt.show()
        return fig
