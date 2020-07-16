package baekjoon;

import java.util.*;

public class sol_8393 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner in = new Scanner(System.in);
		
		int a = in.nextInt();
		int temp = 0;
		
		for(int i=1; i<=a; i++) temp+=i;
		
		System.out.println(temp);
	}

}
