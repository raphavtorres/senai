package GeometricCalculator.FlatFigures;

public class Hexagon extends FlatFigures{
    double side;
    

    public Hexagon(double side) {
        this.side = side;
    }

    @Override
    public double calcArea() {
        double area_hex = 3 * Math.pow(3, 0.5) * Math.pow(this.side, 2) / 2;
        return area_hex;

    }

    @Override
    public double calcPerimeter() {
        double perimeter = this.side * 6;
        return perimeter;
    }  
}
