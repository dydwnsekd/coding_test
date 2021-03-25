// https://programmers.co.kr/learn/courses/30/lessons/12910?language=scala
object Solution {
    def solution(arr: Vector[Int], divisor: Int): Vector[Int] = {
        if (arr.filter(_ % divisor == 0).sorted.length == 0)
            return Vector(-1)
        else
            return arr.filter(_ % divisor == 0).sorted
    }
}