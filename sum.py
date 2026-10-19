def add(n):
    if n==0:
        return 0
    else:
        return n + add(n-1)
n= int(input("Enter a number to calculate its sum: "))
answer = add(n)
print(f"The sum of first {n} natural numbers is {answer}")