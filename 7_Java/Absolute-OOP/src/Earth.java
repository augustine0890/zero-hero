public class Earth {
    public static void main(String[] args) {
        /*
        Human tom;
        tom = new Human();
        tom.age = 5;
        tom.eyeColor = "brown";
        tom.name = "Tom Jack";
        tom.heightInInches = 72;
        */

        Human tom = new Human("Tom Hanks", 5, 72, "brown");
        System.out.println("Calling method...");
        tom.speak();

        /*
        Human joe = new Human();
        joe.age = 6;
        joe.eyeColor = "blue";
        joe.name = "Joe Collins";
        joe.heightInInches = 75;
        */
        Human joe = new Human("Joe Collins", 6, 75, "blue");
        joe.speak();

    }
}
