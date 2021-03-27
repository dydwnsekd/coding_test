// https://programmers.co.kr/learn/courses/30/lessons/12912?language=scala

object Solution {
    def solution(a: Int, b: Int): Long = {
        var result: Long = 0
        
        if (a < b)
            for (i <- a to b)
                result += i
        else
            for (i <- b to a)
                result += i

        return result
    }
}