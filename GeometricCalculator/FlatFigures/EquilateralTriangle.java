package GeometricCalculator.FlatFigures;

public class EquilateralTriangle extends FlatFigures{
    double side;
    

    public EquilateralTriangle(double side) {
        this.side = side;
    }

    @Override
    public double calcArea() {
        double area_sqr = Math.pow(this.side, 2);
        return area_sqr / 2;

    }

    @Override
    public double calcPerimeter() {
        double perimeter = this.side * 3;
        return perimeter;
    }  
}
