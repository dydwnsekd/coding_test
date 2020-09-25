# Scala 문법 정리
Scala는 기본적으로 immutable로 불변의 객체를 가짐  
List를 mutable로 List를 만들기 위해서는  

scala.collection.mutable에 있는 것들을 import해서 사용
ListBuffer, ArrayBuffer 등이 있음
```scala
import scala.collection.mutable.*
```

List 계열의 특정 index 값에 접근하는 경우 ()사용 python은 []로 헷갈리지 않도록 조심  
immutable로 되어 있는 List의 값 update 방법  
```scala
List = List.updated(index, value)
```
List에 있는 updated method를 이용 index와 변경하고자 하는 값을 넣고 다시 List로 반환받아서 사용해야 함

배열의 길이
```scala
List.length
```

배열 요소 추가 += 연산자 사용
```scala
List = List += a
```

배열 자르기
```scala
List.slice(start_index, end_index)
```

배열 안에 값이 포함되어 있는지 확인 여부
```scala
List.contains(value)
```