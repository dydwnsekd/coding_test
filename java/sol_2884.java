import java.util.Scanner;

public class sol_2884 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int h = in.nextInt();
        int m = in.nextInt();

        if(m<45)
        {
            if(h==0)
                h=23;
            else
                h--;
            m += 15;
        }
        else
            m -= 45;

        System.out.printf("%d %d", h, m);
    }
}

    