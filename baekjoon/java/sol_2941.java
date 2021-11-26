import java.util.Scanner;

public class sol_2941 {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        String[] croatia_text = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};

        String text = in.next();
        int count = 0;

        for(String i: croatia_text) {
            if(text.contains(i)){
                int temp = text.length();
                text = text.replace(i, "&");
                if(i.length() == 2)
                    count += (temp-text.length());
                else
                    count += (temp-text.length()) / 2;
            }
        }
        text = text.replace("&", "");
        System.out.println(count + text.length());
    }
}