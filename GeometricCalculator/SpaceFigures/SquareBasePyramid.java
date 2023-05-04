package GeometricCalculator.SpaceFigures;

public class SquareBasePyramid extends SpaceFigures {
    double height;
    double side;
    double perimeter;
    double base_area;

    public SquareBasePyramid(double height, double side) {
        this.height = height;
        this.side = side;
        this.perimeter = this.side * 6;
        this.base_area = 3 * Math.pow(3, 0.5) * Math.pow(this.side, 2) / 2;
    }

    @Override
    public double calcVolume() {
        double volume = 1/3 * Math.pow(this.side, 2) * this.height;
        return volume;
    }

    @Override
    public double calcSuperficialArea() {
        return this.perimeter * this.height / 2 + this.base_area;
    }
}
