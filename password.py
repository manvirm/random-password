import random

uppercaseLetter1 = chr(random.randint(65, 90))
uppercaseLetter2 = chr(random.randint(65, 90))

lowercaseLetter1 = chr(random.randint(97, 122))
lowercaseLetter2 = chr(random.randint(97, 122))

digit1 = random.randint(0, 9)
digit2 = random.randint(0, 9)

punctuationSign1 = chr(random.randint(123, 126))
punctuationSign2 = chr(random.randint(58, 64))

password_string = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + str(digit1) + str(digit2) + punctuationSign1 + punctuationSign2
password_list = list(password_string)

random.shuffle(password_list)
password = "".join(password_list)

print(password)