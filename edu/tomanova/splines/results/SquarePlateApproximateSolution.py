import sympy

from edu.tomanova.splines.core.rule.SquarePlateRule import SquarePlateRule
from edu.tomanova.splines.core.Solver import Solver
from tomanova.splines.core.plate.Apex import Apex
from tomanova.splines.core.plate.SquarePlate import SquarePlate
from tomanova.splines.core.split import SquareSplitter
#from edu.tomanova.splines.utils.DataHelper import saveToFile
#from edu.tomanova.splines.utils.ImageHelper import savePyPlotData
"""
Contains approximate solution of biharmonic equation for square plate with dimensions (-0.5, -0.5, 0.5, 0.5)

@author: iryna.tomanova
"""

x, y = sympy.symbols(('x', 'y'))
plate = SquarePlate(Apex(-0.5, -0.5), Apex(0.5, 0.5))
splitter = SquareSplitter()
triangles = splitter.splitToTriangles(plate, 0)
#splitPlotData = splitter.plot(size=(10, 10))
#saveToFile(triangles, 'square', 'splitTo4Triangles')
#savePyPlotData(splitPlotData, 'square', 'splitTo4Triangles')
rule = SquarePlateRule(plate, triangles)
rule.setParams()
solver = Solver(rule)
solver.solve()
print(solver.splines[0].subs({x: 0, y: 0}))
print(solver.splines[1].subs({x: 0, y: 0}))
print(solver.splines[2].subs({x: 0, y: 0}))
print(solver.splines[3].subs({x: 0, y: 0}))
