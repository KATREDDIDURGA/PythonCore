import random
n = 20
# generate random number between 0 and 20
to_be_guessed = int(n*random.random()+1)
guess = 0
while guess != to_be_guessed:
    guess = int(input("new Number"))
    if guess > 0:
        if guess > to_be_guessed:
            print("number too large")
        elif guess < to_be_guessed :
            print("number too small")
    else:
        print('sorry')
        break
else:
    print("congrats")

