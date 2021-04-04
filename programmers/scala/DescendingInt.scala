// 정수 내림차순으로 배치하기
// https://programmers.co.kr/learn/courses/30/lessons/12933?language=scala

object Solution {
    def solution(n: Long): Long = {
        return n.toString.sorted.reverse.toLong
        // 내림차순으로 정렬하기 위한 다른 방법
        // return n.toString.sorted(_>_).toLong
    }
}