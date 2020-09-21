// https://programmers.co.kr/learn/courses/30/lessons/42748?language=scala
// K번쨰 수

import scala.collection.mutable.ListBuffer

object Solution {
    def solution(array: Vector[Int], commands: Vector[Vector[Int]]): Vector[Int] = {
        
        var result_index:ListBuffer[Int] = ListBuffer()
        
        for (cmd <- commands)
          result_index = result_index += (array.slice(cmd(0)-1, cmd(1)).sortWith(_<_)(cmd(2)-1))
        
        return result_index.toVector
        
    }
}