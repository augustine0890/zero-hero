public class Bird extends Animal {
    public Bird(String name, int age, String gender, int weightIbLbs) {
        super(name, age, gender, weightIbLbs);
    }
    // overriding the method defined in Bird
    public void fly() {
        System.out.println("Flying...");
    }
}
