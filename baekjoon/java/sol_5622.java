import java.util.*;

public class sol_5622 {

    public static void main(String[] args) throws Exception {
        
        Scanner in = new Scanner(System.in);
        String alphabet_list = in.next();

        int result = 0;
        
        for(int i=0;i<alphabet_list.length();i++)
        {
            if("ABC".contains(Character.toString(alphabet_list.charAt(i))))
                result += 3;
            else if("DEF".contains(Character.toString(alphabet_list.charAt(i))))
                result += 4;
            else if("GHI".contains(Character.toString(alphabet_list.charAt(i))))
                result += 5;
            else if("JKL".contains(Character.toString(alphabet_list.charAt(i))))
                result += 6;
            else if("MNO".contains(Character.toString(alphabet_list.charAt(i))))
                result += 7;
            else if("PQRS".contains(Character.toString(alphabet_list.charAt(i))))
                result += 8;
            else if("TUV".contains(Character.toString(alphabet_list.charAt(i))))
                result += 9;
            else if("WXYZ".contains(Character.toString(alphabet_list.charAt(i))))
                result += 10;
        }
        System.out.println(result);
    }
}