
score = 0

userName = input("Enter your name: ")

print(f"Welcome to the Star Wars Quiz, {userName}!")

print("1.Why is Obi Wan so OP?")
print("A) Because he has the high ground!")
print("B) Because he is a master of the Force!")
print("C) Because he has a lightsaber!")

userAnswer1 = input("Your answer (A, B, or C): ")

rightAnswer1 = "A"

if userAnswer1.upper() == rightAnswer1:
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"Your score is: {score}")