import java.util.Scanner;

public class Media {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int i = 1;
        float sum_notes = 0;
        float average = 0;
        int number_notes;

        while (true) {
            System.out.println("How many notes you want to insert?: ");
            number_notes = scanner.nextInt();

            if (number_notes > 25)
                System.out.println("Invalid Value, please insert a valid number of notes!\n");
            else
                break;
        }


        while (i <= number_notes) {
            System.out.print("Insert the " + i + "º note: ");
            float current_note = scanner.nextFloat();
            sum_notes += current_note;
            i++;
        }

        average = sum_notes / 3;
        System.out.printf("The average is: %.2f %n", average); // %n jumps to next line

        if (average >= 7)
            System.out.println("Student passed!");
        else if (average >= 5)
            System.out.println("Student needs to go through the council! ");
        else
            System.out.println("Student have failed!");
    }
}