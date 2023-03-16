import java.util.Arrays;
import java.util.Locale;
import java.util.Scanner;

public class Intermediate_Ex01 {
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);

        System.out.print("How many numbers do you wanna add?: ");
        int size_array = scanner.nextInt();
        int[] num_array = new int[size_array];
        int value;
        for(int i = 0; i < size_array; i++){
            System.out.print("Number: ");
            value = scanner.nextInt();
            num_array[i] = value;
        }

        for(int b = 1; b < size_array; b++){
            for(int m = 0; m < size_array; m++){
                if (num_array[m] > num_array[b]){
                    int temp = num_array[m];
                    num_array[m] = num_array[b];
                    num_array[b] = temp;
                }
            }
        }
        System.out.println(Arrays.toString(num_array));

        scanner.close();
    }
}
