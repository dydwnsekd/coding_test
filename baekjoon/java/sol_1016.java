import java.util.Scanner;

public class sol_1016 {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int min = in.nextInt();
        int max = in.nextInt();

        int n = (int) Math.floor(Math.sqrt(max)) - (int) Math.ceil(Math.sqrt(min));
        int m = max - min;

        System.out.println(m-n);

    }
}