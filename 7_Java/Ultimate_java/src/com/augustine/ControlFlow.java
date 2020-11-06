package com.augustine;

import java.util.Scanner;

public class ControlFlow {
    public static void main(String[] args) {
        // Comparison Operators
        int x = 1;
        int y = 2;
        System.out.println(x == y);
        System.out.println(x != y);
        System.out.println(x <= y);
        System.out.println(x >= y);

        // Logical Operators
        int temperature = 22;
        boolean isWarm = temperature > 20 && temperature < 30;
        System.out.println("Is warm: " + isWarm);

        boolean hasHighIncome = true;
        boolean hasGoodCredit = true;
        boolean hasCriminalRecord = false;
        boolean isEligible = (hasHighIncome || hasGoodCredit) && !hasCriminalRecord;
        System.out.println("Is eligible " + isEligible);

        // If Statements
        int temp = 32;
        if (temp > 30) {
            System.out.println("It's a hot day");
            System.out.println("Drink water");
        } else if (20 < temp) {
            System.out.println("Beautiful day");
        } else {
            System.out.println("Cold day");
        }

        // Simplifying If Statements
        int income = 120_000;
        boolean highIncome = (income > 100_000);
        System.out.println(highIncome);
        // The Ternary Operator
        String className = income > 100_000 ? "First" : "Economy";
        System.out.println(className);

        // Switch Statement
        String role = "admin";

        switch (role) {
            case "admin":
                System.out.println("You're an admin");
                break;
            case "moderator":
                System.out.println("You're a moderator");
                break;
            default:
                System.out.println("You're a guest");
        }

        // For Loops
        for (int i = 0; i < 5; i++)
            System.out.println("Hello, World!");

        // While Loops
        int i = 5;
        while (i > 0) {
            System.out.println("Looping " + i);
            i--;
        }

        Scanner scanner = new Scanner(System.in);
        String input = "Initialize";
        while (!input.equals("quit")) {
            System.out.println("Input: ");
            input = scanner.next().toLowerCase();
            System.out.println(input);
        }

        /* Do..While Loops */
        do {
            System.out.println("Input: ");
            input = scanner.next().toLowerCase();
            System.out.println(input);
        } while (!input.equals("quit"));
    }
}
