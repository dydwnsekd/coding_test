package app;

import java.util.*;

class my_stack {

    ArrayList<Integer> stack = new ArrayList<>();
    int head = -1;

    public my_stack()
    {

    }

    public void push(int num)
    {
        this.stack.add(num);
        head += 1;
    }
    
    public int pop()
    {
        if(head == -1) return -1;
        else
        {
            int value = stack.remove(head);
            head-=1;
            return value;
        }
    }
    public int size()
    {
        return head+1;
    }
    
    public int empty()
    {
        if(head == -1) return 1;
        else return 0;
    }

    public int top()
    {
        if(head == -1) return -1;
        else return stack.get(head);
    }

}



public class sol_10828 {
    public static void main(String[] args) throws Exception {
        // https://www.acmicpc.net/problem/10828 스택 구현 문제
        // class 생성하여 아래의 기능 구현
        // push X: 정수 X를 스택에 넣는 연산이다.
        // pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        // size: 스택에 들어있는 정수의 개수를 출력한다.
        // empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
        // top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

        Scanner in = new Scanner(System.in);
        String input_string = "";
        String command = "";
        String num = "";

        int a = in.nextInt();
        in.nextLine();

        my_stack ms = new my_stack();

        for(int i=0; i<a; i++)
        {
            input_string = in.nextLine();
            
            if (input_string.split(" ").length == 2)
            {
                command = input_string.split(" ")[0];
                num = input_string.split(" ")[1];

                if (command.equals("push")) ms.push(Integer.parseInt(num));
            }
            else
            {
                command = input_string;
                if (command.equals("pop")) System.out.println(ms.pop());
                else if (command.equals("size")) System.out.println(ms.size());
                else if (command.equals("empty")) System.out.println(ms.empty());
                else if (command.equals("top")) System.out.println(ms.top());
            }

        }
        in.close();
    }
}

