import random 
import string

# Generate a key 20 characters

numbers = ''.join(str(random.randint(0,9)) for _ in range(2))
letters = ''.join(random.choices(string.ascii_letters, k=3))

numbers1 = ''.join(str(random.randint(0,9)) for _ in range(3))
letters1 = ''.join(random.choices(string.ascii_letters, k=6))

numbers2 = ''.join(str(random.randint(0,9)) for _ in range(3))
letters2 = ''.join(random.choices(string.ascii_letters, k=3))

key = numbers + letters + numbers1 + letters1 + numbers2 + letters2

print(key)
