import java.util.*;

public class sol_10950 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
        Scanner in = new Scanner(System.in);

        int a,b;
        int n = in.nextInt();
        
    
        for(int i=0;i<n;i++)
        {
            a = in.nextInt();
            b = in.nextInt();

            if (a==0 && b==0)
                break;
            else
                System.out.println(a+b);
        }

	}

}
