public class Fish extends Animal{
    public Fish(String name, int age, String gender, int weightIbLbs) {
        super(name, age, gender, weightIbLbs);
    }

    public void swim() {
        System.out.println("Swimming...");
    }

    public void move() {
        System.out.println("Fish is swimming...");
    }
}
