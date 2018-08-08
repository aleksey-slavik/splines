import pickle
"""
Contains methods for operation with data

@author: iryna.tomanova
"""


def saveToFile(data, directoryName, fileName, fileFormat='dat', mode='wb'):
    """
    Save given data to file

    Parameters
    ----------
    data: object
        given data
    directoryName: str
        name of directory
    fileName: str
        name of file
    fileFormat: str
        format of file
    mode: str
        specifies the mode in which the file is opened
    """
    with open('../resources/' + directoryName + '/' + fileName + '.' + fileFormat, mode) as outFile:
        pickle.dump(data, outFile)


def loadFromFile(directoryName, fileName, fileFormat='dat', mode='rb'):
    """
    Load saved data from file

    Parameters
    ----------
    directoryName: str
        name of directory
    fileName: str
        name of file
    fileFormat: str
        format of file
    mode: str
        specifies the mode in which the file is opened

    Returns
    -------
    data: object
        saved data
    """
    with open('../resources/' + directoryName + '/' + fileName + '.' + fileFormat, mode) as inFile:
        data = pickle.load(inFile)

    return data
