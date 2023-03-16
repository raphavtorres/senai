package MathOperators;

import java.util.Locale;
import java.util.Scanner;

public class Ex05 {
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);

        float base, height, area;

        System.out.print("Base of the triangle (centimeter): ");
        base = scanner.nextFloat();
        System.out.print("Height of the triangle (centimeter): ");
        height = scanner.nextFloat();

        area = base * height / 2;

        System.out.println("Area: " + area);
        scanner.close();
    }
}
