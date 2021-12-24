class Solution {
    public int[] solution(long n) {
        
        String str_n = String.valueOf(n);
        int[] answer = new int[str_n.length()];

        for(int i=str_n.length()-1;i>=0;i--)
            answer[str_n.length()-1-i] = str_n.charAt(i)-'0';
        
        return answer;
    }
}