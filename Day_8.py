'''def greet():
    print("Hello")
    print("How are you")
    print("Where do you live")
greet()'''
#function that allow for the input

'''def greet1(name):
    print(f"Hello {name}")
    print(f"How are you {name}")
    print("Where do you live")
greet1("Arya" )'''


#function with more than one input
'''def greet_with(name, address):
    print(f"Hello {name}")
    print(f"what u like in {address} ")
greet_with("Riya","Delhi")'''

#Keyword Argument

def greet_with(name, address):
    print(f"Hello {name}")
    print(f"what u like in {address} ")
#greet_with(name="Riya",address="Delhi")
greet_with(address="Delhi",name="Riya")
