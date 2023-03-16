import java.util.Arrays;
import java.util.Locale;
import java.util.Scanner;

public class Basic_Ex01 {
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);
        int value;
        float average, sum = 0f;

        System.out.print("How many numbers do you wanna add?: ");
        int size_array = scanner.nextInt();
        int[] num_array = new int[size_array];

        for(int i = 0; i < size_array; i++){
            System.out.print((i+1) + "º value: ");
            value = scanner.nextInt();
            num_array[i] = value;
            sum += num_array[i];
        }
        average = (sum / size_array);

        System.out.println(Arrays.toString(num_array));
        System.out.println("Average: " + average);
        scanner.close();
    }
}
