#create variables to use as counters
#set the range needed to work within 

row = 1
new_row = 5

#two variables, one for counting forwards and one for backwards

for i in range (1,10):
    if row <5: 

        #making sure our loop stops counting at 5
        #taking into consideration range always starts at zero

        print("* "*row)
        row = row+1
    
    #entering the second conditional onece the count has reached 5

    else:
        print ("* "*new_row)
        new_row = new_row -1