package GeometricCalculator;

import java.util.Scanner;

public class Main {
    public static void main (String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("[0] Exit\n[1] Flat Figure\n[2] Space Figure");
        int choice = scanner.nextInt();

        switch (choice) {
            case 0:
                // Exit
                break;
            case 1:
                // Flat
                break;
            case 2:
                // Space
                break;
            default:
                break;
        }
        
        scanner.close();
    }
}
