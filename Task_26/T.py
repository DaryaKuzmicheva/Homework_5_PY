#Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#*Пример:*
##A = 2; B = 3 -> 8

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
def exponentiation(a, b):
    if b == 0:
        return 1
    else:
     return a *exponentiation(a, b - 1)
print(f"A в степени B = {exponentiation(a, b)}")


