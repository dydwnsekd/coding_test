// 자릿수 더하기
// https://programmers.co.kr/learn/courses/30/lessons/12931?language=scala

object Solution {
    def solution(n: Int): Int = {
        var answer = n.toString.foldLeft(0)(_+_.asDigit)
    
        answer
    }
}