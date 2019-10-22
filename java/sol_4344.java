import java.util.Scanner;

public class sol_4344 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m;
        
        for(int i=0; i<n; i++)
        {
            int sum = 0;
            int count = 0;

            m = in.nextInt();
            int[] num_list = new int[m];

            for(int j=0;j<m;j++)
            {   
                int temp = in.nextInt();
                sum += temp;
                num_list[j]= temp;
            }
            
            float avg = (float)sum/m;
            
            for(int j=0;j<m;j++)
            {
                if(num_list[j] > avg)
                    count++;
            }
            System.out.printf("%.3f%%\n", (float)count/m * 100);
        }
    }
}

    