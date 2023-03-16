import java.util.Arrays;
import java.util.Locale;
import java.util.Random;
import java.util.Scanner;

public class Basic_Ex02 {
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        System.out.print("How many random numbers do you want?: ");
        int size_array = scanner.nextInt();

        int[] num_array = new int[size_array];
        int bigger = 0;

        for(int i = 0; i < size_array; i++){
            num_array[i] = random.nextInt(101) + 1;
            if (bigger < num_array[i]){
                bigger = num_array[i];
            }
        }
        System.out.println(Arrays.toString(num_array));
        System.out.println("Biggest value: " + bigger);
        scanner.close();
    }
}
