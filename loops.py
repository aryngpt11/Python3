'''fruits=["Apple","Peach","Pear"]
for i in fruits:
    print(i)'''
Stu=input("Enter the list of heights of students :").split()
for n in range(0,len(Stu)):
    Stu[n]=int(Stu[n])
print(Stu)


sum1=0
for i in Stu:
    sum1 +=i
print("Sum of the height of the stu are:" ,i)  

total_Stu=0
for j in Stu:
    total_Stu+=1
print(total_Stu)
avgheight=round(sum1/total_Stu)
print(avgheight)





  