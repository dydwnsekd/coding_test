import java.util.*;

public class sol_2562 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int max = -999999999;
        int temp=0;
        int index=0;
        
        for (int i=0;i<9;i++)
        {
            temp = in.nextInt();
            if (temp > max)
            {
                max = temp;
                index = i+1;
            }
        }

        System.out.println(max);
        System.out.println(index);
        
    }
}