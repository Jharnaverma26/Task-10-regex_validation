import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def validate_mobile(mobile):
    pattern = r'^[6-9]\d{9}$'
    return re.match(pattern, mobile)

def validate_password(password):
    pattern = r'^(?=.\d)(?=.[@$!%*?&]).{8,}$'
    return re.match(pattern, password)

email = input("Enter your email: ")
mobile = input("Enter your mobile number: ")
password = input("Enter your password: ")

print("Email:", "Valid ✅" if validate_email(email) else "Invalid ❌")
print("Mobile:", "Valid ✅" if validate_mobile(mobile) else "Invalid ❌")
print("Password:", "Valid ✅" if validate_password(password) else "Invalid ❌")