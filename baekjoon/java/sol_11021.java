import java.util.*;

    public class sol_11021 {
    
        public static void main(String[] args) {
    
            Scanner in = new Scanner(System.in);
            int n = in.nextInt();
            
            for(int i=0;i<n;i++)
            {
                int num1 = in.nextInt();
                int num2 = in.nextInt();

                System.out.printf("Case #%d: %d\n", i+1, num1+num2);
            }
            
        }
    }
    
    