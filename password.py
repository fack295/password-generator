import random
import string
# generate password
def generate_password(length,spacification_password):
    if spacification_password in ["s","S"]:
        characters = string.ascii_letters
    elif spacification_password in ["d","D"]:
        characters = string.digits
    elif spacification_password in ["sd","SD","Sd","sD"]:
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
# check password
def check_password(password):
    z = password.isalpha()
    x = password.isdigit()
    y = password.isalnum()
    if x == True and z == False or x == False and z == True:
        print("Weak (Easy to guess)")
    elif len(password) < 8:
        print("Weak (To short)")
    elif y == True:
        print("Medium (Good, but cout be better)")
    else:
        print("Strong (Excellent,Vary hard to guess ")
# main
print("Password")
# input
length = int(input("Enter password length: "))
spacification_password = input("Enter S for only string password:\nEnter D for only digit password:\nEnter SD for only digit+latter password :\nPress Enter for strong passwod: ")
password_no = int(input("How many password requered: "))
# no of passwords
for n in range(password_no):
    print(f"Generated Password {n + 1}:{generate_password(length,spacification_password)}")
    password =generate_password(length,spacification_password)
    #check password week or strong
check = input("for chacking password strong or week enter (Y/N)")
if check in ["y","Y","yes","YES","Yes"]:
    check_password(password)
