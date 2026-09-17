import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter a binary number (up to 8 digits):");
        String input = scan.nextLine();
        scan.close();

        if (input.length() == 0 || input.length() > 8) {
            System.out.println("Error. Your input was either empty, or contained more than 8 digits.");
            return;
        }

        int decimalValue = 0;

        for (int i = 0; input.length() > i; i++) {
            char character = input.charAt(i);

            if (character != '0' && character != '1') {
                System.out.println("Error. Your input contained a character that is not a 1 or 0.");
                return;
            }

            int digit = character - '0';

            decimalValue = (decimalValue * 2) + digit;
        }

        System.out.println(decimalValue);

    }
}
