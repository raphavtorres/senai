package GeometricCalculator.FlatFigures;

public class Rectangle extends FlatFigures{
    double small_side;
    double big_side;

    public Rectangle(double small_side, double big_side) {
        this.small_side = small_side;
        this.big_side = big_side;
    }

    @Override
    public double calcArea() {
        double area_rec = this.small_side * this.big_side;
        return area_rec;

    }

    @Override
    public double calcPerimeter() {
        double perimeter = (this.small_side + this.big_side) * 2;
        return perimeter;
    }  
    
}
