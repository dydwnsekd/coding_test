import java.util.Scanner;

public class sol_1085 {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int x = in.nextInt();
        int y = in.nextInt();
        int w = in.nextInt();
        int h = in.nextInt();

        int x_min_value = Integer.MAX_VALUE;
        int y_min_value = Integer.MAX_VALUE;

        if(x > Math.abs(x-w))
            x_min_value = Math.abs(x-w);
        else
            x_min_value = x;

        if(y > Math.abs(y-h))
            y_min_value = Math.abs(y-h);
        else
            y_min_value = y;

        System.out.println(Math.min(x_min_value, y_min_value));
    }
}