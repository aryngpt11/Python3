import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','@','$','*']
print("Welcome to password generator")
n_let=int(input("How many letters u want in ur pass: "))
n_symbol=int(input("how many symbols would u lioke:"))
n_numbers=int(input("how many nos would u lioke:"))
'''password =""
for i in range(n_let+1):
    #random_char=random.choice(letters)
    #print(random_char)
    #password +=random_char
    password+=random.choice(letters)
for i in range(n_symbol+1):
    password+=random.choice(symbols)
for i in range(n_numbers+1):
    password+=random.choice(numbers)
print(password)'''

pass_list=" "
for i in range(n_let+1):
    random
    pass_list.append(random.choice(letters))
for i in range(n_symbol+1):
    pass_list+=random.choice(symbols)
for i in range(n_numbers+1):
    pass_list+=random.choice(numbers)
print(pass_list)
random.shuffle(pass_list)
print(pass_list)