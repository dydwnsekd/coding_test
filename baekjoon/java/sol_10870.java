import java.util.*;

    public class sol_10870 {
    
        public static void main(String[] args) {
    
            Scanner in = new Scanner(System.in);
            int[] Fibonacci = new int[21];
            int n;
            
            Fibonacci[0] = 0;
            Fibonacci[1] = 1;

            for(int i=2; i<21; i++)
                Fibonacci[i]=Fibonacci[i-2]+Fibonacci[i-1];

            n = in.nextInt();

            System.out.println(Fibonacci[n]);
            
        }
    }
    
    