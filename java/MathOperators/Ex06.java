package MathOperators;

import java.util.Locale;
import java.util.Scanner;

public class Ex06 {
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);

        float a, b, c, delta, x1, x2;

        System.out.println("----BHASKARA----");
        System.out.print("a: ");
        a = scanner.nextFloat();
        System.out.print("b: ");
        b = scanner.nextFloat();
        System.out.print("c: ");
        c = scanner.nextFloat();

        delta = (float) (Math.pow(b, 2) - 4 * a * c);

        x1 = (float) (-b + Math.pow(delta, 1/2)) / 2 * a;
        x2 = (float) (-b - Math.pow(delta, 1/2)) / 2 * a;

        System.out.println("X1 = " + x1);
        System.out.println("X2 = " + x2);
        scanner.close();
    }
}
