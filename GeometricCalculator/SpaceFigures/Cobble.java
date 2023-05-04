package GeometricCalculator.SpaceFigures;

public class Cobble extends SpaceFigures{
    double small_side;
    double big_side;
    double height;
    double base_area;
    
    public Cobble(double small_side, double big_side, double height) {
        this.small_side = small_side;
        this.big_side = big_side;
        this.height = height;
        this.base_area = this.small_side * this.big_side;
    }

    @Override
    public double calcVolume() {
        double volume = this.base_area * this.height;
        return volume;
    }

    @Override
    public double calcSuperficialArea() {
        double result = 2 * (this.height * this.big_side + this.height * this.small_side);
        return result;
    }
}
