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

public class tmon_test2{

     public static void main(String []args){
        Parent p = new Child();
        p.printMember();
     }
}

