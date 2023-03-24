a=input("Enter the list of the score of the student: ").split()
for n in range(0,len(a)):
    a[n]=int(a[n])
print(a)
maxx=0
for j in a:
    if j>maxx:
        maxx=j
print(maxx)

