import scala.collection.mutable.ListBuffer

object Solution {
    def solution(answers: Vector[Int]): Vector[Int] = {
        
        val p1 = List(1,2,3,4,5)
        val p2 = List(2,1,2,3,2,4,2,5)
        val p3 = List(3,3,1,1,2,2,4,4,5,5)
        
        var result = List(0, 0, 0)
        var count = 0
        
        for (value <- answers)
        {
            if (p1(count%p1.length) == value)
                result = result.updated(0, result(0) + 1)
            if (p2(count%p2.length) == value)
                result = result.updated(1, result(1) + 1)
            if (p3(count%p3.length) == value)
                result = result.updated(2, result(2) + 1)
            
            count += 1;
        }
        
        val max = result.max
        var result_index:ListBuffer[Int] = ListBuffer()

        for (i <- 0 until 3)
        {
          if (result(i) == max)
            result_index = result_index += i+1
        }
        
        return result_index.toVector;
    }
}