import java.util.*;

// 1~n까지의 결과를 모두 저장하는 방식을 사용
// 결과를 저장하고 1~n까지 반복문을 이용해 돌면서 결과를 저장
// 더 큰 숫자가 들어왔을때 3가지 연산을 모두 실행하여 그 결과를 배열에 누적 저장
// 숫자별로 가장 작은 값을 찾을 수 있도록 함
public class sol_1463 {

	public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int result_list[] = new int[1000001];

        result_list[1] = 0;
        result_list[2] = 1;

        for(int i=3; i<=1000000;i++)
        {
            int temp = 1000000;
            if(i%3==0)
                if(result_list[i/3] < temp)
                    temp = result_list[i/3];
            if(i%2==0)
                if(result_list[i/2] < temp)
                    temp = result_list[i/2];
            if(result_list[i-1] < temp)
                temp = result_list[i-1];
            
            result_list[i] = temp+1;
        }

        int n = in.nextInt();
        System.out.println(result_list[n]);
        
	}

}
