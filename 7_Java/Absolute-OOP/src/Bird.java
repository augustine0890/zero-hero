public class Bird extends Animal {
    public Bird(String name, int age, String gender, int weightIbLbs) {
        super(name, age, gender, weightIbLbs);
    }

    public void move() {
        System.out.println("Flapping wings...");
    }
}
