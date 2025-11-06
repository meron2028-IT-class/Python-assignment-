# age classification function 
num = int(input("Enter your age please: "))

def classify_person(age):
    
    
    if num > 0 and num < 12 :
        print("You are a child!")
    elif num > 13 and num < 17 :
        print("You are a minor")
    elif num > 18 and num < 64 :
        print("You are an adult!")
    else:
        print("You are a senior.")
        
classify_person(num)
