tempUnit = input("Enter C for ferenheit to calcius coverter or Enter F for calcius to farenheit converter : ")
temp = float(input("Enter the temprature : "))

if tempUnit == "C":
    result = (temp-32)*(5/9)
    unit = "°C"
    print(f"{temp} F is equal to {round(result,3)} {unit}")
elif tempUnit == "F":
    result = (temp*9/5)+32
    unit = "F" 
    print(f"{temp} °C equal to {round(result,3)} {unit}")
else :
    print(f"{tempUnit} is not valid temp unit")