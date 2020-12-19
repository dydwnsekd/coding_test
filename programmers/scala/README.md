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

## 클래스
class 키워드로 선언 class안에는 필드와 메소드를 선언할 수 있음
```scala
class Calculator {
    val  brand: String = "HP"
    def add(m: Int, n: Int): Int = m + n
}

val calc = new Calculator

calc.add(1,2)
// output 3

calc.brand
// output "HP"
```

### 상속
extends keyword를 이용해 상속
```scala
class ScientificCalculator(brand: String) extends Calculator(brand) {
    def long(m: Double, base: Double) = math.log(m) / math.log(base)
}
```

### 추상 클래스(abstract class)
메소드 정의는 있지만 구현은 없는 클래스  
추상 클래스를 상속한 하위 클래스에서 메소드를 구현하영 사용하며 추상 클래스는 인스턴스를 만들 수 없음

```scala
// 추상클래스
abstract class Shape {
    def getArea(): Int //선언만 존재
}

// 상속받아 구현
class Circle(r: Int) extends Shape {
    def getArea():Int = { r * r * 3 }
}
```

Scala는 기본적으로 immutable로 불변의 객체를 가짐  
List를 mutable로 List를 만들기 위해서는  

scala.collection.mutable에 있는 것들을 import해서 사용
ListBuffer, ArrayBuffer 등이 있음  
ArrayBuffer, ListBuffer을 사용할 때 타입 선언이 필요 
```scala
import scala.collection.mutable.*
var a = ListBuffer[Int]()
var b = ArrayBuffer[Int]()

// 요소 추가
a+=1
println(a)
//output : ListBuffer(1)
```

## 트레잇(Traits, 특성)
다른 클래스가 확장(상속)하거나 섞어 넣을 수 있는 필드와 동작의 모음
```scala
trait Car {
    val brand: String
}

trait Shiny {
    val shineRefraction: Int
}

class BMW extends Car {
    val brand = "BMW"
}

// 여러 trait 사용 class with keyword 사용
class BMW extends Car with Shiny {
    val brand = "BMW"
    val shineRefraction = 12
}
```

### 추상클래스와 트래잇  
- 둘은 비슷한 역할을 수행
- 추상클래스는 하나만 상속할 수 있지만 tarit는 여러 가지를 받아 사용할 수 있어 확장을 위해서는 trait를 사용하는것이 좋음
- 생성자 매개변수가 필요하다면 추상클래스를 사용 trait은 생성자를 허용하지 않음


## apply 메소드
객체 인스턴스를 호출했을 때 대신해서 호출되는 메소드  
bar만 호출해도 apply에 있는 0이 출력
```scala
class Bar {
    def apply() = 0
}

val bar = new Bar
bar()
//output 0
```

## 패턴매칭
값 또는 조건물을 사용해 매칭 가능
```scala
val times = 1
times match {
    case 1 => "one"
    case 2 => "two"
    case _ => "some other number"
    // 여기서 사용하는 _는 else와 같은 의미로 사용
}

times match {
    case i if i == 1 => "one"
    case i if i == 2 => "two"
    case _ => "some other number"
}
```

## 예외처리
java에서와 같이 try-catch-finally와 같이 사용

## 컬렉션

## List(리스트)
List()로 사용
```scala
val numbers = List(1,2,3,4)
```
List 계열의 특정 index 값에 접근하는 경우 ()사용 python은 []로 헷갈리지 않도록 조심  
immutable로 되어 있는 List의 값 update 방법  
```scala
List = List.updated(index, value)
```
List에 있는 updated method를 이용 index와 변경하고자 하는 값을 넣고 다시 List로 반환받아서 사용해야 함

List의 길이
```scala
List.length
```

List 요소 추가 += 연산자 사용
```scala
List = List += a
```

List 자르기
```scala
List.slice(start_index, end_index)
```

List 안에 값이 포함되어 있는지 확인 여부
```scala
List.contains(value)
```

## set(집합)
중복된 데이터가 없는 컬렉션
```scala
Set(1,1,2)
//output : Set(1,2)
```

## tuple(튜플)
클래스를 정의하지 않고 type가 다른 여러 값들을 묶어서 사용  
List없이 ()롤 사용
```scala
val hostPort = ("localhost", 80)
// hostPort: (String, Int) = (localhost, 80) 형태로 저장
```

## map(맵)
key value 형식으로 저장하는 것  
```scala
val a = Map(1 -> 2)  
a(1)
//output : 2
```
1이 Key, 2가 Value형식으로 저장되어 사용  
Key, Value의 type는 서로 다를 수 있음

