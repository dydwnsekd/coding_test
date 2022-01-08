import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        
        int max_x = Integer.MIN_VALUE;
        int max_y = Integer.MIN_VALUE;

        for (int[] i: sizes){
            Arrays.sort(i);
            if (i[0] > max_x)
                max_x = i[0];
            if (i[1] > max_y)
                max_y = i[1];
        }

        return max_x * max_y;
    }
}
