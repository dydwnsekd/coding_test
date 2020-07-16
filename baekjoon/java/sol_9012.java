package baekjoon;

import java.util.*;

public class sol_9012 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner in = new Scanner(System.in);
		
		int a = in.nextInt();
		String temp = "";
		in.nextLine();
		
		int count;
		
		for(int i=0;i<a;i++)
		{
			count = 0;
			
			temp = in.next();
			for(int j=0; j<temp.length();j++)
			{
				if(temp.charAt(j) == '(') count++;
				else if(temp.charAt(j) == ')') 
				{
					count--;
					if(count < 0) break;
				}
			}
			
			if (count == 0) System.out.println("YES");
			else System.out.println("NO");
			
			//System.out.println(open_count);
			//System.out.println(close_count);
		}

	}

}
