import sympy

from edu.tomanova.splines.core.rule.SquarePlateRule import SquarePlateRule
from edu.tomanova.splines.core.integrate.Integrate import Integrate
from edu.tomanova.splines.core.Spline import Spline
from edu.tomanova.splines.plate.Apex import Apex
from edu.tomanova.splines.plate.SquarePlate import SquarePlate
from edu.tomanova.splines.split.SquareSplitter import SquareSplitter
from edu.tomanova.splines.utils.DataHelper import saveToFile
from edu.tomanova.splines.utils.ImageHelper import savePyPlotData
"""
Contains approximate solution of biharmonic equation for square plate with dimensions (-0.5, -0.5, 0.5, 0.5)

@author: iryna.tomanova
"""


plate = SquarePlate(Apex(-0.5, -0.5), Apex(0.5, 0.5))
splitter = SquareSplitter()
triangles = splitter.splitToTriangles(plate, 0)
#splitPlotData = splitter.plot(size=(10, 10))
#saveToFile(triangles, 'square', 'splitTo4Triangles')
#savePyPlotData(splitPlotData, 'square', 'splitTo4Triangles')
rule = SquarePlateRule(plate, triangles)
rule.setParams()
triangles = rule.triangles
splines = []
integrals = []
for triangle in triangles:
    splineObj = Spline(triangle)
    splineObj.build()
    splines.append(splineObj.spline)
    integral = Integrate(triangles, splineObj.spline).integrate()
    integrals.append(integral)
    print(integral)
