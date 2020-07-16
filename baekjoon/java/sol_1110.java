//https://www.acmicpc.net/problem/1110

import java.util.*;

public class sol_1110
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();

        cycle_1110 a = new cycle_1110(num);
        a.cycle_cal();

        System.out.println(a.get_count());
    }
}

class cycle_1110
{
    int num = 0;
    int count = 0;

    public cycle_1110(int num)
    {
        this.num = num;
    }

    public void cycle_cal()
    {
        int cur_num = this.num;

        int first_num;
        int last_num;
        int temp = 0;

        do
        {
            if (check_10(cur_num))
            {
                first_num = cur_num/10;
                last_num = cur_num%10;

                temp = first_num + last_num;
                temp = temp%10;

                cur_num = last_num*10 + temp;
            }
            else
                cur_num = cur_num * 10 + cur_num;

            this.count += 1;
        } while(cur_num != this.num);
    }

    public int get_count()
    {
        return this.count;
    }

    private boolean check_10(int num)
    {
        if (num >= 10) return true;
        else return false;
    }
}