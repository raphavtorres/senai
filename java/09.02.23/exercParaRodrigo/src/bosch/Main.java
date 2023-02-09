package bosch;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("What's your age?: ");
        int age = scanner.nextInt();

        if (age >= 65)
            System.out.println("You're elderly");
        else if (age >= 21)
            System.out.println("You're adult");
        else if (age >= 13)
            System.out.println("You're teenager");
        else if (age >= 3)
            System.out.println("You're child");
        else
            System.out.println("You're a baby");
    }
}
