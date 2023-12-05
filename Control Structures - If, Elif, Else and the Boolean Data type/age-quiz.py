age = input("How old are you? ") #collect users age
age = int(age) #resave as an integer variable
if age >= 100: #start with the highest number for the if block to check first and go descending order
    print ("Sorry you're dead.") #print if equal to or greater
elif age >= 65: 
    print ("Congrats on your retirement!") #if equal to or greater but less than 100
elif age >= 40:
    print ("You're over the hill") #print if equal or greater to but less than 65
elif age == 21:
    print ("Congrats on your 21st!") #print only if exactly 21
elif age < 13:
    print ("You qualify for the kiddie discount") #print if less than 13 only
else:
    print ("Age is but a number") #print for every other number