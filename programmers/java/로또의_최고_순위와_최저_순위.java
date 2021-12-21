import java.util.Arrays;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];

        int zero_count = 0;
        int correct_count = 0;

        for(int i: lottos) {
            if(Arrays.stream(win_nums).anyMatch(n -> n==i))
                correct_count++;
            else if(i == 0)
                zero_count++;
        }

        if(correct_count + zero_count > 1)
            answer[0] = (7-(correct_count+zero_count));
        else
            answer[0] = 6;

        if (correct_count > 1)
            answer[1] = 7-correct_count;
        else
            answer[1] = 6;
        
        return answer;
    }
}