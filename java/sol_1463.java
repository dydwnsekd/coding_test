import java.util.*;

public class sol_1463 {

	public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        int n = in.nextInt();
        int count = 0;
        
        while(n!=1)
        {
            if(n%3==0)
                n /= 3;
            else if(n%2==0)
                n /= 2;
            else
                n -= 1;
            
            System.out.println(n);
            count++;
        }

        System.out.println(count);

	}

}
