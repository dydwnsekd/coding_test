object Solution {
    def solution(answers: Vector[Int]): Vector[Int] = {
        
        val p1 = List(1,2,3,4,5)
        val p2 = List(2,1,2,3,2,4,2,5)
        val p3 = List(3,3,1,1,2,2,4,4,5,5)
        
        var result = List(0, 0, 0)
        
        for ((value, index) <- answers.zipWithIndex)
        {
            if (p1(index%p3.length) == value)
                result.patch(0, Seq(result(index%p1.length)+1), 1)
            if (p2(index%p3.length) == value)
                result.patch(1, Seq(result(index%p2.length)+1), 1)
            if (p3(index%p3.length) == value)
                result.patch(2, Seq(result(index%p2.length)+1), 1)
        }
        println (result)
        for ( i <- result)
        {
            print ("AAA")
            println (i)
        }
        return Vector[Int]()
    }
}