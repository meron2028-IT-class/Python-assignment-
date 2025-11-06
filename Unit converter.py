type = input("Enter conversion type. The types are: C2F, F2C, M2F, F2M): ")
number = float(input("Enter the value to convert: "))

def convert_units(type, number):
    
    if type == 'C2F':  
        result = (number * 9/5) + 32
        print(f"the value changed to fahrenheit is: {result}")
    elif convert_units == 'F2C':  
        result = (number - 32) * 5/9
        print(f"the value changed to Celsius is: {result}")
    
    elif type == 'M2F':  
        result = number * 3.28
        print(f"the value changed to feet is: {result}")
    
    elif type == 'F2M':  
        result = number / 3.28
        print(f"the value changed to meter is: {result}")
    
    else:
        print("Invalid conversion type! Please choose C2F, F2C, M2F, or F2M.")


convert_units(type, number)
