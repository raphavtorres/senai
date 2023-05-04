package GeometricCalculator.SpaceFigures;

public class Cylinder extends SpaceFigures {
    double height;
    double radius;
    double area_circle;

    public Cylinder(double height, double radius) {
        this.height = height;
        this.radius = radius;
        this.area_circle = Math.PI * Math.pow(this.radius, 2);
    }

    @Override
    public double calcVolume() {
        return this.area_circle * this.height;
    }

    @Override
    public double calcSuperficialArea() {
        return Math.PI * Math.pow(this.radius, 2) * this.height;
    }
}
