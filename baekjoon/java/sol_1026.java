import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class sol_1026 {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int n = in.nextInt();

        ArrayList<Integer> a = new ArrayList<>();
        ArrayList<Integer> b = new ArrayList<>();

        int result = 0;

        for(int i=0;i<n;i++)
            a.add(in.nextInt());
        for(int i=0;i<n;i++)
            b.add(in.nextInt());

        Collections.sort(a);
        Collections.sort(b);
        Collections.reverse(b);

        for(int i=0;i<n;i++)
            result += a.get(i) * b.get(i);

        System.out.println(result);
    }
}