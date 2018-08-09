"""
Contains methods for operation with images

@author: iryna.tomanova
"""


def saveSymPyData(data, directoryName, fileName, imageFormat='png'):
    """
    Save sympy package plot data to file

    Parameters
    ----------
    data: object
        plot data
    directoryName: str
        name of directory
    fileName: str
        name of file
    imageFormat: str
        format of file
    """
    data.save('../resources/' + directoryName + '/' + fileName + '.' + imageFormat)


def savePyPlotData(data, directoryName, fileName, imageFormat='png'):
    """
    Save pyplot package plot data to file

    Parameters
    ----------
    data: object
        plot data
    directoryName: str
        name of directory
    fileName: str
        name of file
    imageFormat: str
        format of file
    """
    data.savefig('../resources/' + directoryName + '/' + fileName + '.' + imageFormat)
