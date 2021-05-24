// 하샤드 수
// https://programmers.co.kr/learn/courses/30/lessons/12947?language=scala

object Solution {
    def solution(x: Int): Boolean = {
        val y = x.toString.foldLeft(0)(_ + _.asDigit)
        if (x % y == 0)
            return true
        else
            return false
    }
}