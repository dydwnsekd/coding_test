// https://programmers.co.kr/learn/courses/30/lessons/12918?language=scala
object Solution {
    def solution(s: String): Boolean = {
        if (s.forall(_.isDigit) && (s.length == 4 || s.length == 6))
          return true
        else
          return false
    }
}