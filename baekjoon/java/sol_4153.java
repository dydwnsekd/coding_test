package com.testproject;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class sol_4153 {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        while(true) {
            ArrayList<Integer> num_list = new ArrayList<>();
            int a = 0;

            for(int i=0;i<3;i++)
                num_list.add(in.nextInt());

            int max_value = Collections.max(num_list);
            int min_value = Collections.min(num_list);

            if(max_value == min_value && min_value == 0)
                break;

            for(int i: num_list){
                if(i != max_value)
                    a += Math.pow(i, 2);
            }

            if(a == Math.pow(max_value,2))
                System.out.println("right");
            else
                System.out.println("wrong");
        }
    }
}