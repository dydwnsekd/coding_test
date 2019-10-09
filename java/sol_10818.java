import java.util.*;

public class sol_10818 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
        Scanner in = new Scanner(System.in);
        ArrayList<Integer> num_list = new ArrayList<Integer>();

        int num_count = in.nextInt();
        
        for (int i=0;i<num_count;i++)
            num_list.add(in.nextInt());

        Collections.sort(num_list);

        System.out.printf("%d %d", num_list.get(0), num_list.get(num_count-1));

	}

}
