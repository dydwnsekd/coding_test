import java.util.Scanner;

public class sol_4344 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m;
        
        for(int i=0; i<n; i++)
        {
            int sum = 0;
            m = in.nextInt();
            for(int j=0;j<m;j++)
            {   
                sum += in.nextInt();
            }
            System.out.printf("%.3f%%\n", (float)sum/m);
        }
    }
}

    