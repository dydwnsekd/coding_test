import java.util.Scanner;

public class sol_1712 {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        long A = in.nextLong();
        long B = in.nextLong();
        long C = in.nextLong();

        if (B >= C)
            System.out.println(-1);
        else {
            int count = 0;
            long create_value = A;
            long profit = 0;
            while(true){
                create_value += B;
                profit += C;
                count += 1;
                if(create_value < profit){
                    System.out.println(count);
                    break;
                }

            }
        }
    }
}
