import java.util.Scanner;

public class sol_1016 {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        long min = in.nextLong();
        long max = in.nextLong();

        ArrayList<Long> num_list = new ArrayList<>();

        long n = (long) Math.ceil(Math.sqrt(min));
        long m = (long) Math.floor(Math.sqrt(max));

        if(n<=1)
            n=2;

        for(long i=n;i<=m;i++) {
            long temp = i*i;
            long count = 1;
            while(true) {
                if(temp*count > max)
                    break;
                else if(!num_list.contains(temp*count)) {
                    num_list.add(temp * count);
                    count++;
                }
                else
                    count++;
            }
        }

        System.out.println(max-min-num_list.size()+1);

    }
}