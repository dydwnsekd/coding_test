//https://programmers.co.kr/learn/courses/30/lessons/42748?language=java
import java.util.*;

public class programmers_k_num {

	public static void main(String[] args) {

		Scanner in = new Scanner(System.in);
		
        ArrayList<Integer> a = new ArrayList<>();
        
        String arr = in.nextLine();
        arr = arr.substring(1, arr.length()-1);

        for (String ar : arr.split(", "))
            a.add(Integer.parseInt(ar));
        
        arr = in.nextLine();
        arr = arr.substring(1, arr.length()-1);

        for (String ar : arr.split("],"))
        {
            // ar = ar.substring(1);
            System.out.println(ar);
        }
	}

}
