from random import randint


function #1
def g_to_o (grams):
    ounces = 28.3495231 * grams
    return ounces

#2
def f_to_c (Fahrenheit):
    c = (5/9) * (Fahrenheit - 32)
    return c

#3
def solve (heads, legs):
    for chicken in range (heads + 1):
        rabbits = heads - chicken 
        if (chicken * 2 + rabbits * 4) == legs:
            return chicken, rabbits
    return None

#4
def prime(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

#7
def has(a):
    for i in range (len(a) - 1):
        if a[i] == 3 and a[i+1] == 3:
            return False
    return True

#9
def sphere (r):
    pi = 3.14159
    v = (4/3) * pi * (r**3)
    return v

#10
def remove_duplicates(input_list):
    unique_list = []
    for i in input_list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

#12
def histogram(v):
    for i in v:
        print('*' * i)
        
        #13
def guess_number():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret_num = randint(1, 20)
    guesses = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses += 1

        if guess < secret_num:
            print("Your guess is too low.")
        elif guess > secret_num:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break