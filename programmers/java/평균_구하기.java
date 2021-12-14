class Solution {
    public double solution(int[] arr) {
        int answer = 0;
        for(int i: arr)
            answer += i;
        return ((double)answer/arr.length);
    }
}