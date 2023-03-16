package MathOperators;

import java.util.Locale;
import java.util.Scanner;

public class Ex04 {
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);

        int num, sqr, cubed;

        System.out.print("Number: ");
        num = scanner.nextInt();

        sqr = (int) Math.pow(num, 2);
        cubed = (int) Math.pow(num, 3);

        System.out.println("Squared: " + sqr);
        System.out.println("Cubed: " + cubed);

        scanner.close();
    }
}
