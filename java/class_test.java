import java.util.*;
import array_split;

public class class_test {

	public static void main(String[] args) {
        
        array_split as = new array_split();

        ArrayList a = as.OneArray("[1, 2]");
        System.out.println(a);

        a = as.TwoArray("[[3, 4], [5, 6]]");
        System.out.println(a);
        
    }
}