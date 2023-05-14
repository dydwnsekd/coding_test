# TODO
import sys

person_count = int(sys.stdin.readline())
releation = int(sys.stdin.readline())

result = []
friend = {}
temp = []

for i in range(person_count):
    friend[i+1] = []

for i in range(releation):
    a, b = map(int, sys.stdin.readline().split())

    if a == 1:
        result.append(b)
    else:
        friend[a].append(b)
        friend[b].append(a)



# ArrayList < Integer > t = new ArrayList <> ();
# t = (ArrayList)result.clone();
#
# for (int i=0; i < result.size(); i++)
# {
# t.addAll(friend.get(result.get(i)));
# }
#
# ArrayList < Integer > r = new ArrayList <> ();
# for (int i=0; i < t.size(); i++)
# {
# if (!r.contains(t.get(i)))
# r.add(t.get(i));
# }
#
# System.out.println(r.size());
# }
# }