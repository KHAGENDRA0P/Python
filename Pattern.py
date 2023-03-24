N = int(input())
i = 1
while i<=N:
    spaces = 1
    while spaces<=N-i:  
        print(" ",end="")
        spaces=spaces+1

    val = i
    cnt = 1
    while cnt<=i:
        print(val,end="")
        val=val+1
        cnt=cnt+1

    val=val-2
    cnt=1
    while cnt<=i-1:
        print(val,end="")
        val=val-1
        cnt=cnt+1
    
    print()
    i=i+1