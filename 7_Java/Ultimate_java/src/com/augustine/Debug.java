package com.augustine;

import java.util.Arrays;

public class Debug {
    public static void main(String[] args) {
        String name = "Augustine";
        System.out.println(name);

        System.out.println("Start");
        printNumbers(4);
        System.out.println("Finish");
    }

    public static void printNumbers(int limit) {
        for (int n = 1; n <= limit; n++)
            System.out.println("number = " + n);
    }
}
