# циклы

# for i in range(0, 10):
#     print("*", end=' ')
# print()

# задание 1
# n = int(input("введите число 1-100:"))
# if n < 1 and n > 100:
#    print("error: число не кратно 3 и 5" )
# else:
#     if n % 3 == 0 and n % 5 == 0:
#         print("fizz buzz")
#     elif n % 3 ==0:
#         print("fizz")
#     elif n % 5 ==0:
#         print ("buzz")
#     else:
#         print(n)


        # задание 2

# base = input("Введите число: ")
# #
# #
# base = float(base)
# print("Выберите степень (0-7):")
# print(f"0: {base}^0 = {base ** 0}")
# print(f"1: {base}^1 = {base ** 1}")
# print(f"2: {base}^2 = {base ** 2}")
# print(f"3: {base}^3 = {base ** 3}")
# print(f"4: {base}^4 = {base ** 4}")
# print(f"5: {base}^5 = {base ** 5}")
# print(f"6: {base}^6 = {base ** 6}")
# print(f"7: {base}^7 = {base ** 7}")
#
# print()
#
#
# задание 3
# number = float(input("Введите число: "))
#
# print("Выберите степень для возведения:")
# print("0 - Нулевая степень")
# print("1 - Первая степень")
# print("2 - Вторая степень")
# print("3 - Третья степень")
# print("4 - Четвертая степень")
# print("5 - Пятая степень")
# print("6 - Шестая степень")
# print("7 - Седьмая степень")
#
# choice = int(input("Ваш выбор (0-7): "))
#
# if choice == 0:
#     result = number ** 0
#     print(f"{number} в степени 0 = {result}")
# elif choice == 1:
#     result = number ** 1
#     print(f"{number} в степени 1 = {result}")
# elif choice == 2:
#     result = number ** 2
#     print(f"{number} в степени 2 = {result}")
# elif choice == 3:
#     result = number ** 3
#     print(f"{number} в степени 3 = {result}")
# elif choice == 4:
#     result = number ** 4
#     print(f"{number} в степени 4 = {result}")
# elif choice == 5:
#     result = number ** 5
#     print(f"{number} в степени 5 = {result}")
# elif choice == 6:
#     result = number ** 6
#     print(f"{number} в степени 6 = {result}")
# elif choice == 7:
#     result = number ** 7
#     print(f"{number} в степени 7 = {result}")
# else:
#     print("Ошибка: выберите степень от 0 до 7")


# задание 4
# def calculate_salary(sales):
#     base_salary = 200
#     if sales < 500:
#         percentage = 0.03
#     elif 500 <= sales < 1000:
#         percentage = 0.05
#     else:
#         percentage = 0.08
#
#     bonus = sales * percentage
#     total_salary = base_salary + bonus
#     return total_salary
#
# print("Расчет зарплаты менеджеров")
# print("=" * 30)
#
# managers = []
# for i in range(3):
#     sales = float(input(f"Введите уровень продаж для менеджера {i + 1} ($): "))
#     managers.append(sales)
#
# print("\nРезультаты расчета зарплаты:")
# print("-" * 40)
#
# for i, sales in enumerate(managers, 1):
#     salary = calculate_salary(sales)
#     print(f"Менеджер {i}:")
#     print(f"  Продажи: ${sales:.2f}")
#     print(f"  Зарплата: ${salary:.2f}")
#     print(f"  (Базовая ставка: $200 + бонус: ${salary - 200:.2f})")
#     print()


# 16.09.25

# for i in range(5):
#    print(i)
#
# login = input("enter login:")
# password = input("enter login:")
#
# while login != "user" or password != "240624":
#        print("incorrent login or password")
#        login = input("enter login: ")
#        password = input("enter password: ")
# print("you are welcome")

# 1 задание: напечатайте все четные числа от 0 до 100
# for c in range(0, 100 +2, 2):
#     print(c)
# print("-" * 30)
# for c in range(0, 1001, 60):
#     print(c)
# print("-" * 30)
# for c in range(100, 0, -2):
#     print(c)
# print("-" * 30)

# 2 задание напечатайте эти же числа в обратном порядке
# for c in range(100-2, 0, 2):
#     print(c)
# print("-" * 30)
# for c in range(1001, 0, 60):
#     print(c)
# print("-" * 30)
# for c in range(0, 100+2, +2):
#     print(c)
# print("-" * 30)

# 3 задание пользователь вводит начало и конец диапозона, вывести все четные числа в данном диапозоне.

# num =int(input("enter number: "))
# for n in range(1 , 10+1):
#     print(f"{num} * {n} = {num * n}")
# print("-" * 30)
 # 4 задание пользователь вводит начало диапозона и конец, вывести все четные числа для этого диапазона
num = int(input("веди начало диапазона: "))
num = int(input("введи конец диапазона:"))
for w in range(num, num +1, 2):
    print(w)

    # цикл while
    # 1 задание напечатайте числа от 1 до 5
    x = 0
    while x < 6:
        print(x)
        x += 1
     # 2 задание найдите сумму чисел от 1 до 5
i = 1
sum = 0
while i <= 10:
    sum += i
    i += 1
print("-" * 30)
print(f"Сумма чисел от 1 до 10: {sum}")
