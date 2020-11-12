public class Sparrow extends Bird implements Flyable {
    public Sparrow(String name, int age, String gender, int weightIbLbs) {
        super(name, age, gender, weightIbLbs);
    }

    public void fly() {
        System.out.println("Sparrow flying high...");
    }
}