## Option(옵션)
어떤 것이 존재하거나 존재하지 않을 수 있는데 이를 처리하기 위한 방법으로 Option 사용  
```scala
// Option의 기본 인터페이스
trait Option[T] { def isDefined: Boolean def get: T def getOrElse(t: T): T }
// 옵션 자체는 일반적 클래스며, Some[T] None의 하위 클래스를 가짐
// Map.get은 Option을 반환

val numbers = Map("one" -> 1, "two" -> 2)
numbers.get("two")
//output : Some(2)

numbers.get("three")
//output : None
```
None를 처리하기 위해서는 getOrElse나 패턴매칭를 이용해 처리할 수 있음
아래와 비슷한 형식으로 사용 가능
```scala
val result = nunmbers.getOrElse(0) * 2
```

# 함수 콤비네이터
함수와 컬렉션 등 다른 식을 받아서 적절한 작업을 해주는 조합 장치 정도로 생각

## map
리스트의 모든 원소에 함수를 적용한 결과값으로 이루어진 새 리스트를 반환  
원소 갯수는 적용 대상이 된 리스트의 원소 갯수와 동일  
```scala
val numbers = List(1,2,3,4)
numbers.map((i: Int) => i * 2)
// output : List(2,4,6,8)

// 기존 선언된 함수를 적용하는 것도 가능
def timesTwo(i: Int): Int = i * 2
numbers.map(timesTwo _)
// output : List(2,4,6,8)
```

### foreach
맵과 비슷하지만 반환하는 것이 없이 상태를 변환
```scala
numbers.foreach((i: Int) => i * 2)
// output : 없음
```
for문을 foreach로 바꿔 사용할 수 있음
구구단 출력의 예
```scala
for (i <- 1 until 10) {
      for (j <- 1 to 9)
        println(i + " * " + j + " = " + i * j)
}

//위의 for문을 foreach를 사용해 아래와 같이 사용가능
val a = 1 until 10
val b = 1 to 9
a.foreach(i => b.foreach(j => println(i + " * " + j + " = " + i * j)))
```

### filter
전달된 함수가 거짓을 반환하는 원소들을 제외한 나머지 원소들로 이루어진 리스트를 반환  
```scala
numbers.filter((i: Int) => i % 2 == 0)
// output : List(2,4)
```

### zip
zip은 두 리스트의 원소들의 쌍(튜플)로 이루어진 단일 리스트를 반환
```scala
List(1,2,3).zip(List("a", "b", "c"))
// output : List((1,a), (2,b), (3,c))
```
1,2,3과 a,b,c 를 묶어서 반환

### partition
partition은 술어 함수가 반환하는 값에 따라 리스트를 둘로 나눈다
```scala
val numbers = List(1,2,3,4,5,6,7,8,9,10)
numbers.partion(_ % 2 == 0)
// output : List(2,4,6,8,10), List(1,3,5,7,9)
```

### find
리스트에서 술어함수를 만족하는 가장 첫 원소 반환
```scala
numbers.find((i: Int) => i > 5)
// output : Some(6)
```

## drop
첫 i개의 원소를 제거하며 나머지의 원소만 남음
```scala
numbers.drop(5)
//output : List(6,7,8,9,10)
```

## dropWhile
리스트의 앞에서 술어함수를 만족하는 최초의 원소까지만 자르고 뒤는 남겨짐  
filter와 drop가 하나로 합쳐진 느낌
```scala
numbers.dropWhile(_ % 2 != 0)
// output : List(2,3,4,5,6,7,8,9,10)
```

## foldLeft
누적 연산을 진행하며 초기값, 연산을 지정하면 반환값이 나온다
```scala
numbers.foldLeft(0)((m: Int, n: Int) => m + n)
//output : 55
```
foldLeft의 동작과정은 아래와 같음  
m: 0, n: 1  
m: 1, n: 2  
m: 3, n: 3  
m: 6, n: 4  
m: 10, n: 5  
m: 15, n: 6  
m: 21, n: 7  
m: 28, n: 8  
m: 36, n: 9  
m: 35, n: 10  
output : 55  

기준값을 m(왼쪽)에 넣고 n(오른쪽)을 계속 더하는 연산 진행

## foldRight
foldLeft와 반대로 누적값을 오른쪽으로 넣는데 List연산의 순서가 반대
m: 10, n: 0  
m: 9, n: 10  
m: 8, n: 19  
m: 7, n: 27  
m: 6, n: 34  
m: 5, n: 40  
m: 4, n: 45  
m: 3, n: 49  
m: 2, n: 52  
m: 1, n: 54  
output : 1  

위의 2가지는 +연산에서는 동일한 결과를 가지지만 다른 연산을 진행하는 경우에는 다른 결과가 나올 수 있음  

## flatten
2개의 리스트를 하나로 연결해 상위 하나의 리스트로 병합
```scala
List(List(1,2), List(3,4)).flatten
// output : List(1,2,3,4)
```

## flatMap
map와 flatten을 합성한 것으로 내포 리스트에 적용할 수 있는 함수를 중첩된 리스트 안에 각각 적용한 후 하나로 합치는 작업
```scala
val nestedNumbers = List(List(1,2), List(3,4))

nestedNumbers.flatMap(x => x.map(_ * 2))
// output : List(2,4,6,8)
```