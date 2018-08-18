"""
Contains exact solution for square plate with dimensions(-0.5, -0.5, 0.5, 0.5)

@author: iryna.tomanova
"""
from edu.tomanova.splines.plate.Apex import Apex
from edu.tomanova.splines.plate.SquarePlate import SquarePlate
from edu.tomanova.splines.exact.tymoshenko.SquareSolver import Solver
from edu.tomanova.splines.utils.ImageHelper import saveSymPyData
from edu.tomanova.splines.utils.DataHelper import saveToFile
from edu.tomanova.splines.utils.DataHelper import saveAsPlainText

plate = SquarePlate(Apex(-0.5, -0.5), Apex(0.5, 0.5))
solver = Solver(plate)
solution = solver.build()
saveToFile(solution, 'square', 'exactSolutionByTymoshenko')
saveAsPlainText(solution, 'square', 'exactSolutionByTymoshenko')
plotData = solver.plot3d()
saveSymPyData(plotData, 'square', 'exactSolutionByTymoshenko')
