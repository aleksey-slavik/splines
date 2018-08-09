import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from edu.tomanova.splines.utils.DataHelper import loadFromFile
"""
Contains methods for split area and plot triangulation

@author: iryna.tomanova  
"""


class Splitter:
    triangles: list

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
                [self.triangles[i].x1, self.triangles[i].x2, self.triangles[i].x3, self.triangles[i].x1],
                [self.triangles[i].y1, self.triangles[i].y2, self.triangles[i].y3, self.triangles[i].y1],
                'k-')

        plt.show()
        return fig
