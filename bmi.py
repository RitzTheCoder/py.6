h=float(input("Enter your height in cm:"))
w=float(input("Enter your height in kg:"))
BMI = w/(h/100)**2
print("Your BMI is",BMI)
if BMI <= 18.4:
    print("You are Underweight") 
elif BMI <= 24.9:
    print("You are Healhty") 
elif BMI <= 29.9:
    print("You are Overweight")
elif BMI <= 34.9:
    print("You are Severly Overweight")            
elif BMI <= 39.9:
    print("You are Obese")    
else:
    print("You are severly obese")    