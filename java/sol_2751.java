import java.util.*;

public class sol_2751 {

    public static void main(String[] args) {
        
        ArrayList<Integer> a = new ArrayList<>();
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();
        
        for(int i=0; i<num; i++)
        {
            a.add(in.nextInt());
        }
        System.out.println(a);
        
        //이 경우 int형 배열만 사용 가능 ArrayList를 사용하는 경우는 직접 구현해야 할 것 같음.
        //Arrays.sort(a);
    }

}
