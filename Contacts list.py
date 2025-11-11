Contacts = []

while True:
    Feature_choose = int(input("Press 1 if you want to add contacts, press 2 to view contacts, press 3 to remove contacts, choose 4 to leave the program: "))
    if Feature_choose == 1:
        new_contact = input("Name of the contact: ")
        Contacts.append(new_contact)
        print(f"Your contacts are now {Contacts}")
    elif Feature_choose == 2:
        print(Contacts)
    elif Feature_choose == 3:
        remove_contact = input("Contact you want to remove: ")
        Contacts.remove(remove_contact)
        print(f"Your current contacts are {Contacts}")
    elif Feature_choose == 4:
        break
    else:
        print("Please enter numbers only from 1-3")
    
