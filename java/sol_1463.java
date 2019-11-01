import java.util.*;

// 1~n까지의 결과를 모두 저장하는 방식을 사용
// 결과를 저장하고 1~n까지 반복문을 이용해 돌면서 결과를 저장
// 더 큰 숫자가 들어왔을때 3가지 연산을 모두 실행하여 그 결과를 배열에 누적 저장
// 숫자별로 가장 작은 값을 찾을 수 있도록 함
public class sol_1463 {

	public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        int n = in.nextInt();
        int count = 0;
        
        while(n!=1)
        {
            if(n%3==0)
                n /= 3;
            else if(n%2==0)
                n /= 2;
            else
                n -= 1;
            
            System.out.println(n);
            count++;
        }

        System.out.println(count);

	}

}
