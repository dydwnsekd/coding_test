//https://www.acmicpc.net/problem/5567

import java.util.*;

public class sol_5567 {

    public static void main(String[] args) throws Exception {
        
        Scanner in = new Scanner(System.in);

        in.nextInt();
        int releation = in.nextInt();
        in.nextLine();

        ArrayList<Integer> result = new ArrayList<>();
        HashMap<Integer, ArrayList<Integer>> friend = new HashMap<>();
        ArrayList<Integer> temp = new ArrayList<>();

        for(int i=0; i<releation; i++)
        {
            String input = in.nextLine();
            int a = Integer.parseInt(input.split(" ")[0]);
            int b = Integer.parseInt(input.split(" ")[1]);

            if(a==1)
                result.add(b);
            else if(friend.containsKey(a))
                friend.get(a).add(b);
            else
            {
                temp.add(b);
                friend.put(a,(ArrayList)temp.clone());
                temp.clear();
            }
        }

        ArrayList<Integer> t = new ArrayList<>();
        t = (ArrayList)result.clone();

        for(int i=0; i<result.size(); i++)
        {
            if(friend.containsKey(result.get(i)))
            {
                t.addAll(friend.get(result.get(i)));
            }
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