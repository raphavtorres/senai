import java.util.*;

public class FindTheTreasure {
    static String[][] matrix = new String[5][5];
    static void showMatrix(){
        for(int i = 0; i < 5; i++){
            System.out.println(Arrays.toString(matrix[i]));
        }
    }
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        System.out.println("______FIND THE TREASURE______");
        System.out.println("You have 3 attempts");

        for(int row = 0; row < 5; row++){
            for(int column = 0; column < 5; column++) {
                matrix[row][column] = "_";
            }
        }

        int row_random = random.nextInt(5);
        int column_random = random.nextInt(5);

        int count = 0;
        while(count < 3){
            int row_input = 0;
            int column_input = 0;
            // PRINT THE MATRIX
            showMatrix();

            // GETTING USER'S ATTEMPT
            System.out.println((count + 1) + "ª chance!");

            try{
                System.out.print("Choose row: ");
                row_input = scanner.nextInt() - 1;
                System.out.print("Choose column: ");
                column_input = scanner.nextInt() - 1;
            }catch (InputMismatchException e) {
                System.out.println("Invalid Value!");
                break;
            }

            matrix[row_input][column_input] = "X";

            // WINNING AND LOOSING
            if(row_input == row_random && column_input == column_random){
                System.out.println("YOU WON!");
                break;
            } else if(count == 2){
                System.out.println("YOU LOST!");
                matrix[row_random][column_random] = "*";
                showMatrix();
                System.out.print("The answer was row: " + (row_random + 1) + " | column: " + (column_random + 1));
                break;
            }
            count++;
        }
        scanner.close();
    }
}
