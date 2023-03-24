import random
a=input("Write names with seperated with comma: ")  #Aryan,Arya,Prince,Ayush,Arav,Sanjay,Geeta like that
names=a.split(",")
cd=len(names)
random_choice=random.randint(0,cd-1)
print(random_choice)
