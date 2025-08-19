# this program is for a password 
def password():
    try:
        key = input("enter the passord given ").upper()
        if key == "MR FRANK":
            print("Access Granted")
        else:
            print("Access denied ")
    except ValueError:
        print("This will not show in the terminal")

password()