def password_checker():
    while True:  # Keep asking until password is strong
        password = input("Enter a password: ")

        # Criteria checks
        has_upper = False
        has_lower = False
        has_digit = False

        # Loop through each character in the password
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True

        # Now check if all conditions are met
        if len(password) < 8:
            print("Password too short. Must be at least 8 characters.")
        elif not has_upper:
            print("Password must include at least one UPPERCASE letter.")
        elif not has_lower:
            print("Password must include at least one lowercase letter.")
        elif not has_digit:
            print("Password must include at least one number.")
        else:
            print("Strong password created successfully!")
            break  


password_checker()
