import java.lang.Math;
import java.text.NumberFormat;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        // Declaring scanner for reading user input
        Scanner scanner = new Scanner(System.in);

        //Creating variables
        int principal;
        float monthly_interest_rate = 0, num_payments_months = 0;

        // Interaction with user
        while (true) {
            System.out.print("Principal: ($1K - $1M)");
            principal = scanner.nextInt();

            if (principal < 1_000 || principal > 1_000_000)
                System.out.println("Enter a value between $1K and $1M.");
            else
                break;

        }

        while (true) {
            System.out.print("Annual Interest Rate: ");
            float annual_interest_rate = scanner.nextFloat();

            if (annual_interest_rate <= 0 || annual_interest_rate > 30)
                System.out.println("Enter a value greater than 0  and less than or equal to 30.");
            else
                monthly_interest_rate = ((annual_interest_rate / 100) / 12);
                break;
        }

        while (true){
            System.out.print("Period (Years): ");
            float num_payments_years = scanner.nextFloat();

            if (num_payments_years < 1 || num_payments_years > 30)
                System.out.println("Enter a value between 1 and 30.");
            else
                num_payments_months = num_payments_years * 12;
                break;
        }

        // Calculation
        float firstPart = (float) (principal * (monthly_interest_rate * Math.pow((1 + monthly_interest_rate), num_payments_months)));
        float secondPart = (float) (Math.pow((1 + monthly_interest_rate), num_payments_months)) - 1;
        double mortgage = firstPart / secondPart;

        String mortgageFormated = NumberFormat.getCurrencyInstance().format(mortgage);
        System.out.print("Mortgage: " + mortgageFormated);
    }
}
