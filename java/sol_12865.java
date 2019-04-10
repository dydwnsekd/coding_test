//https://www.acmicpc.net/problem/12865

import java.util.*;

public class sol_12865
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        String input_temp = in.nextLine();
        int item_count = Integer.parseInt(input_temp.split(" ")[0]);
        int weight = Integer.parseInt(input_temp.split(" ")[1]);
        
        String item_info = "";

        ArrayList<ArrayList<Integer>> item_list = new ArrayList<>();
        ArrayList<Integer> temp = new ArrayList<>();
        ArrayList<Integer> result = new ArrayList<>();

        for(int i=0; i<item_count; i++)
        {
            input_temp = in.nextLine();
            int item_weight = Integer.parseInt(input_temp.split(" ")[0]);
            int item_value = Integer.parseInt(input_temp.split(" ")[1]);

            temp.add(item_weight);
            temp.add(item_value);

            item_list.add((ArrayList)temp.clone());
            temp.clear();
        }
    }
}