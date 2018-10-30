package edu.tomanova.splines.core.integrate;

import edu.tomanova.splines.core.plate.Point;
import edu.tomanova.splines.core.plate.Triangle;
import org.jscience.mathematics.function.Polynomial;
import org.jscience.mathematics.number.Float64;

import java.util.ArrayList;
import java.util.List;

public class Integrate {

    private List<Triangle> grid;
    private Polynomial<Float64> integrand;
    private int divideCount;

    public Integrate(Triangle triangle, Polynomial<Float64> integrand) {
        this(triangle, integrand, 3);
    }

    public Integrate(Triangle triangle, Polynomial<Float64> integrand, int divideCount) {
        this.integrand = integrand;
        this.divideCount = divideCount;
        this.grid = new ArrayList<Triangle>();
        grid.add(triangle);
    }

    public Float64 integrate() {
        Float64 integral = Float64.valueOf(0);
        divideArea();

        for (Triangle triangle : grid) {
            Float64 p1 = substring(triangle.getNorm12());
            Float64 p2 = substring(triangle.getNorm23());
            Float64 p3 = substring(triangle.getNorm13());

            integral.plus((p1.plus(p2).plus(p3)).times(triangle.square()).divide(3));
        }

        return integral;
    }

    private Float64 substring(Point point) {
        return integrand.evaluate(Float64.valueOf(point.getX()), Float64.valueOf(point.getY()));
    }

    private void divideArea() {

        for (int i = 0; i < divideCount; i++) {
            List<Triangle> intermediates = new ArrayList<Triangle>();

            for (Triangle triangle : grid) {
                intermediates.add(new Triangle(
                        triangle.getApex1(),
                        triangle.getNorm12(),
                        triangle.getNorm13()));
                intermediates.add(new Triangle(
                        triangle.getNorm12(),
                        triangle.getNorm13(),
                        triangle.getNorm23()));
                intermediates.add(new Triangle(
                        triangle.getNorm12(),
                        triangle.getApex2(),
                        triangle.getNorm23()));
                intermediates.add(new Triangle(
                        triangle.getNorm23(),
                        triangle.getNorm13(),
                        triangle.getApex3()));
            }

            grid = intermediates;
        }
    }
}
