package com.augustine;

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
    }
}
