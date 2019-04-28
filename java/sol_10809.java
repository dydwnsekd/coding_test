//https://www.acmicpc.net/problem/10809

import java.util.*;

public class sol_10809 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        String str = in.nextLine();

        int[] str_idx = new int[26];

        for(int i=0; i<26; i++)
            str_idx[i] = -1;

        for(int i=0; i<str.length(); i++)
        {
            int alpa_num = (int)str.charAt(i) - 97;
            if(str_idx[alpa_num] == -1)
                str_idx[alpa_num] = i;
        }

        for(int i=0; i<26; i++)
            System.out.print(str_idx[i] + " ");
    }
}

    