import java.util.Scanner;

public class sol_11047 {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        int money = in.nextInt();
        int count = 0;

        int[] money_list = new int[n];
        for(int i=0;i<n;i++)
            money_list[i] = in.nextInt();

        for(int i=n-1;i>=0;i--){
            count += money / money_list[i];
            money = money % money_list[i];
        }

        System.out.println(count);
    }
}