def verify_for_lower(password):
    for i in password:
        if(ord(i) >= 65 and ord(i) <= 90):
              return 0
    return 1

def verify_for_upper(password):
    for i in password:
        if(ord(i) >= 97 and ord(i) <= 120):
              return 0
    return 1

def verify_for_three_in_a_row(password):
    for i in range(len(password)-2):
        if password[i] == password[i+1] == password[i+2] :
             return 1
    return 0

def verify_for_consecutiv_number(password):
    for i in range(len(password)-1):
        if password[i].isdigit() and password[i+1].isdigit() :
            if int(password[i]) == int(password[i+1]) - 1:
                return 1
    return 0

def verify_for_special_characters(password):
    for i in password:
        if i == "~" or i == "`" or i == "!" or i == "@" or i == "#" or i == "$" or i == "%" or i == "^" or i == "&" or i == "*" or i == "(" or i == ")" or i == "-" or i == "_" or i == "+" or i == "=" or i == "{" or i == "}" or i == "[" or i == "]" or i == "|" or i == "\ " or i == ";" or i == ":" or i == "<" or i == ">" or i == "," or i == "." or i == "/" or i == "?":
               return 0
    return 1

def  verify_for_number_of_char(password):
    if len(password) > 8 and len(password) < 20:
        return 0
    elif len(password) > 20:
        return len(password) - 20
    else:
        return 8 - len(password)
    
password = input("Input: ")
nr_of_corrections = 0
nr_char = verify_for_number_of_char(password)
nr_of_corrections += nr_char
k = verify_for_special_characters(password)  
if nr_of_corrections == 0:
    nr_of_corrections += k
k = verify_for_three_in_a_row(password)
nr_of_corrections += k
k = verify_for_upper(password)
if nr_char == 0:
    nr_of_corrections += k
k = verify_for_lower(password)
if nr_char == 0:
    nr_of_corrections += k
k = verify_for_consecutiv_number(password)
nr_of_corrections += k
if nr_of_corrections == 0:
    print("good")
else:
    print(nr_of_corrections)
