import scala.collection.mutable.ListBuffer

object Solution {
    def solution(n: Int, lost: Vector[Int], reserve: Vector[Int]): Int = {
    
        var temp_list:ListBuffer[Int] = ListBuffer()

        for (i <- reserve) {
          if (lost.contains(i)) {
            temp_list = temp_list += lost(i)
            lost.filterNot(_ == i)
            println(lost)
          }
        }
        for (i <- temp_list)
          reserve.filter(_ == i)
        for (i <- reserve) {
          if (reserve.contains(i-1))
            lost.filterNot(_ == i-1)
          else if (reserve.contains(i+1))
            lost.filterNot(_ == i+1)

        }
        print(lost)
        return (n-lost.length)
    }
}