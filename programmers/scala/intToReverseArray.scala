// https://programmers.co.kr/learn/courses/30/lessons/12932?language=scala
// 자연수 뒤집어 배열로 만들기
object Solution {
    def solution(n: Long): Vector[Int] = {
        return n.toString.reverse.toCharArray.toVector.map(_.asDigit)
    }
}