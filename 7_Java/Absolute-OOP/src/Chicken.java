public class Chicken extends Bird {
    public Chicken(String name, int age, String gender, int weightIbLbs) {
        super(name, age, gender, weightIbLbs);
    }

    public void fly() {
        System.out.println("Not able to fly...");
    }
}
