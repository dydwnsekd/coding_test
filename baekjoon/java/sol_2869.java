package com.testproject;

import java.util.Scanner;

public class sol_2869 {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        long a = in.nextInt();
        long b = in.nextInt();
        double v = in.nextDouble();

        long day = 1;

        day += Math.ceil((v-a) / (a-b));

        System.out.println(day);
    }
}