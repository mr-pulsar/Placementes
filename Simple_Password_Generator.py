import random
Alphabet='QWERTYUIOPLKJHGFDSAZXCVBNM'
Numeric='1234567890'
Symbols='@#$%^&*()_+=-<>?:"\][]'
length=16
password=Alphabet+Numeric+Symbols
print("".join(random.sample(password, length)))