import java.util.Scanner;

public class sol_10872 {
    public static int factorial(int n){
        if(n == 1 || n == 0)
            return 1;
        else
            return factorial(n-1) * n;
    }

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        System.out.println(factorial(n));
    }
}