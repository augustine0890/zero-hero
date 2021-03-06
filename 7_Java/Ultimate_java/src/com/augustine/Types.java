package com.augustine;

import java.awt.*;
import java.text.NumberFormat;
import java.util.Arrays;
import java.util.Date;
import java.util.Scanner;

public class Types {

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

        // Order of Operations
        int y = 2 + 3 * 5;

        // Casting: byte > short > int > long > float > double
        short z = 1;
        int t = z + 2;

        double x1 = 1.1;
        int y1 = (int)x1 + 2;

        String x2 = "1";
        int y2 = Integer.parseInt(x2) + 2;

        // Math Class
        int res3 = Math.round(1.1F);
        double res4 = Math.round(Math.random() * 100);

        // Formatting Numbers
        // NumberFormat currency = NumberFormat.getCurrencyInstance();
        NumberFormat percent = NumberFormat.getPercentInstance();
        String res5 = percent.format(0.1);

        // Reading Input
        Scanner scanner = new Scanner(System.in);
        System.out.print("Name: ");
        // byte age = scanner.nextByte();
        String name = scanner.nextLine().trim();
        System.out.println("You are " + name);

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

        System.out.println(y);
        System.out.println(t);
        System.out.println(y1);
        System.out.println(y2);

        System.out.println(res3);
        System.out.println(res4);

        System.out.println(res5);

        System.out.println("===End===");
    }
}
