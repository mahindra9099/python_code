### Strong password
### At least 8 characters
### At least 1 should be lowercase and uppercase
### Should include special characters

def password_gen(password):
    if len(password)<8:
        #print("in len")
        return False
    if not any(char.islower() for char in password):
        #print("in lower")
        return False
    if not any(char.isupper() for char in password):
        #print("in upper")
        return False
    if not any(char for char in password if char in '!@#%^&*()_'):
        print("In special")
        return False
    return True


result= password_gen("abjc_@fhhhzJh")
print(result)