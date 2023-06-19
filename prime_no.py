def prime_checker(number):
    is_prime=True
    for i in range(2,number):
        if number%i==0:
            is_prime=False
    if is_prime:
        print("It is a prime")
    else:
        ("Not a prime")
n=int(input("Enter trhe number: "))
prime_checker(number=n)
