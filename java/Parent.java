public class Parent {
    protected int value;
    protected Parent()
    {
        value = 100;
        System.out.println(value);
    }
    protected void printMember()
    {
        System.out.println(value);
    }
}