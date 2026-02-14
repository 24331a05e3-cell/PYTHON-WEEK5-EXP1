#24331A05E3
#factorial using without recursion
n=int(input("enter n number:"))
res=1
for i in range(n,0,-1):
    res=res*i
print("factorial is:",res)
