import java.util.*;

    public class sol_1152 {
    
        public static void main(String[] args) {
    
            Scanner in = new Scanner(System.in);
            String n = in.nextLine().trim();
            int word_count=0;


            if(n.equals(""))
                word_count = 0;
            else
                word_count = n.split(" ").length;
    
            System.out.println(word_count);
            
        }
    }
    
    