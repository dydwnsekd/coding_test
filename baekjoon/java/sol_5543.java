package com.testproject;

import java.util.ArrayList;
import java.util.Scanner;

import static java.util.Collections.min;

public class programmers {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        ArrayList<Integer> burger_list = new ArrayList<Integer>();
        ArrayList<Integer> drink_list = new ArrayList<Integer>();

        burger_list.add(in.nextInt());
        burger_list.add(in.nextInt());
        burger_list.add(in.nextInt());

        drink_list.add(in.nextInt());
        drink_list.add(in.nextInt());

        System.out.println(min(burger_list) + min(drink_list) - 50);
    }
}
