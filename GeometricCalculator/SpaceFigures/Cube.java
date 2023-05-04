package GeometricCalculator.SpaceFigures;

public class Cube extends SpaceFigures{
    double side;
    double base_area;

    public Cube(double side) {
        this.side = side;
        this.base_area = Math.pow(this.side, 2);
    }

    @Override
    public double calcVolume() {
        double volume = this.base_area * this.side;
        return volume;
    }

    @Override
    public double calcSuperficialArea() {
        return this.base_area * 6;
    }
}
