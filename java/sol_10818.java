import java.util.*;

public class sol_10818 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
        Scanner in = new Scanner(System.in);
        
        int num_count = in.nextInt();
        int max=-9999999;
        int min=9999999;
        int temp;
        
        for (int i=0;i<num_count;i++)
        {
            temp = in.nextInt();
            if(temp>max)
                max = temp;
            if(temp<min)
                min = temp;
        }

        System.out.printf("%d %d", min, max);

	}

}
