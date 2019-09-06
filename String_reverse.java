public class String_reverse{

    public static void main(String []args){
       String a[] = {"I", "am", "a", "boy"};
       String[] reverseone = new String[a.length];
       
       for(int i=a.length;i>0;i--)
           reverseone[i-1] = a[a.length-i];
       
       for(int i=0;i<reverseone.length;i++)
           System.out.println(reverseone[i]);
    }
}