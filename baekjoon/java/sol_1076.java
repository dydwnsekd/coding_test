import java.util.*;

public class sol_1076 {

    public static void main(String[] args) {

        HashMap<String, Integer> resistance = new HashMap();
        resistance.put("black", 0);
        resistance.put("brown", 1);
        resistance.put("red", 2);
        resistance.put("orange", 3);
        resistance.put("yellow", 4);
        resistance.put("green", 5);
        resistance.put("blue", 6);
        resistance.put("violet", 7);
        resistance.put("grey", 8);
        resistance.put("white", 9);

        HashMap<String, Integer> digit_num = new HashMap();
        digit_num.put("black", 1);
        digit_num.put("brown", 10);
        digit_num.put("red", 100);
        digit_num.put("orange", 1000);
        digit_num.put("yellow", 10000);
        digit_num.put("green", 100000);
        digit_num.put("blue", 1000000);
        digit_num.put("violet", 10000000);
        digit_num.put("grey", 100000000);
        digit_num.put("white", 1000000000);
        
        Scanner in = new Scanner(System.in);
        String n = in.next();
        String m = in.next();
        String digit = in.next();

        long result_value = 0;

        result_value += resistance.get(n) * 10;
        result_value += resistance.get(m);
        result_value = result_value * digit_num.get(digit);

        System.out.println(result_value);
        
    }
}

