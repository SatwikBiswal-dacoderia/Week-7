def printing(L):
    for i in L:
        print(i, end=" ")

L = eval(input("Enter a List : "))

print("The elements of the list : ", end="")
printing(L)