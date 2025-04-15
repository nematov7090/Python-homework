# a = float(input('Bitta son kiriting: '))
# b = round(a, 2)
# print(b)

########################

# a = input("birinchi raqamni kiriting:" )
# b = input("ikkinchi raqamni kiriting:" )
# c = input("uchinchi raqamni kiriting:" )
# katta = max(a, b, c)
# kichik = min(a, b, c)
# print(f"eng katta son {katta}")
# print(f"eng kichik son {kichik}")

#################################

# km = int(input("Enter distance in kilometers:"))
# print(f"{km} km = {km * 1000} in m = {km * 10000} in cm")

#####################################################

# num1 = float(input("birinchi sonni kiriting: "))

# num2 = float(input("ikkinchi sonni kiriting: "))
# a = num1 // num2
# print(a)

#####################################

# celsius = float(input("celsius haroratni kiriting: "))
# if celsius >= -273.15:
#     f = (celsius * 9/5) + 32
#     print(f"{celsius}°C ga teng {f}°F.")

##########################################

# num = int(input("raqam kiriting"))
# oxirgiraqam =num % 10
# print(num, oxirgiraqam)

################################
# a = input('Ismingizni kiriting: ')
# b = int(input('Tugilgsn yilingizni kiriting: ' ))
# c = 2025 - b
# print(f"{a}, sizning yoshingiz {c}da:")

###################################

# num1 = 12
# num2 = 12
# num3 = num1 == num2
# print(num3, num1, num2)

 #####################################

# import re
# car = ['Toyota', 'Ford', 'BMW', 'Tesla', 'Honda', 'Audi', 'Mercedes', 'Chevrolet', 'Nissan']
# def a(c, brand):
#     b = []
#     for brand in brand:
#         if re.search(r'\b' + re.escape(brand) + r'\b', c, re.IGNORECASE):
#             b.append(brand)
#     return b
# c = 'Men bugun yangi BMW va Tesla sotib oldim!'
# car_names = a(c, car)
# print(car_names)

#######################################

# a= input("Enter a string: ")
# print("Length of the string:", len(a))
# print("Uppercase:", a.upper())
# print("Lowercase:", a.lower())

##################################

# a = input("Enter a string: " )
# b = a.replace(" ","").lower()
# if b == b[::-1]:
#     print("String is a palindrome")
# else:
#     print("String is not a palindrome ")    

#########################################

# input_string = input("Matn kiriting: ")
# vowels = "aeiouAEIOU"
# vowel_count = 0
# consonant_count = 0

# for char in input_string:
#     if char.isalpha(): 
#         if char in vowels:
#             vowel_count += 1
#         else:
#             consonant_count += 1
# print(f"Vowels: {vowel_count}")
# print(f"Consonants: {consonant_count}")  

######################################

# a = input("asosiy matnni kiriting")
# b = input("qidirilayotgan matnni kiriting")
# if b in a:
#     print("qidirilayotgan matn asosiy matnda mavjud")
# else:
#     print("qidirilayotgan matn asosiy matnda mavjud emas.")

######################################

# a = input("bitta so'z kiriting")
# b = input("o'zgartirmoqchi bo'lgan so'zni kiriting")
# c = input("uning o'rniga qo'yiladigan so'zni kiriting")
# d = a.replace(b, c)          
# print("yangi so'z", d)

###################################

# a = input("matn kiriting: ")
# if len(a) > 0:
#     first_char = a[0]  
#     last_char = a[-1]   
#     print(f"Matnning birinchi belgisi: {first_char}")
#     print(f"Matnning oxirgi belgisi: {last_char}")
# else:
#    print("bo'sh bo'lmagan matn kiriting.")

########################

# a = input("bitta so'z kiriting: ")
# b = a[::-1]
# print("teskari so'z: ")
# print(b)

#############################
#10
# sentence = input("enter a sentence: ")
# words = sentence.split()
# word_count = len(words)
# print("The number of words in the sentence is:", word_count)

###############################
#11
# matn = input("Matn kiriting: ")
# raqam_bormi = False
# for belgi in matn:
#     if belgi.isdigit():
#         raqam_bormi = True
#         break
# if raqam_bormi:
#     print("Matnda raqam mavjud.")
# else:
#     print("Matnda hech qanday raqam yo'q.")

################################
# #12
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username != "" and password != "":
#     print("Login successful!")
# else:
#     print("username and password cannot be empty")    

#################################
#13

# user_input = input("Enter a string: ")
# no_spaces = user_input.replace(" ", "")
# print("String without spaces:", no_spaces)

###########################

# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")


# if string1 == string2:
#     print("The strings are equal.")
# else:
#     print("The strings are not equal.")

################################

# sentence = input("Enter a sentence: ")
# words = sentence.split()
# acronym = "".join(word[0].upper() for word in words)
# print("Acronym:", acronym)

###########################

# user_string = input("matn kiriting: ")
# character_to_remove = input("Enter a character remove: ")
# modified_string = user_string.replace(character_to_remove, "")
# print("Modified string:", modified_string)

#########################################

# a = input("Iltimos, matn kiriting: ")
# b = "aeiouAEIOU"
# c = ""
# for belgi in a:
#     if belgi in b:
#         c+= "*"
#     else:
#         c+= belgi
# print("unli harflar almashtirilgan matn:", c)

#######################################

# matn = input("matnni kiriting")
# boshlanish = input("matn qanday so'z bilan boshlanishi kerak")
# tugash = input("matn qanday so'z bilan tugashi kerak")
# if matn.startswith(boshlanish and matn.endswith(tugash)):
#     print("matn belgilangan so'z bilan boshlanadi va tugaydi")
# else:    
#     print("matn belgilangan so'z bilan boshlamaydi va tugamaydi")

#######################

# username = input("Enter your name: ").strip()
# password = input("Enter your name: ").strip()

# if username and password:
#     print("Login successful")
# else:
#     print("Error: Username and password cannot be empty.")    

####################################################

# num1 = float(input("birinchi raqamni kiriting: "))
# num2 = float(input("ikkinchi raqamni kiriting: "))
# if num1 == num2:
#     print("The number are equal. ")
# else:
#     print("The number are not equal.")    

##########################################

# number = int(input("Raqam kiriting"))
# if number > 0 and number % 2 == 0:
#     print("Number is positive and even. ")
# else:
#     print("Number is not positive and not even. ")
    
#################################

# num1 = float(input("birinchi raqamni kiriting: "))
# num2 = float(input("ikkinchi raqamni kiriting: "))
# num3 = float(input("uchinchi raqamni kiriting: "))

# if num1 != num2 and num1 != num3 and num2 != num3:
#       print("all numbers are different.")
# else:
#       print("some numbers are the same. ")
            
##################################

# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string:")
# if len(string1) ==len(string2):
#     print("The strings have the same length")
# else:
#     print("The strings don't have the same length.")

####################################

# number  = int(input("raqam kiriting: "))
# if number % 3 == 0 and number % 5 == 0:
#     print("the number is divisible by both 3 and 5.")
# else:
    
#     print("the number is not divisible by both 3 and 5.")

######################################

# num1 = float(input(" birinchi raqamni kiriting"))
# num2 = float(input(" ikkinchi raqamni kiriting"))
# total = num1 + num2
# if total > 50.8:
#     print("The sum is greater than 50.8.")
# else:
#     print("The sum is not greater than 50.8.")
