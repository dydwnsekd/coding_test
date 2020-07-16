import java.util.*;

public class sol_2750 {

    public static void main(String[] args) {
        
        ArrayList<Integer> a = new ArrayList<>();
        ArrayList<Integer> result = new ArrayList<>();
        Scanner in = new Scanner(System.in);
        int current = 999999999;
        int idx = 0;
        int num = in.nextInt();
        
        for(int i=0; i<num; i++)
            a.add(in.nextInt());
        
        //이 경우 int형 배열만 사용 가능 ArrayList를 사용하는 경우는 직접 구현해야 할 것 같음.
        //Arrays.sort(a);

        for(int i=num; i>0; i--)
        {
            for(int j=0; j<i; j++)
            {
                if(current > a.get(j))
                {
                    idx = j;
                    current = a.get(j);
                }
            }
            a.remove(idx);
            result.add(current);
            current = 999999999;
        }

        for(int i=0; i<num; i++)
            System.out.println(result.get(i));
    }

}
