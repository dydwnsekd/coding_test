import java.time.LocalDate;
import java.time.ZoneId;
import java.time.ZonedDateTime;

public class aetaewt {
    public static void main(String[] args) {

        ZoneId a = ZoneId.of("Asia/Seoul");
        LocalDate date = LocalDate.of(2011,1,2);
        ZonedDateTime zdt1 = date.atStartOfDay(a);

        System.out.println(zdt1);
    }
}
