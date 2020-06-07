# 어노테이션
어노테이션이란?
부가 정보를 프로그램에 장식할 수 있는 기능으로 문법적 메타데이타

아래의 예제코드를 보자
```java
@Before
public void setUp(){
    this.list = new ArrayList<>();
}

@Test
public void testAlgorithm(){
    assertEquals(5, list.size());
}
```

위의 예제에서 어노테이션의 아래의 용도로 사용
- JUnit의 콘텍스트에서 어노테이션으로 설정 작업을 하는 메서드와 단위 테스트를 실행하는 메서드 구분
- 문서화에 어노테이션을 이용하여 사용하지 말아야하는 메서드에 @Deprecated 어노테이션 활용
- 자바 컴파일러에서도 어노테이션을 사용해 에러를 검출하고 경고를 줄이고 코드를 생성 할 수 있음
- 자바 EE에서 엔터프라이즈 애플리케이션을 설정할 때 어노테이션을 많이 활용
