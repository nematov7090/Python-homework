#1
# def convert_cel_to_far(celsius: float) -> float:
#     fahrenheit = celsius * 9 / 5 + 32
#     return fahrenheit

# if __name__ == "__main__":
#     c = float(input("Enter temperature in Celsius: "))
#     f = convert_cel_to_far(c)
#     print(f"{c}°C is equal to {f}°F")
    

# def convert_far_to_cel(fahrenheit: float) -> float:
#        return (fahrenheit - 32) * 5 / 9

# if __name__ == "__main__":
#     f = float(input("Enter temperature in Fahrenheit: "))
#     c = convert_far_to_cel(f)
#     print(f"{f}°F is equal to {c:.2f}°C")

#2
# a = int(input("Boshlang'ich depozit miqdorini kiriting (dolar): $"))
# b = int(input("Yillik qaytish foizini kiriting (foizda): %"))
# c = int(input("Nechta yil davomida investitsiya qilishni istaysiz?: "))
# d = b / 100
# for a1 in range(1, c + 1):
#     a = a * (1 + d)
#     print(f"{a1}-Yil: ${a:.2f}")

# a = int(input("Dastlabki depozit miqdorini kiriting: $"))
# b = int(input("Yillik daromad stavkasini kiriting : "))
# c = int(input("Yillar sonini kiriting: "))
# d = b / 100
# for a1 in range(1, c + 1):
#     a = a * (1 + d)
#     print(f"{a1}-Yil: ${a:.2f}")
#########################################
# a = int(input("Boshlang'ich depozit miqdorini kiriting: $"))
# b = int(input("Yillik qaytish foizini kiriting: %"))
# c = int(input("Nechta yil davomida investitsiya qilishni istaysiz?: "))
# d = b / 100
# for year in range(1, c + 1):
#     a = a * (1 + d)
#     print(f"{year}-Yil: ${a:.2f}")
#########################################
# a = int(input("Boshlang'ich depozit miqdorini kiriting: $"))
# b = int(input("Yillik qaytish foizini kiriting: %"))
# c = int(input("Nechta yil davomida investitsiya qilishni istaysiz?: "))
# d = b / 100
# for a1 in range(1, c + 1):
#     a = a * (1 + d)
#     print(f"{a1}-Yil: ${a:.2f}")
########################################
# a = int(input("Boshlang'ich depozit miqdorini kiriting: $"))
# b = int(input("Yillik qaytish foizini kiriting: %"))
# c = int(input("Nechta yil davomida investitsiya qilishni istaysiz?: "))
# d = b / 100
# for a1 in range(1, c + 1):
#     a = a * (1 + d)
#     print(f"{a1}-Yil: ${a:.2f}")
########################################
# a = int(input("Boshlang'ich depozit miqdorini kiriting (dolar): $"))
# b = int(input("Yillik qaytish foizini kiriting (foizda): %"))
# c = int(input("Nechta yil davomida investitsiya qilishni istaysiz?: "))
# d = b / 100
# for a1 in range(1, c + 1):
#     a = a * (1 + d)
#     print(f"{a1}-Yil: ${a:.2f}")

# #3
# def main():
#     try:
#         n = int(input("Enter a positive integer: "))
#         if n <= 0:
#             print("Please enter a positive integer greater than 0.")
#             return
        
#         for i in range(1, n + 1):
#             if n % i == 0:
#                 print(f"{i} is a factor of {n}")
#     except ValueError:
#         print("That's not a valid integer. Please enter a positive integer.")

# if __name__ == "__main__":
#     main()

#4
# a = [
#     ["Toshkent Davlat Universiteti", 15000, 5000000],
#     ["Samarkand Davlat Universiteti", 12000, 4500000],
#     ["Urganch Davlat Universiteti", 10000, 4000000]
# ]
# for b in a:
#     ism = a[0]  
#     talabalar = a[1]  
#     oqish_tolovi = a[2]     
#     print(f"Universitet: {ism}")
#     print(f"Talabalar soni: {talabalar}")
#     print(f"Yillik o'quv xarajatlari: {oqish_tolovi} so'm")
#     print("-" * 30)

#########################################
# a = [
#     ["Toshkent Davlat Universiteti", 15000, 5000000],
#     ["Samarkand Davlat Universiteti", 12000, 4500000],
#     ["Buxoro Davlat Universiteti", 10000, 4000000]
# ]
# b = []  
# c = []  
# for a1 in a:
#     b.append(a1[1])  
#     c.append(a1[2]) 
# print("Talabalar soni:", b)
# print("O'quv xarajatlari:", c)
# universities = [
#     ["Toshkent Davlat Iqtisodiyot Universiteti", 15000, 5000000],
#     ["Samarkand Davlat Pedagogika Universiteti", 12000, 4500000],
#     ["Buxoro Davlat Tibbiyot Universiteti", 10000, 4000000]
# ]
# a = []  
# b = []  
# for university in universities:
#     a.append(university[1])  
#     b.append(university[2])  
# c = sum(a)
# d = sum(b)
# e = c / len(a)
# f = d / len(b)
# a.sort()
# g = len(a)
# if g % 2 == 1:
#     h = a[g // 2]
# else:
#     h = (a[g // 2 - 1] + a[g // 2]) / 2
# b.sort()
# q = len(b)
# if q % 2 == 1:
#     s = b[q // 2]
# else:
#     s = (b[q // 2 - 1] + b[q // 2]) / 2
# print(f"Umumiy talabalar soni: {c}")
# print(f"Umumiy o'quv xarajatlari: {d} so'm")
# print(f"Talabalar sonining o'rtachasi (mean): {e}")
# print(f"O'quv xarajatlarining o'rtachasi (mean): {f} so'm")
# print(f"Talabalar sonining mediani: {h}")
# print(f"O'quv xarajatlarining mediani: {s} so'm")
#########################################
# universities = [
#     ["Toshkent Davlat Iqtisodiyot Universiteti", 15000, 5000000],
#     ["Samarkand Davlat Pedagogika Universiteti", 12000, 4500000],
#     ["Buxoro Davlat Tibbiyot Universiteti", 10000, 4000000]
# ]
# a = []  
# b = [] 
# for c in universities:
#     a.append(c[1])  
#     b.append(c[2]) 
# d = sum(a)
# e = sum(b)
# f = d / len(a)
# g = e / len(b)
# a.sort()
# h = len(a)
# if h % 2 == 1:
#     j = a[h // 2]
# else:
#     j = (a[h // 2 - 1] + a[h // 2]) / 2
# b.sort()
# k = len(b)
# if k % 2 == 1:
#     l = b[k // 2]
# else:
#     l = (b[k // 2 - 1] + b[k // 2]) / 2
# print("*" * 30)
# print(f"Jami talabalar: {d:,}")
# print(f"Umumiy o'qish to'lovi $ {e:,.2f}")
# print()
# print(f"Talabalar soni bo'yicha o'rtacha qiymat: : $ {f:,.2f}")
# print(f"Talabalar o'rtacha: {j:,}")
# print()
# print(f"O'qish to'lovi: $ {g:,.2f}")
# print(f"Ta'lim o'rtacha: $ {l:,.2f}")
# print("*" * 30)









