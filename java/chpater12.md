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
java.time 패키지에는 LocalDate, LocalTime, LocalDateTime, Instant, Duration, Period 클래스를 제공  

### 12.1.1 LocalDate와 LocalTime 사용
LocalDate는 어떤 시간대 정보도 가지지 않음

LocalDate를 사용하는 간단한 예
```
LocalDate date = LocalDate.of(2017, 9, 21); // 2017-09-21 날짜 생성
int year = date.getYear();
Month month = date.getMonth();
int day = date.getDayOfMonth();
DayOfWeek dow = date.getDayOfWeek();
int len = date.lengthOfMonth();
boolean leap = date.isLeapYear();           // 윤년 여부 판단

LocalDate today = LocalDate.now();          // 현재 날짜 생성

System.out.println(date);
System.out.println(today);
```

get 메서드로 TemporalField를 전당해 정보를 얻는 방법  
TemporalField는 시간 관련 객체에서 어떤 필드의 값에 접근할지 정의하는 인터페이스  
열거자 ChronoField는 TemporalField 인터페이스를 정의하므로 ChronoField의 열거자를 이용해 아래와 같이 사용 가능
```
int year = date.get(ChronoField.YEAR);
int month = date.get(ChronoField.MONTH_OF_YEAR);
int day = date.get(ChronoField.DAY_OF_MONTH);

System.out.println(year);
System.out.println(month);
System.out.println(day);
```

날짜가 아닌 시간에 대한 것은 LocalTime를 이용해 사용  
```
LocalTime time = LocalTime.of(13,45, 20);
int hour = time.getHour();
int minute = time.getMinute();
int second = time.getSecond();

System.out.println(hour);
System.out.println(minute);
System.out.println(second);
```

문자열로 LocalDate와 LocalTime 만들기  
parse를 이용해 문자열을 date, time로 변경
```
LocalDate date = LocalDate.parse("2017-09-21");
LocalTime time = LocalTime.parse("13:45:20");

System.out.println(date);
System.out.println(time);
```

### 12.1.2 날짜와 시간 조합
날짜와 시간을 모두 표현하는 LocalDateTime  
LocalDateTime는 위의 예제에서 본 Date와 Time를 하나의 클래스로 나타냄
```
LocalDate date = LocalDate.parse("2017-09-21");
LocalTime time = LocalTime.parse("13:45:20");

LocalDateTime dt1 = LocalDateTime.of(2017, Month.SEPTEMBER, 21, 13, 45, 20);
LocalDateTime dt2 = LocalDateTime.of(date, time);
LocalDateTime dt3 = date.atTime(13,45,20);
LocalDateTime dt4 = date.atTime(time);
LocalDateTime dt5 = time.atDate(date);

System.out.println(dt1);
System.out.println(dt2);
System.out.println(dt3);
System.out.println(dt4);
System.out.println(dt5);

LocalDate date1 = dt1.toLocalDate();
LocalTime time1 = dt1.toLocalTime();

System.out.println(date1);
System.out.println(time1);
```

### 12.1.3 Instant 클래스 : 기계와 날짜와 시간
기계의 관점에서의 시간은 연속된 시간에서 특정 지점을 기준으로 하나의 큰 수로 표현하는 것이 자연스러움  
java.time.Instant 클래스를 이용해 유닉스 시간(1970년 1월 1일 0시 0분 0초)로 표현  
Instant 클래스를 이용해 나노초(10억분의 1초)까지 표현  
모두 같은 시간의 표현하는 예
```
Instant t1 = Instant.ofEpochSecond(3);
Instant t2 = Instant.ofEpochSecond(3, 0);
Instant t3 = Instant.ofEpochSecond(2, 1_000_000_000);
Instant t4 = Instant.ofEpochSecond(4, -1_000_000_000);

System.out.println(t1);
System.out.println(t2);
System.out.println(t3);
System.out.println(t4);
```


