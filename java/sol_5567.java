//https://www.acmicpc.net/problem/5567
import java.util.*;

public class sol_5567 {

    public static void main(String[] args) throws Exception {
        
        Scanner in = new Scanner(System.in);

        int person_count = in.nextInt();
        int releation = in.nextInt();
        in.nextLine();

        ArrayList<Integer> result = new ArrayList<>();
        HashMap<Integer, ArrayList<Integer>> friend = new HashMap<>();
        ArrayList<Integer> temp = new ArrayList<>();

        for (int i=0; i<person_count; i++)
            friend.put(i+1,(ArrayList)temp.clone());

        for(int i=0; i<releation; i++)
        {
            String input = in.nextLine();
            int a = Integer.parseInt(input.split(" ")[0]);
            int b = Integer.parseInt(input.split(" ")[1]);

            if(a==1)
                result.add(b);
            else
            {
                friend.get(a).add(b);
                friend.get(b).add(a);
            }
        }

        ArrayList<Integer> t = new ArrayList<>();
        t = (ArrayList)result.clone();

        for(int i=0; i<result.size(); i++)
        {
            t.addAll(friend.get(result.get(i)));
        }

        ArrayList<Integer> r = new ArrayList<>();
        for(int i=0; i<t.size(); i++)
        {
            if(!r.contains(t.get(i)))
                r.add(t.get(i));
        }

        System.out.println(r.size());
    }
}