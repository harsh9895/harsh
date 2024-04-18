import random
secret_number = random.randint(1,100)

guess = int(input("enter Number: "))
i = 0
while i < 3:
if guess == secret_number:
    print("bingo")
elif guess > secret_number : 
    print("too high")
elif guess< secret_number:
    print("too low")
else:
    print("all good")

    print("thanks my lod for doing this program")
print(secret_number)
 i += 1
 print(i)
    