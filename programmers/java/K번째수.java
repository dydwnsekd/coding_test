import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        int arr_num = 0;
        for(int[] a: commands) {
            int[] temp = Arrays.copyOfRange(array, a[0]-1, a[1]);
            Arrays.sort(temp);

            answer[arr_num] = temp[a[2]-1];
            arr_num++;
        }

        return answer;
    }
}