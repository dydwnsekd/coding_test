import java.util.*;

    public class sol_17362 {
    
        public static void main(String[] args) {
    
            Scanner in = new Scanner(System.in);
            int n = in.nextInt();

            n = n%8;
            if (n == 1)
                System.out.println(1);
            else if (n == 5)
                System.out.println(5);
            else if (n == 2 || n == 0)
                System.out.println(2);
            else if (n == 3 || n == 7)
                System.out.println(3);
            else
                System.out.println(4);
            
        }
    }