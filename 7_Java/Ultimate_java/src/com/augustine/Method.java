package com.augustine;

public class Method {
    public static void main(String[] args) {
        String message = greetUser("Augustine", "Nguyen");
        System.out.println(message);
    }

    public static String greetUser (String firstName, String lastName) {
        return "Hello " + firstName + " " + lastName;
    }
}
