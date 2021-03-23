//https://programmers.co.kr/learn/courses/30/lessons/12901
//2016년

object Solution {
    def solution(a: Int, b: Int): String = {
        val DayOfweek = Array("SUN","MON","TUE","WED","THU","FRI","SAT")
        val DayOfMonth = Array(0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30)
        
        var totalDays = 4
        for (i <- 0 until a) 
            totalDays += DayOfMonth(i)
        
        totalDays += b
        
        return DayOfweek(totalDays % 7)
    }
}