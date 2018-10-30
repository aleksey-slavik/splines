package edu.tomanova.splines.core.plate;

import static javolution.lang.MathLib.sqrt;

public class Triangle {

    private Point apex1;
    private Point apex2;
    private Point apex3;
    private Point norm12;
    private Point norm23;
    private Point norm13;

    public Triangle (Point apex1, Point apex2, Point apex3) {
        this.apex1 = apex1;
        this.apex2 = apex2;
        this.apex3 = apex3;
        this.norm12 = new Point((apex1.getX() + apex2.getX()) / 2, (apex1.getY() + apex2.getY()) / 2);
        this.norm23 = new Point((apex2.getX() + apex3.getX()) / 2, (apex2.getY() + apex3.getY()) / 2);
        this.norm13 = new Point((apex1.getX() + apex3.getX()) / 2, (apex1.getY() + apex3.getY()) / 2);
    }

    public double square() {
        double a = apex1.distance(apex2);
        double b = apex2.distance(apex3);
        double c = apex1.distance(apex3);
        double p = (a + b + c) / 2;

        return sqrt(p * (p - a) * (p - b) * (p - c));
    }

    public Point getApex1() {
        return apex1;
    }

    public Point getApex2() {
        return apex2;
    }

    public Point getApex3() {
        return apex3;
    }

    public Point getNorm12() {
        return norm12;
    }

    public Point getNorm23() {
        return norm23;
    }

    public Point getNorm13() {
        return norm13;
    }
}
