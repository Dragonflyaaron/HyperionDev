#save the string "The!quick!brown!fox!jumps!over!the!lazy!dog." as 'pangram'
#use the replace() function to swap '!' with blank spaces and overwrite variable
#print
# use the upper() function with print to reprint the sentence in uppercase
#use slicing with negative 1 to instruct the string to print in reverse order

pangram = "The!quick!brown!fox!jumps!over!the!lazy!dog."
pangram = (pangram.replace("!"," "))
print (pangram)
print (pangram.upper())
print (pangram[::-1])