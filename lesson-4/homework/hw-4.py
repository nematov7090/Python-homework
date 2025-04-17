#1
# list1 = [1, 1, 2]
# list2 = [2, 3, 4]
# x1 = [a for a in list1 if a not in list2]
# x2 = [a for a in list2 if a not in list1]
# result = x1 + x2
# print(result)


# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# x1 = [a for a in list1 if a not in list2]
# x2 = [a for a in list2 if a not in list1]
# result = x1 + x2
# print(result)


# list1 = [1, 1, 2, 3, 4, 2]
# list2 = [1, 3, 4, 5]
# x1 = [a for a in list1 if a not in list2]
# x2 = [a for a in list2 if a not in list1]
# result = x1 + x2
# print(result)

#2
# n = 5

# for a in range(1, n):
#     print(a * a)

#3
# txt1 = 'hello'
# txt2 = (txt1[:3] + '_' + txt1 [3:])
# print(txt2)

# txt1 = 'assalom'
# txt2 = (txt1[:3] + '_' + txt1 [3:])
# print(txt2)

# txt1 = 'abcabcdabcdeabcdefabcdefg'
# txt2 = txt1.replace('abc', 'abc_')
# print(txt2)

#4
# import random
# secret_number = random.randint(1, 100)

# while True:
#     guess = int(input("Guess a number between 1 and 100: "))

#     if guess < secret_number:
#         print("Too low!")
#     elif guess > secret_number:
#         print("Too high!")
#     else:
#         print("Congratulations! You guessed the number!")
#         break

# import random

# secret_number = random.randint(1, 100)

# while True:
#     guess = int(input("Guess a number between 1 and 100: "))
    
#     if guess > secret_number:
#         print("Too high!")
#     elif guess < secret_number:
#         print("Too low!")
#     else:
#         print("Congratulations! You guessed the number!")
#         break

# import random
# son = random.randint(1, 100)
# for i in range(10):
#     taxmin = int(input(f"1 dan 100 gacha sonni toping (Qolgan urinishlar: {10 - i}): "))    
#     if taxmin == son:
#         print(f"You guessed it right in {i + 1} attempts!")
#         break
#     elif taxmin < son:
#         print("Xato! Siz kiritgan son kichikroq.")
#     else:
#         print("Xato! Siz kiritgan son kattaroq.")
# else:
#     print(f"You lost. Want to play again? (To'g'ri javob: {son})")

# import random
# son = random.randint(1, 10)
# for i in range(5):
#     taxmin = int(input("1 dan 10 gacha sonni toping: "))    
#     if taxmin == son:
#         print("To'g'ri topdingiz!")
#         break
#     else:
#         print("Xato. Qayta urinib ko'ring.")

# print("O'yin tugadi.")

# restart = input("Yana o'ynaysizmi? (Y/YES/y/yes/ok): ").strip().lower()
# if restart in ['y', 'yes', 'ok']:
#     print("O'yin yana boshlanmoqda...")
# else:
#     print("O'yinni tugatdingiz. Rahmat!")

#5
# password = input("Enter your password: ")
# if len(password) < 10:
#     print("Password is too short! Must be at least 8 characters.")
# elif password.isdigit() or password.isalpha():
#     print("Password should contain both letters and numbers.")
# else:
#     print("Password looks good!")

# password = input("Enter your password: ")

# if len(password) < 8:
#     print("Password is too short.")
# else:
#     print("Password accepted.")

# a = input("parol kiriting: ")

# if not any(char.isupper() for char in a):
#     print("parolda katta harf bo'lishi kerak.")
# else:
#     print("parol qabul qilindi.")

# password = input("Enter your password: ")

# if len(password) < 8:
#     print("Password is too short.")
# elif not any(char.isupper() for char in password):
#     print("Password must contain an uppercase letter.")
# else:
#     print("Password is strong.")

#6
# for num in range(2, 101):
#     is_prime = True 
    
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break  
    
#     if is_prime:
#         print(num)

