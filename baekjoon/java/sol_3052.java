import java.util.HashSet;
import java.util.Scanner;

public class sol_3052 {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        HashSet<Integer> mod_set = new HashSet<>();

        for(int i=0;i<10;i++)
            mod_set.add(in.nextInt() % 42);

        System.out.println(mod_set.size());
    }
}
