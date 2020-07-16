import java.util.*;

public class sol_4504 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        
        while(true)
        {
            int num = in.nextInt();

            if(num==0)
                break;
            else if(num%n==0)
                System.out.printf("%d is a multiple of %d.\n", num, n);
            else
                System.out.printf("%d is NOT a multiple of %d.\n", num, n);
        }
    }
}

    