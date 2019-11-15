import java.util.*;

public class sol_2439 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		
		for(int i=1; i<=n; i++)
		{
			for(int j=n; j>i; j--)
				System.out.print(" ");
            for(int k=i; k>0; k--)
                System.out.print("*");
			System.out.println();
		}
		
		
	}

}
