package baekjoon;

import java.util.*;

public class sol_11721 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner in = new Scanner(System.in);
		String a = in.next();
		
		int len = (a.length()/10)+1;
		
		for(int i=0;i<len;i++)
		{
			if(a.length() < i*10 + 10)
				System.out.println(a.substring(i*10,a.length()));
			else
				System.out.println(a.substring(i*10, i*10+10));
		}
		
	}

}
