import java.util.*;

public class sol_10871 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int x = in.nextInt();
        int temp = 0;
		
		for(int i=0; i<n; i++)
		{
            temp = in.nextInt();
            if(x > temp)
                System.out.printf("%d ", temp);
        }
    }
}
