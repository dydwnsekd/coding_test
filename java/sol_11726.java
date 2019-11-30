import java.util.*;

    public class sol_11726 {
    
        public static void main(String[] args) {
    
            Scanner in = new Scanner(System.in);
            int[] Fibonacci = new int[1001];
            int n;
            
            Fibonacci[0] = 1;
            Fibonacci[1] = 1;

            for(int i=2; i<1001; i++)
            {
                Fibonacci[i]=Fibonacci[i-2]+Fibonacci[i-1];
                Fibonacci[i] = Fibonacci[i] % 10007;
            }

            n = in.nextInt();

            System.out.println(Fibonacci[n]);
            
        }
    }
    
    