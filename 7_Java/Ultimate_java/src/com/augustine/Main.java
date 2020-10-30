package com.augustine;

import java.awt.*;
import java.util.Arrays;
import java.util.Date;

public class Main {

    public static void main(String[] args) {
        // Primitive types
        byte myAge = 30;
        myAge = 29;
        int viewsCount = 123_456_789;
        long biggerViewsCount = 3_123_456_789L;
        float price = 10.99F;
        char letter = 'A';
        boolean isExpire = false;

        // Reference types
        Date now = new Date();
//        now.getTime();

        // Reference vs Primitive
        Point point1 = new Point(1, 1);
        Point point2 = point1;
        point1.x = 2;

        // Strings
        String message = new String(" Hello \"World\"" + "!");

        // Array
        int[] numbers = new int[5];
        numbers[0] = 1;
        numbers[1] = 2;

        int[] numbers2 = { 2, 4, 5, 1, 8 };
        Arrays.sort(numbers2);

        // Multi-dimensional Arrays
        int[][] matrix = new int[2][3];
        matrix[0][0] = 1;

        int[][] matrix2 = { { 1, 2, 3}, { 4, 5, 6} };

        // Constants
        final float pi = 3.14F;

        // Arithmetic
        int result = 10 / 3;
        double res2 = (double) 10 / (double) 3;

        int x = 1;
        x++;
        x += 2;

        System.out.println(message);
        System.out.println(message.endsWith("!"));
        System.out.println(message.indexOf("H"));
        System.out.println(message.trim());

        System.out.println(myAge);
        System.out.println(viewsCount);
        System.out.println(biggerViewsCount);
        System.out.println(price);
        System.out.println(letter);
        System.out.println(isExpire);

        System.out.println(now);

        System.out.println(point2);

        System.out.println(Arrays.toString(numbers));
        System.out.println(numbers2.length);
        System.out.printf("%s \n", Arrays.toString(numbers2));

        System.out.println(Arrays.deepToString(matrix));
        System.out.println(Arrays.deepToString(matrix2));

        System.out.println(result);
        System.out.println(res2);
        System.out.println(x);

        System.out.println("===End===");
    }
}
