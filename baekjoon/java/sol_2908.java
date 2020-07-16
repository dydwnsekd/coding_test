import java.util.Scanner;

public class sol_2908 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        String str_num1 = in.next();
        String str_num2 = in.next();

        int num1 = Integer.parseInt(String.valueOf(str_num1.charAt(2)) + String.valueOf(str_num1.charAt(1)) + String.valueOf(str_num1.charAt(0)));
        int num2 = Integer.parseInt(String.valueOf(str_num2.charAt(2)) + String.valueOf(str_num2.charAt(1)) + String.valueOf(str_num2.charAt(0)));

        if(num1 > num2)
            System.out.println(num1);
        else
            System.out.println(num2);
    }
}

    