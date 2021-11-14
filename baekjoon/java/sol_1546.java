import java.util.Scanner;
import static java.lang.Math.round;

public class sol_1546 {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int t = in.nextInt();

        double[] score = new double[t];
        double max = -999;
        double total_score = 0;

        for(int i=0;i<t;i++) {
            double temp = in.nextDouble();
            score[i] = temp;
            if(max < temp)
                max = temp;
        }

        for(int i=0;i<t;i++)
            total_score += round(((score[i]/max) * 10000) / 100);

        System.out.println(total_score/t);

    }
}