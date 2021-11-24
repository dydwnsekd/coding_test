import java.util.Arrays;
import java.util.Scanner;

public class sol_2577 {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int[] num_count = new int[10];
        Arrays.fill(num_count, 0);
        int result=1;

        for(int i=0;i<3;i++)
            result *= in.nextInt();

        for(int i=0;i<Integer.toString(result).length();i++)
            num_count[Integer.toString(result).charAt(i)-'0'] += 1;

        for(int i=0;i<10;i++)
            System.out.println(num_count[i]);
    }
}