import java.util.Scanner;

public class sol_1100 {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int count = 0;

        for(int i=0;i<8;i++){
            String row = in.nextLine();
            if(i%2==0){
                for(int j=0;j<8;j++){
                    if(j % 2 == 0 && row.charAt(j) == 'F')
                        count++;
                }
            }
            else{
                for(int j=0;j<8;j++){
                    if(j % 2 == 1 && row.charAt(j) == 'F')
                        count++;
                }
            }
        }
        System.out.println(count);
    }
}