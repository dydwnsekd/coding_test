import java.util.*;

public class sol_2588 {

	public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        int n1 = in.nextInt();
        String n2 = in.next();
        
        System.out.println(n1 * Character.getNumericValue(n2.charAt(2)));
        System.out.println(n1 * Character.getNumericValue(n2.charAt(1)));
        System.out.println(n1 * Character.getNumericValue(n2.charAt(0)));

        System.out.println(n1*Integer.parseInt(n2));

    }
}
