import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

security_count = s.count("security")
bigdata_count = s.count("bigdata")

if security_count > bigdata_count:
    print("security!")
elif security_count < bigdata_count:
    print("bigdata?")
else:
    print("bigdata? security!")