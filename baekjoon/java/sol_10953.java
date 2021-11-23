import java.util.Scanner;

public class sol_10953 {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        in.nextLine();
        for(int i=0;i<n;i++) {
            String s = in.nextLine();
            System.out.println(Integer.parseInt(s.split(",")[0]) + Integer.parseInt(s.split(",")[1]));
        }
    }
}