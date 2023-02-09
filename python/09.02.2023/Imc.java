import java.util.Scanner;
import java.lang.Math;

public class Imc {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        float weight, height, imc;

        System.out.println("Write your weight: ");
        weight = scanner.nextFloat();
        System.out.println("Write your height: ");
        height = scanner.nextFloat();

        imc = (float) (weight / Math.pow(height, 2));

        System.out.println("Seu IMC é: " + imc);
        if (imc < 16.9)
            System.out.println("Muito abaixo do peso");
        else if (imc >= 16.9 && imc < 18.5)
            System.out.println("Abaixo do peso");
        else if (imc > 18.5 && imc < 25)
            System.out.println("Peso Normal");
        else if (imc >= 25 && imc < 30)
            System.out.println("Acima do peso");
        else if (imc >= 30 && imc < 35)
            System.out.println("Obesidade grau I");
        else if (imc >= 35 && imc <= 40)
            System.out.println("Obesidade grau II");
        else
            System.out.println("Obesidade grau III (mórbida)");
    }
}
