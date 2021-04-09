// 정수 제곱근 판별
// https://programmers.co.kr/learn/courses/30/lessons/12934?language=scala

import scala.math.sqrt
import scala.math.pow

object Solution {
    def solution(n: Long): Long = {
        if (math.sqrt(n)  == math.sqrt(n).toInt)
            return (pow(sqrt(n)+1,2).toLong)
        else
            return -1
    }
}