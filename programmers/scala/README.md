# Scala 문법 정리
https://twitter.github.io/scala_school/ko/index.html 참고

## val과 var
scala에서는 변수를 선언할 때 val과 var 둘 중 하나를 지정해 선언  
val은 불변값으로 아래에 나올 immutable와 연결되며 한번 선언된 값을 변경할 수 없다  
var은 가변값으로 값과 이름의 관계를 변경하기 위해서는 var을 이용해 선언

## 함수
scala에서 함수를 만들때는 def 키워드를 사용하며  
return 이 없는 경우 맨 마지막 줄에 있는 값이 자동으로 return 된다
```scala
// 1을 더하는 함수
def addOne(m: Int): Int = m + 1

// 사용
val three = addOne(2)
```

### 인자의 일부만 사용해 호출(부분 적용, Partial application)
함수 호출시 밑줄(_)을 사용해 일부만 적용 가능  
_ 은 문맥에 따라 다르며 아래와 같이 사용
```scala
def adder(m: Int, n: Int) = m + n
//add2라는 새로운 함수가 만들어짐
val add2 = adder(2,_:int)

// 새로 만들어진 add2 함수 사용
add2(3)
// output 5
```

### 가변 길이 인자
동일한 타입의 매개변수가 반복되는 경우 처리할 수 있는 문법  
n개의 매개변수를 처리할 때 사용
```scala
// *키워드를 이용해 여러개의 문자를 받을 수 있도록 함 단, 타입은 String로 고정
def capitalizeAll(args: String*) = {
    args.map{arg => 
        arg.capitalize
    }
}

capitalizeAll("rarity", "applejack")
// output ArrayBuffer(Rarity, Applejack)
```

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