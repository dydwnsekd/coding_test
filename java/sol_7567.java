// https://www.acmicpc.net/problem/7567
import java.util.*;

public class sol_7567 {
    public static void main(String[] args) throws Exception {
        
        Scanner in = new Scanner(System.in);

        String a = in.nextLine();

        int result = 0;
        char pre = ' ';

        for(int i=0; i<a.length(); i++)
        {
            if (i==0)
            {
                result += 10;
                pre = a.charAt(i);
            }
            else
            {
                if (pre == a.charAt(i))
                    result += 5;
                else
                {
                    result += 10;
                    pre = a.charAt(i);
                }
                
            }
        }
        System.out.println(result);

    }
}