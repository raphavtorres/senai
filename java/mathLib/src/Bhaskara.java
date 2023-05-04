import java.sql.Array;
import java.util.ArrayList;

public class Bhaskara extends MathOperators {
    @Override
    public double sum(double... param) {
        double sum = 0.0;

        for (double num: param) {
            sum += num;
        }
        return sum;
    }
    @Override
    public double subtraction(double x, double y) {
        return x - y;
    }
    @Override
    public double multiplication(double... param) {
        double mult = 1.0;

        for (double num: param) {
            mult *= num;
        }
        return(mult);
    }
    @Override
    public double division(double x, double y) {
        return(x / y);
    }

    public double toSquare(double number) {
        return multiplication(number, number);
    }

    public double calcSqrt(double number) {
        return Math.pow(number, 0.5);
    }
    public double Delta(double a, double b, double c) {
        return subtraction(toSquare(b), multiplication(4, a, c));
    }
    public ArrayList<Double> calcBhaskara(double a, double b, double c){
        double sqrtDelta = calcSqrt(Delta(a, b, c));
        double minor_b = multiplication(-1, b);
        double two_plus_a = multiplication(2, a);

        double x1 = division(sum(minor_b, sqrtDelta), two_plus_a);
        double x2 = division(subtraction(minor_b, sqrtDelta), two_plus_a);

        ArrayList<Double> result = new ArrayList<>();
        result.add(x1);
        result.add(x2);

        return result;
    }
}
