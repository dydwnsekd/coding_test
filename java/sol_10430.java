import java.util.*;

public class sol_10430 {

    public static void main(String[] args) {

        // (A+B)%C, 둘째 줄에 (A%C + B%C)%C, 셋째 줄에 (A×B)%C, 넷째 줄에 (A%C × B%C)%C
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();

        System.out.println((a+b)%c);
        System.out.println((a%c + b%c)%c);
        System.out.println((a*b)%c);
        System.out.println(((a%c) * (b%c))%c);
    }
}