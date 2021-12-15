import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> answer = new ArrayList<>();
        int size = 0;
        int pre = -1;

        for(int i: arr){
            if(pre != i)
                answer.add(i);
            pre = i;
        }

        int[] answer_arr = new int[answer.size()];
        
        for(int i: answer)
            answer_arr[size++] = i;
        
        return answer_arr;
        
    }
}