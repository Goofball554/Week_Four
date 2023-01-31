email = input("Please enter your email: ")

if len(email) > 10:
    if len(email) < 20:
        if "@" in email:
            print("This is a valid email.")
        
        else:
            print("This is not a valid email.")
    
    else:
        print("This is not a valid email.")

else:
    print("This is not a valid email.")