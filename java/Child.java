public class Child extends Parent {
    String value;
    public Child()
    {
        super();
        value = "abcd";
        System.out.println(value);
    }
    
    public void printMember()
    {
        System.out.println(value);
    }
}