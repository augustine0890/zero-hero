public class Animal {
    String name;
    int age;
    int numLegs;
    boolean tail;
    boolean canSwim;

    public Animal(String name, int age, int numLegs, boolean tail, boolean canSwim) {
        this.name = name;
        this.age = age;
        this.numLegs = numLegs;
        this.tail = tail;
        this.canSwim = canSwim;
    }

    public void speak() {
        System.out.println("I am " + this.name + " and I'm " + this.age + " years old.");
    }
}
