class sort(object):

    def bubble(sort_list):
        for i in range(len(sort_list)-1, 0, -1):
            for j in range(0, i):
                if sort_list[j] > sort_list[j+1]:
                    sort_list[j], sort_list[i] = sort_list[j], sort_list[i]
        
        return sort_list


'''
public static ArrayList<Integer> bubble(ArrayList<Integer> input_arr)
    {
        int temp;
        for(int i=input_arr.size()-1; i>0; i--)
        {
            for(int j=0; j<i; j++)
            {
                if(input_arr.get(j) > input_arr.get(j+1))
                {
                    temp = input_arr.get(j);
                    input_arr.set(j, input_arr.get(j+1));
                    input_arr.set(j+1, temp);
                }
            }
        }
        return input_arr;
    }

    public static ArrayList<Integer> selection(ArrayList<Integer> input_arr)
    {
        int temp;
        int idx = 0;
        for(int i=0; i<input_arr.size()-1; i++)
        {
            idx = i;
            for(int j=i+1; j<input_arr.size(); j++)
            {
                if(input_arr.get(idx) > input_arr.get(j))
                    idx = j;
            }
            temp = input_arr.get(i);
            input_arr.set(i, input_arr.get(idx));
            input_arr.set(idx, temp);
        }
        return input_arr;
    }


    public static ArrayList<Integer> insertion(ArrayList<Integer> input_arr)
    {
        int temp;
        int idx=0;
        for(int i=1; i<input_arr.size(); i++)
        {
            idx = i;
            temp = input_arr.get(i);
            for(int j=i-1; j>=0; j--)
            {  
                if(temp < input_arr.get(j))
                {
                    input_arr.set(idx, input_arr.get(j));
                    idx = j;
                    if(j==0)
                        input_arr.set(0, temp);
                }
                else
                {
                    input_arr.set(idx, temp);
                    break;
                }
            }
        }
        return input_arr;
    }
'''