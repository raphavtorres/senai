package GeometricCalculator.FlatFigures;

public class Circle extends FlatFigures {
    double diameter;
    double radius;
    

    public Circle(double diameter) {
        this.diameter = diameter;
        this.radius = diameter/2;
    }

    @Override
    public double calcArea() {
        double area_circle = Math.PI * Math.pow(this.radius, 2);
        return area_circle;

    }

    @Override
    public double calcPerimeter() {
        double circumference = this.diameter * Math.PI;
        return circumference;
    }  
}
