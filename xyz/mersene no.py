n=int(input("Enter the value of n:"))
u=2**n-1
m=u*u
print("Mersenne number:",u)
if u==1 or u==0:
     prime=2
else:
for i in range(u+1,0):
c=0
for j in range(2,i):
if i%j==0:
     c=1
if c==0:
   prime=i
   break
   print("Next prime number",prime)
