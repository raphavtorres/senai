package GeometricCalculator.SpaceFigures;

public class Sphere extends SpaceFigures {
    double radius;

    public Sphere(double radius) {
        this.radius = radius;
    }

    @Override
    public double calcVolume() {
        double volume = 4/3 * Math.PI * Math.pow(this.radius, 3);
        return volume;
    }

    @Override
    public double calcSuperficialArea() {
        return 4 * Math.PI * Math.pow(this.radius, 2);
    }
    
}
