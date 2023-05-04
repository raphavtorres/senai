package GeometricCalculator.SpaceFigures;

public class Cone extends SpaceFigures {
    double base_area;
    double radius;
    double generatrix;
    double side_area;
    double height;

    public Cone(double radius, double generatrix, double height) {  
        this.radius = radius;
        this.generatrix = generatrix;
        this.height = height;
        this.base_area = Math.PI * Math.pow(this.radius, 2);
        this.side_area = Math.PI * this.radius * this.generatrix;
    }

    @Override
    public double calcVolume() {
        return Math.PI * Math.pow(this.radius, 2) * this.height / 3;
    }

    @Override
    public double calcSuperficialArea() {
        return this.base_area + this.side_area;
    }
}
