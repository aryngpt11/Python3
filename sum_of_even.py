a=int(input("Enter the no: "))
t=0
for i in range(2,a,2):
    t+=i
print(t)

t1=0
for i in range(1,a):
    if i%2==0:
        t1+=i
print(t1)