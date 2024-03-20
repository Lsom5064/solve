s= int(input())

for i in range(s):
    x=0
    ps=input()
    for j in ps:
        if j=='(':
            x+=1
        else:
            x-=1
            if x<0: break
    print("YES" if x==0 else "NO")