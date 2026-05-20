#compound intrest calculator
import math

p = intial_amt = int(input("Enter your intial amount: "))
r = int_rate = int(input("Enter your intrest rate per year: "))
t = duration = int(input("Enter your time period for intrest(in year):"))

compund_interest = p*pow((1+r/100),t)

print(f"Your amount is {compund_interest}")