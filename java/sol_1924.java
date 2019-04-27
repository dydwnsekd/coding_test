import java.util.*;

public class sol_1924 {

    public static void main(String[] args) {
    
        Scanner in = new Scanner(System.in);
        int[] month_day = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30};
        int month = in.nextInt();
        int day = in.nextInt();

        int result = 0;

        for(int i=0;i<month;i++)
            result += month_day[i];

        result += day;

        result %= 7;

        if(result==1) System.out.println("MON");
        else if(result==2) System.out.println("TUE");
        else if(result==3) System.out.println("WED");
        else if(result==4) System.out.println("THU");
        else if(result==5) System.out.println("FRI");
        else if(result==6) System.out.println("SAT");
        else if(result==0) System.out.println("SUN");
    }
}
