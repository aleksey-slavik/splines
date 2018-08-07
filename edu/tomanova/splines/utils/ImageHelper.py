"""
Contains methods for operation with images

@author: iryna.tomanova
"""


def savePlotData(data, directoryName, fileName, imageFormat='png'):
    """
    Save plot data to file

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
