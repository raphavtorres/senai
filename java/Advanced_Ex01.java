import java.util.Arrays;
import java.util.Locale;
import java.util.Scanner;

public class Advanced_Ex01 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);

        int size_array, value, pair = 0, odd = 0;

        System.out.print("How many numbers do you wanna add?: ");
        size_array = scanner.nextInt();

        int[] num_array = new int[size_array];
        for(int i = 0; i < size_array; i++){
            System.out.print("Number: ");
            value = scanner.nextInt();
            num_array[i] = value;
            if (num_array[i] % 2 == 0){
                pair++;
            } else {
                odd++;
            }
        }
        int[] pair_array = new int[pair];
        int[] odd_array = new int[odd];

        int pair_index = 0;
        int odd_index = 0;
        for(int i = 0; i < size_array; i++){
            if (num_array[i] % 2 == 0){
                pair_array[pair_index] = num_array[i];
                pair_index++;
            } else {
                odd_array[odd_index] = num_array[i];
                odd_index++;
            }
        }
        System.out.println(Arrays.toString(num_array));
        System.out.println("Pair numbers: " + Arrays.toString(pair_array));
        System.out.println("Odd numbers: " + Arrays.toString(odd_array));
        scanner.close();
    }
}
