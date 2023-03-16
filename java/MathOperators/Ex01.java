package MathOperators;

import java.util.Locale;
import java.util.Scanner;

public class Ex01 {
    // leia fare conv celcius
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);

        float celcius, fah;

        System.out.print("Temperature in Fahrenheit: ");
        fah = scanner.nextFloat();

        celcius = (fah - 32) / 1.8f;
        System.out.println(fah + " Fahrenheit: " + celcius + " Celsius");
        scanner.close();
    }

}
