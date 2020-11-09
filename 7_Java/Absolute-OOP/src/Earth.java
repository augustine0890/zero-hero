public class Earth {
    public static void main(String[] args) {
        Human tom;
        tom = new Human();
        tom.age = 5;
        tom.eyeColor = "brown";
        tom.name = "Tom Jack";
        tom.heightInInches = 72;

        System.out.println("Calling method...");
        tom.speak();
    }
}
