package com.augustine;

import java.awt.*;
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
        String message = new String(" Hello World" + "!");

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
        System.out.println("===End===");
    }
}
