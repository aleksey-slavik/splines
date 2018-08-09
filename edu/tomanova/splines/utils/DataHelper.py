import pickle
"""
Contains methods for load/save operations with data

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


def saveAsPlainText(data, directoryName, fileName, fileFormat='txt', mode='w'):
    """
    Save given data to file as plain text

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
        print(data, file=outFile)


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

    Return
    ------
    data: object
        saved data
    """
    with open('../resources/' + directoryName + '/' + fileName + '.' + fileFormat, mode) as inFile:
        data = pickle.load(inFile)

    return data
