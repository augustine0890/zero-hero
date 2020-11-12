public class Zoo {
    public static void main(String[] args) {
        Animal tim = new Animal("Tim", 3, "Male", 12);
        tim.speak();
        tim.eat();
        tim.sleep();

        Bird bird1 = new Bird("Pi", 1, "Female", 2);
        bird1.speak();
        // bird1.fly();
        bird1.eat();
        bird1.sleep();

        Chicken chicken1 = new Chicken("Chick", 1, "Female", 1);
        // chicken1.fly();

        Sparrow sparrow1 = new Sparrow("Spa", 1, "Male", 1);
        sparrow1.fly();
    }
}
