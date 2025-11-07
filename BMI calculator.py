def BMI_calculator():
    weight_val = float(input("Tell me your weight(kg): "))
    height_val = float(input("Tell me your height(meter): "))
    BMI = round(weight_val/(height_val * height_val), 2)
    print(f"The result of your BMI is {BMI}")
    
    if BMI < 18.5:
        print("Your BMI is considered as Underweight")
    elif BMI <= 24.9:
        print("Your BMI is considered as Normal Weight")
    elif BMI <= 29.9:
        print("Your BMI is considered as Overweight")
    elif BMI >= 30:
        print("Your BMI is considered as Obese")
    
BMI_calculator()
    
