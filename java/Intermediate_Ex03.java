import java.util.Arrays;
import java.util.Locale;
import java.util.Scanner;

public class Intermediate_Ex03 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);

        int size_array, value, nozero_amount = 0;

        System.out.print("How many numbers do you wanna add?: ");
        size_array = scanner.nextInt();

        int[] num_array = new int[size_array];
        for(int i = 0; i < size_array; i++){
            System.out.print("Number: ");
            value = scanner.nextInt();
            num_array[i] = value;
            if (value != 0) {
                nozero_amount++;
            }
        }
        int[] nozero_array = new int[nozero_amount];
        int c = 0;
        for(int i = 0; i < size_array; i++){
            if (num_array[i] != 0) {
                nozero_array[c] = num_array[i];
                c++;
            }
        }
        System.out.println(Arrays.toString(num_array));
        System.out.println(Arrays.toString(nozero_array));
    }
}
