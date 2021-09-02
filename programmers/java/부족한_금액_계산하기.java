// https://programmers.co.kr/learn/courses/30/lessons/82612

class Solution {
    public long solution(int price, int money, int count) {
        long answer = -1;
        long need_money = 0;
        
        for(int i=1; i<count+1; i++)
            need_money += i * price;
        
        if(need_money > money)
            return (need_money - money);
        else
            return 0;
    }
}