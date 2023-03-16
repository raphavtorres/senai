package MathOperators;

import java.util.Locale;
import java.util.Scanner;

public class Ex02 {
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);

        float celsius, fah;

        System.out.print("Temperature in Celsius: ");
        celsius = scanner.nextFloat();

        fah = 1.8f * celsius + 32;
        System.out.println(celsius + " Celsius: " + fah + " Fahrenheit");
        scanner.close();
    }
}
