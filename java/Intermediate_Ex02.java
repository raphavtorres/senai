import java.util.Arrays;
import java.util.Locale;
import java.util.Random;
import java.util.Scanner;

public class Intermediate_Ex02 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);

        System.out.print("How many numbers do you wanna add?: ");
        int size_array = scanner.nextInt();

        int[] num_array = new int[size_array];
        int[] inverse_array = new int[size_array];

        int c = size_array - 1;
        for(int i = 0; i < size_array; i++){
            num_array[i] = random.nextInt(101);
            inverse_array[c] = num_array[i];
            c--;
        }

        System.out.println(Arrays.toString(num_array));
        System.out.println(Arrays.toString(inverse_array));
        scanner.close();
    }
}
