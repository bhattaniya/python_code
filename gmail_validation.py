# 'a-z'
# '0-9'
# '.' '-' , time 1
# '@' , time 1
# '.' , time 1 back place 2,3

import re
email_codition= "[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter Your Email : ")

if re.search(email_codition, user_email):
    print("valid email")
else:
    print ("invalid email ")