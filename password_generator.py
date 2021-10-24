import random

pwd_length = int(input("Enter the length of the password : "))

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_case = "@#£_&/*!?~π$€¥<>~"
number_str ="1234567890"

p = lower_case + upper_case + special_case + number_str

password = "".join(random.sample(p,pwd_length))

print("Your password is :",password)