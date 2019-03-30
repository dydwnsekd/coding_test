package baekjoon;

import java.util.*;

public class sol_2441 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int a = in.nextInt();
		
		for(int i=a; i>0; i--)
		{
			for(int j=a; j>i; j--)
			{
				System.out.print(" ");
			}
			for(int k=i; k>0; k--)
			{
				System.out.print("*");
			}
			System.out.println();
		}
		
		
	}

}
