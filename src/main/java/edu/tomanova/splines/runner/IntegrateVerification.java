package edu.tomanova.splines.runner;

import edu.tomanova.splines.core.integrate.Integrate;
import edu.tomanova.splines.core.plate.Point;
import edu.tomanova.splines.core.plate.Triangle;
import org.jscience.mathematics.function.Polynomial;
import org.jscience.mathematics.function.Variable;
import org.jscience.mathematics.number.Float64;

public class IntegrateVerification {

    public static void main(String[] args) {

        Triangle triangle = new Triangle(new Point(0, 0), new Point(1, 0), new Point(0, 1));

        Variable<Float64> varX = new Variable.Global<Float64>("x");
        Variable<Float64> varY = new Variable.Global<Float64>("y");
        Polynomial<Float64> x = Polynomial.valueOf(Float64.ONE, varX);
        Polynomial<Float64> y = Polynomial.valueOf(Float64.ONE, varY);
        Polynomial<Float64> integrand = x.plus(y);

        Integrate integrate = new Integrate(triangle, integrand);
        System.out.println(integrate.integrate().doubleValue());
    }
}
