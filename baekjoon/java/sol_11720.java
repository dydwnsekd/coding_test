package baekjoon;

import java.util.*;

public class sol_11720 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner in = new Scanner(System.in);
		int a = in.nextInt();
		String b = in.next();
		
		int result = 0;
		
		for(int i=0; i<a; i++)
		{
			result += Integer.parseInt(b.substring(i, i+1));
		}
		System.out.println(result);
	}

}
