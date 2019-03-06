import time,random
response = ["yes","okay","ok","sure"]
characters = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
print ("Do you want a secure password??")
answer = input(">>")
answer.lower()

paslen = 8

if answer in response:
    print("let me make one for you...")
    time.sleep(4)
    print("Done!!")
    time.sleep(2)
    print ("" .join(random.sample(characters,paslen)))
    time.sleep(6)
else:
    print("Don't forget the importance of privacy...bye!!")
