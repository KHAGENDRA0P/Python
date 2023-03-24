def largestnumber():
    A = int(input())
    B = int(input())
    C = int(input())
   
    if A>=B and B>=C:
        print(A,"is Largest")
    return

    if B>=A and B>=C:
        print(B,"is Latgest")
    return

else:
    print(C,"Is Largest")
    return

largestnumber()