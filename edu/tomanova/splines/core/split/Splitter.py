import matplotlib.pyplot as plt
"""
Contains methods for split area and plot triangulation

@author: iryna.tomanova  
"""


class Splitter:

    def __init__(self):
        self.triangles = []

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
