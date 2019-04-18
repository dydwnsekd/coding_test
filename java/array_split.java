import java.util.*;

//배열 형식으로 입력이 들어왔을 때 (String) 그걸 진짜 배열에 넣어서 반환하는 함수 개발

public class array_split {

	public static void main(String[] args) {

        // 1차원 배열
        Scanner in = new Scanner(System.in);
        // String str = in.nextLine();
        // ArrayList<String> str_al = new ArrayList<>();
	
        // StringTokenizer st = new StringTokenizer(str.substring(1, str.length()-1), ", ");
        // while(st.hasMoreElements())
        // {
        //     str_al.add(st.nextToken());
        // }
        // System.out.println(str_al);

        // 2차원 배열
        String sttr = in.nextLine();
        ArrayList<String> sttr_al = new ArrayList<>();
        StringTokenizer stt = new StringTokenizer(sttr.substring(1, sttr.length()-1), "],\\s[");
        System.out.println(stt.countTokens());
        System.out.println(sttr.substring(1, sttr.length()-1));

        while(stt.hasMoreElements())
        {
            System.out.println(stt.nextToken());
        }
        //System.out.println(sttr_al.size());
    }
}