//https://programmers.co.kr/learn/courses/30/lessons/12969?language=scala

import scala.io.StdIn.readLine

object Solution {
    def main(args: Array[String]) {
        val n = readLine().split(" ")
        val (a, b) = (n(0).toInt, n(1).toInt)
        for ( i <- 0 until b)
        {
            for ( j <- 0 until  a)
            {
                print("*")    
            }
            println()
        }
    }   
}