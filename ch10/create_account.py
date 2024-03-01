from ast import While



def main():
    full_name = get_full_name()
    print()

    email = get_email()

    password = get_password()
    print()
    
    phone = get_phone()
    
    first_name = get_first_name(full_name)  
    display_phone = get_phone_display(phone) 
    print(f"Hi {first_name}, thanks for creating an account.")  
    print(f"Your registered email is {email}, and phone number is {display_phone}.")
    print(f"You will recieve a confirmation via email and text... you can reply 'stop'"
           "via text if you do not want to recieve notifications via text.")
    print(f"Have a nice day !!!")           
    
def get_full_name():
    while True:
        name = input("Enter full name:  ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")
            
def get_email():
    while True:
        email = input("Enter email address:  ").strip()
        if email.find(" ") != -1: ## if it is not = -1 that means it found a space
            print("Email cannot include spaces")
        elif email.find("@") == -1  and email.find(".com") == -1: ## if it is -1 then it could not find @ or .com
            print("Email must include '@' and '.com'") 
        else:
            return email
        
def get_phone():
    while True:
        temp_phone = input("Enter phone number, must be 10 digits:  ").strip()
        phone = ""
        for i in temp_phone:
            if i.isdigit() == True:
                phone += i
        
        if phone.isdigit() and len(phone) == 10:
            return phone
        else:
            print("Phone number must be 10 digits only or seperated by () or -")

def get_phone_display(phone: str):
    count = 0
    phone_display = ""
    for i in phone:
        if count == 3 or count == 6:
            phone_display += "."
        phone_display += i
        count += 1
    return phone_display
        


def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name
    
def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:  ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print(f"Password must be 8 characters or more \n"
                  f"with at least one digit and one uppercase letter.")
        else:
            return password
        
if __name__ == "__main__":
    main()
