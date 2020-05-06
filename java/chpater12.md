# 새로운 날짜와 시간 API
Java 1.0에서의 날짜 시간 클래스
Java.util.Data
```
Date date = new Date(117, 8, 21);

# 출력 결과
Thu Sep 21 00:00:00 CET 2017
```

Data class의 문제점
- 직관적이지 않음
- Date 클래스의 toString로 반환되는 문자열을 추가로 활용하기 어려움  
- CET(중앙 유럽 시간)으로 설정되어 있어 추가적인 변환작업이 필요

Java 1.1에서 새로운 Java.util.Calendar class 추가
- 달의 index가 0부터 시작
- Date와 Calendar 두 가지 클래스가 통일되지 않아 개발자들간의 문제 발생(DateFormat 같은 경우 Date class에만 존재)
- Date와 Calendar 모두 가변 클래스로 유지보수가 어려움

위와 같은 문제점으로 Joda-Time와 같은 third-party 날짜/시간 라이브러리 사용  
java 8에서 java.time 패키지로 추가

## 12.1 LocalDate, LocalTime, Instant, Duration, Period

