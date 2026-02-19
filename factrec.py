#24331A05E3
#Factorial with recursion
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter n value:"))
print("Factorial is ",fact(n))
