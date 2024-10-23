a , b = map(int,input().split())
wr=a+b
days=a
if a<=0 and b<=0:
    print("0")
elif a==0 and b>7:
    print("0")
else:
    while wr>=7:
        add_choco=wr//7
        days+=add_choco
        wr=add_choco+wr%7

print(days)
