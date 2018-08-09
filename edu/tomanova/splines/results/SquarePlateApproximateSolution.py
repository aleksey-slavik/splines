from edu.tomanova.splines.plate.SquarePlate import SquarePlate
from edu.tomanova.splines.split.SquareSplitter import SquareSplitter
from edu.tomanova.splines.utils.DataHelper import saveToFile
from edu.tomanova.splines.utils.ImageHelper import savePyPlotData
"""
Contains approximate solution of biharmonic equation for square plate with dimensions (-0.5, -0.5, 0.5, 0.5)

@author: iryna.tomanova
"""


plate = SquarePlate(-0.5, -0.5, 0.5, 0.5)
splitter = SquareSplitter()
triangles = splitter.splitToTriangles(plate, 0)
splitPlotData = splitter.plot(size=(10, 10))
saveToFile(triangles, 'square', 'splitTo4Triangles')
savePyPlotData(splitPlotData, 'square', 'splitTo4Triangles')
