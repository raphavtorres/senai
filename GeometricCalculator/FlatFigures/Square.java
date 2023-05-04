package GeometricCalculator.FlatFigures;

public class Square extends FlatFigures{
    double side;

    public Square(double side) {
        this.side = side;
    }

    @Override
    public double calcArea() {
        double area_sqr = Math.pow(this.side, 2);
        return area_sqr;
    }

    @Override
    public double calcPerimeter() {
        double perimeter = this.side * 4;
        return perimeter;
    }
    
}
