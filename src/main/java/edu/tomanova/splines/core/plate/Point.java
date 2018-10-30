package edu.tomanova.splines.core.plate;

import static javolution.lang.MathLib.pow;
import static javolution.lang.MathLib.sqrt;

public class Point {

    private double x;
    private double y;

    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double distance(Point other) {
        return sqrt(pow(this.x - other.x, 2) + pow(this.y - other.y, 2));
    }

    public double getX() {
        return x;
    }

    public void setX(double x) {
        this.x = x;
    }

    public double getY() {
        return y;
    }

    public void setY(double y) {
        this.y = y;
    }
}
