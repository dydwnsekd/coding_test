import java.util.*;

public class sol_10817 {

	public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int second_max=-99998;
        int max=-99999;
        
        for(int i=0;i<3;i++)
        {
            int temp = in.nextInt();
            if(temp>max)
            {
                second_max = max;
                max = temp;
            }
            else if(temp>second_max)
                second_max = temp;
        }
        System.out.println(second_max);
	}
}
