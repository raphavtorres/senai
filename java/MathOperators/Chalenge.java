package MathOperators;

public class Chalenge {
    public static void main(String[] args){
        double p1, p2, p3, last;

        p1 = 3 * Math.pow((-3.0 / 4), -2);
        p2 = 6 * (Math.pow(3, -1) / 4);
        p3 = 7 * Math.pow((-3.0 / 4), -1) + 2;
        last = Math.pow((p1 + p2 - 4) / p3, -1) + 4;
        System.out.println(last);
    }
}
