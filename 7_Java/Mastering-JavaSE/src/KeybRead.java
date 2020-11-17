import java.util.Scanner;

public class KeybRead {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
//        int a, b, c;
//        System.out.println("Enter two numbers: ");
//        a = scanner.nextInt();
//        b = scanner.nextInt();
//        c = a + b;
//        System.out.println("Sum is " + c);

        String name;
        System.out.println("What's your name?");
        name = scanner.nextLine();
        System.out.println("Welcome Mr/Ms " + name);
    }
}
