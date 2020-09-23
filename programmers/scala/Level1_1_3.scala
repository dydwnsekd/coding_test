import scala.collection.mutable.ListBuffer

object Solution {
    def solution(n: Int, lost: Vector[Int], reserve: Vector[Int]): Int = {
        var temp_list = ListBuffer()
    
        for (i <- lost){
            if (lost.contains(i)) {
            temp_list = temp_list += lost.(i)
            lost -= (i)
            }
        }
        for (i <- temp_list)
            reverve.remove(i)
        for (i <- reserve) {
            if (reserve.contains(i-1)
                lost.remove(i-1)
            else if (reserve.contains(i+1))
                lost.remove(i+1)
                
        }
        return (n-lost.length)
    }
}