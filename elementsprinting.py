def printing(L,i):
    i=0
    if i==len(L):
        return
    print(L[i], end=" ")
    printing(L,i+1)