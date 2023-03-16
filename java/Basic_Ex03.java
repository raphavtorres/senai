import java.util.Arrays;
import java.util.Locale;
import java.util.Random;
import java.util.Scanner;

public class Basic_Ex03 {
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        System.out.print("How many numbers do you want to insert?: ");
        int size_array = scanner.nextInt();

        int[] first_array = new int[size_array];
        int[] second_array = new int[size_array];
        int value, sum;

        for(int i = 0; i < 2; i++){
            System.out.println("Values of the " + (i+1) + "º array: ");
            for(int j = 0; j < size_array; j++) {
                System.out.println((j + 1) + "º value: ");
                value = scanner.nextInt();
                if (i == 0) {
                    first_array[j] = value;
                } else {
                    second_array[j] = value;
                }
            }
        }

        System.out.println(Arrays.toString(first_array));
        System.out.println(Arrays.toString(second_array));

        for(int i = 0; i < size_array; i++) {
            sum = 0;
            sum = first_array[i] + second_array[i];
            System.out.println("The sum of the " + (i+1)+ "º position of both arrays: " + sum);
        }
    }
}
