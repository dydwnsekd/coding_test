import java.util.*;

public class sol_1157 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        String str = in.nextLine();
        String[] array_str;
        HashMap<String, Integer> result = new HashMap<>();
        String result_key = "";
        int max_num=0;
        str = str.toUpperCase();
        
        array_str = str.split("");

        for(int i=0; i<str.length(); i++)
        {
            if(result.containsKey(array_str[i]))
                result.put(array_str[i], result.get(array_str[i])+1);
            else
                result.put(array_str[i], 1);
        }

        for (String key: result.keySet())
        {
            if(max_num < result.get(key))
            {
                max_num = result.get(key);
                result_key = key;
            }
            else if(max_num == result.get(key))
                result_key = "?";
        }

        System.out.println(result_key);
    }
}
