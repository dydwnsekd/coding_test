import java.util.*;
import org.apache.commons.lang.StringUtils;

//배열 형식으로 입력이 들어왔을 때 (String) 그걸 진짜 배열에 넣어서 반환하는 함수 개발
//split와 StringTokenizer의 차이
//split의 경우 split(",[")를 사용하는 경우 ,[ 로 문자열을 자르는 반면
//StringTokenizer의 경우 ",[" 를 사용하는 경우 , or [ 로 구분해서 문자열을 자름

public class array_split {

	public static void main(String[] args) {

        // 1차원 배열
        Scanner in = new Scanner(System.in);
        String str = in.nextLine();
        ArrayList<String> str_al = new ArrayList<>();
    
        str = str.replaceAll(" ", "");
        str = str.substring(1, str.length()-1);

        for (String temp: str.split(","))
            str_al.add(temp);
        
        System.out.println(str_al);

        // 2차원 배열
        String sttr = in.nextLine();
        sttr = sttr.substring(1, sttr.length()-1).replaceAll(" ", "");
        ArrayList<ArrayList<String>> sttr_al = new ArrayList<>();
        ArrayList<String> al_temp = new ArrayList<>();
        StringTokenizer st_temp = null;

        System.out.println(sttr);

        for (String temp: sttr.split("\\],"))
        {
            st_temp = new StringTokenizer(temp, "[,]");
            while (st_temp.hasMoreTokens())
            {
                al_temp.add(st_temp.nextToken());
            }
            //System.out.println(al_temp);
            sttr_al.add((ArrayList)al_temp.clone());
            al_temp.clear();
        }

        System.out.println(sttr_al);
    }
}