from random import choice, shuffle, randint

#
# This will generate a 12 character password with 8 letters LC 1 UC 1 number and 1 special character
# It will be better to generate a 12 character password but random number of uc, lc, number, spl character
#

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
special_chars=['!','#','$','%','&','(',')','*','+']
password_letters=[]
password=""
for i in range(0,9):
    password_letters.append(choice(letters))
password_letters.append(choice(letters).upper())
password_letters.append(choice(numbers))
password_letters.append(choice(special_chars))
shuffle(password_letters)
password = "".join(password_letters)
print(password)