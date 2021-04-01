// 약수의 합
// https://programmers.co.kr/learn/courses/30/lessons/12928?language=scala

object Solution {
    def solution(n: Int): Int = {
        return (1 to n).filter(n % _ == 0).foldLeft(0) (_ + _)
    }
}