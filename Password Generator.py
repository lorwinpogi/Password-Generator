import random
import string

def random_password(min_length, special_characters=True):  
    letters = string.ascii_letters
    #ascii contains all lower case and upper case letters
    special = string.punctuation

    characters = letters
    if special_characters:
        characters += special

    password = []

    # Ensure at least one special character if required
    if special_characters:
        password.append(random.choice(special))

    while len(password) < min_length:
        password.append(random.choice(characters))
    
    random.shuffle(password)
    
    return "".join(password)

# Example usage
password = random_password(12)
print(password)
