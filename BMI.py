name = input("Enter your name: ")
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi_calc = round((weight / (height ** 2)),1) # Calculate the bmi using formula. Round to one decimal place
print(name + " your BMI index is", bmi_calc)