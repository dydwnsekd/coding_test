import java.util.*;

//배열 형식으로 입력이 들어왔을 때 (String) 그걸 진짜 배열에 넣어서 반환하는 함수 개발
//split와 StringTokenizer의 차이
//split의 경우 split(",[")를 사용하는 경우 ,[ 로 문자열을 자르는 반면
//StringTokenizer의 경우 ",[" 를 사용하는 경우 , or [ 로 구분해서 문자열을 자름

public class array_split {

	public static void main(String[] args) {

        
    }

    public ArrayList OneArray(String s)
    {
        // 1차원 배열
        ArrayList<String> str_al = new ArrayList<>();
    
        s = s.replaceAll(" ", "");
        s = s.substring(1, s.length()-1);

        for (String temp: s.split(","))
            str_al.add(temp);
        
        return str_al;
    }

    public ArrayList TwoArray(String s)
    {
        // 2차원 배열
        s = s.substring(1, s.length()-1).replaceAll(" ", "");
        ArrayList<ArrayList<String>> str_al = new ArrayList<>();
        ArrayList<String> al_temp = new ArrayList<>();
        StringTokenizer st_temp = null;

        for (String temp: s.split("\\],"))
        {
            st_temp = new StringTokenizer(temp, "[,]");
            while (st_temp.hasMoreTokens())
            {
                al_temp.add(st_temp.nextToken());
            }
            //System.out.println(al_temp);
            str_al.add((ArrayList)al_temp.clone());
            al_temp.clear();
        }

        return str_al;
    }
}