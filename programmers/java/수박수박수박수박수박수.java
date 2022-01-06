class Solution {
    public String solution(int n) {
        String answer = "";
        String watermelon = "수박";
        
        for(int i=0;i<n/2;i++)
            answer += watermelon;
        
        if (n%2 == 1)
            return answer + "수";
        else
            return answer;
    }
}