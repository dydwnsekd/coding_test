class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        
        int sum = 0;
        String str_x = String.valueOf(x);

        for(int i=0;i<str_x.length();i++)
            sum += str_x.charAt(i)-'0';

        if (x%sum!=0)
            answer = false;
        
        return answer;
    }
}