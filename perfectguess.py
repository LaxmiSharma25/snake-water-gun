import random

n = random.randint(1,100)
a = -1
guesses = 0
while(a != n):
    a = int(input("Enter a guess number: "))
    guesses += 1
    
    if(a<n):
        print("Higher number please!")

    elif(a>n):
        print("Lower number please!")
        
print(f"You have guessed the {n} correctly in {guesses} attempts")