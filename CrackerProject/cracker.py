import random
import hashlib
import numpy as np


# the password generator generates 'n' number of random passwords. The passwords can be of two types, strong or weak.
# strong passwords are made up of a combination of at least one capital letter, small letter, number and a special character.
# weak passwords do not cater to all the above conditions.
# all passwords are at least 6 characters in length and at max 20 characters in length.

# 33 - 47 and 58 - 64 and 91 - 96 and 123 - 126: special characters
# 48 - 57 : numbers 
# 65 - 90 : capital letters
# 97 - 122 : small letters

special = [i for i in range(33,48)]
special.extend([i for i in range(58,65)])
special.extend([i for i in range(91,97)])
special.extend([i for i in range(123,127)])

numbers = [i for i in range(48,58)]
capital = [i for i in range(65,91)]
small = [i for i in range(97,123)]


def get_random_number():
    return chr(numbers[np.random.randint(low = 0, high = len(numbers), size = 1)[0]])

def get_random_small():
    return chr(small[np.random.randint(low = 0, high = len(small), size = 1)[0]])

def get_random_capital():
    return chr(capital[np.random.randint(low = 0, high = len(capital), size = 1)[0]])

def get_random_special():
    return chr(special[np.random.randint(low = 0, high = len(special), size = 1)[0]])


def print_dict(d):
    for each in d.keys():
        print(each, end = ": ")
        print(d[each])

def generate_strong_password(size = 8):
    num = get_random_number()
    small = get_random_small()
    cap = get_random_capital()
    spec = get_random_special()

    out = np.random.randint(low = 33, high = 127, size = size-4) 
    
    pwd = num + small + cap + spec 

    for each in out:
        pwd = pwd + chr(each)

    pwd = ''.join(random.sample(pwd, len(pwd)))
    return pwd

    
def generate_weak_password(size = 8):
    rand =  np.random.randint(low = 0, high = 4, size = 3)
    pwd = ""
    while len(pwd) < size: 
        rand2 = np.random.randint(low = 0, high = 3, size = 1)
        if rand[rand2][0] == 0:
            pwd = pwd + get_random_capital()
        elif rand[rand2][0] == 1:
            pwd = pwd + get_random_number()
        elif rand[rand2][0] == 2:
            pwd = pwd + get_random_small()
        else :
            pwd = pwd + get_random_special()
    return pwd

def check_pass_word_type(password): # returns 0 for a weak password and returns 1 for a strong password
    arr = [0 for i in range(4)]
    i = 0
    while i < len(password):
        if ord(password[i]) in special:
            arr[0] = 1
        elif ord(password[i]) in numbers:
            arr[1] = 1
        elif ord(password[i]) in capital:
            arr[2] = 1
        elif ord(password[i]) in small:
            arr[3] = 1
        else :
            return -1 # invalid password
        i = i + 1
    for each in arr :
        if each == 0:
            return 0
    return 1

def generate_password_dict(num_strong = 10, num_weak = 10):
    passwords = {}
    
    i = 0
    while i < (num_strong):
        _ = generate_strong_password()
        if _ not in passwords.keys():
            passwords[_] = hashlib.md5(_.encode("utf-8")).hexdigest()
            i = i + 1
    i = 0
    while i < (num_weak):
        _ = generate_weak_password()
        if _ not in passwords.keys():
            passwords[_] = hashlib.md5(_.encode("utf-8")).hexdigest()
            i = i + 1

    return passwords

def save_dictionary(dic):
    f = open("weak_passwords.txt", "w")
    for each in dic.keys():
        if check_pass_word_type(each) == 0:
            f.write(each)
            f.write("\n")
    f.close()
    f = open("strong_passwords.txt", "w") 
    for each in dic.keys():
        if check_pass_word_type(each) == 1:
            f.write(each)
            f.write("\n")
    f.close() 
    return 1

def load_dictionary(path):
    f = open(path, "r")
    d = {}
    for each in f :
        each = each[:-1]
        if check_pass_word_type(each) in [0,1]:
            d[each] = hashlib.md5(each.encode("utf-8")).hexdigest()
    f.close()
    return d

def add_password_to_dict(dic, password):
    if check_pass_word_type(password) == -1:
        print("Invalid password!")
        return -1
    if password in dic.keys():
        print("Password already exists!")
        return -1
    dic[password] = hashlib.md5(password.encode("utf-8")).hexdigest()
    return 1

def analyze_dic(dic):
    strong_pass = 0
    weak_pass = 0
    invalid_pass = 0
    
    for each in dic.keys():
        if check_pass_word_type(each) == 1:
            strong_pass = strong_pass + 1
        elif check_pass_word_type(each) == 0 :
            weak_pass = weak_pass + 1
        else :
            invalid_pass = invalid_pass + 1
    print("The dictionary contains: ")
    print(strong_pass, " strong passwords")
    print(weak_pass, " weak passwords")
    print(invalid_pass, " invalid passwords")
    return 1

def crack_pass_using_dic(dic, inp):
    for each in dic.keys():
        if dic[each] == inp:
            return (1, each)
    return (0, "No match found")



strong_pass = generate_strong_password()
weak_pass = generate_weak_password()
print(strong_pass)
print(weak_pass)

print(check_pass_word_type(strong_pass))
print(check_pass_word_type(weak_pass))

d = generate_password_dict()
print_dict(d)
print(save_dictionary(d))

b = load_dictionary("strong_passwords.txt")
print_dict(b)

new_d = {}
print(add_password_to_dict(new_d, "ThisIs_AStrongPassw0rd"))
print_dict(new_d)

analyze_dic(new_d)
analyze_dic(d)

