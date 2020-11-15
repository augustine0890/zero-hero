public abstract class Animal {
    String name;
    int age;
    String gender;
    int weightIbLbs;

    public Animal(String name, int age, String gender, int weightIbLbs) {
        this.name = name;
        this.age = age;
        this.gender = gender;
        this.weightIbLbs = weightIbLbs;
    }

    public void speak() {
        System.out.println("I am " + this.name + " and I'm " + this.age + " years old.");
    }

    public void eat() {
        System.out.println("Eating...");
    }

    public void sleep() {
        System.out.println("Sleeping...");
    }

    public abstract void move();
}
