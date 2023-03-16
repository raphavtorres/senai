package MathOperators;

import java.util.Locale;
import java.util.Scanner;

public class Ex03 {
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);

        String level = "";
        float imc, weight, height;

        System.out.print("How much do you weight?: ");
        weight = scanner.nextFloat();
        System.out.print("what's your height?: ");
        height = scanner.nextFloat();

        imc = weight / (float)Math.pow(height / 100, 2);

        if (imc > 15 && imc <= 18.5)
            level = "Under weigth.";
        else if (imc > 18.5 && imc <= 24.9)
            level = "Normal weight.";
        else if (imc > 24.9 && imc <= 29.9)
            level = "Overweight.";
        else if (imc > 29.9 && imc <= 39.9)
            level = "Grade I Obesity.";
        else if (imc > 39.9)
            level = "Grade I Obesity.";

        System.out.println("Your IMC is: " + imc + " | " + level);
        scanner.close();
    }
}
