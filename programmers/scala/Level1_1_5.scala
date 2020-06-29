// https://programmers.co.kr/learn/courses/30/lessons/12903?language=scala

object Solution {
    def solution(s: String): String = {
        if (s.length() % 2 == 0)
            return s.substring((s.length()/2)-1, s.length() / 2 + 1)
        else
            return s.substring((s.length()-1) / 2, (s.length()+1) / 2)
    }
}