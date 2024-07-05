# Instructions
# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.

n= int(input("What number would you like to check for being a prime number or not? "))

def prime_checker(number=n):
    prime_number = True
    for i in range (2, number):
        if number % i ==0:
            prime_number = False
    if prime_number:
            print("It's a prime number. ")
    else:
            print("It's not a prime number.")

prime_checker()

