# x: int = "Привет "
# y: int = " мир "
# # print(x + y)

# def summa(x1, x2):
#     print(x1 + x2)

# def summa2(x1: int, x2: int) -> int:
#     global x
#     res: int = x1 + x2
#     x = x + " алоха "
#     return res

# summa(8,12)
# print(summa2(7,13))
# print(summa2("hello ","world"))
# print(x)

# Напишите программу, которая принимает на вход 
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# str1 = 'a a a b c a a d c d d'
# a = ''
# str1 = str1.split(' ')
# for i in str1:
#     count1 = a.count(i)
#     # print(count1)
#     if a.count(i) == 0:
#         a += i+' '
#     else:
#         a += i+'_'+str(count1)+' '
# print(a.strip())

# sp = "a a a b c a a d c d d"
# new_list = sp.split()
# # print(new_list)
# new_ar = {}
# result = ""
# for i in new_list:
#     if i not in new_ar:
#         new_ar[i] = 0
#         result +=f"{i} "
#     else:
#         new_ar[i] += 1
#         result +=f"{i}_{new_ar[i]} "
# print(result)


# ___________________
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# sentense = "She sells sea shells on the sea shore The shells that she sells are sea "\
#     "shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# # lst = sentense.lower().split(' ')
# lst = sentense.replace(".", " ").lower().split()
# print(len(set(lst)))

# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента последовательности,
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”.
# Однако 2  друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание.
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих слайдах

# n = int(input('Введите число '))
# max_number = 1000
# while n != 0:
#    int(input('Введите число '))
#    if max_number > n:
#        max_number = n
# print(max_number)

# n = int(input('Введите число '))
# max_number = -1
# while n < 0:
#    int(input('Введите число '))
#    if max_number < n:
#        n = max_number
# print(n)

# max = 0
# while True:
#     n = int(input('Введите число '))
#     if n > max:
#         max = n
#     elif n == 0:
#         print(max)
#         break

# Вариант 2
# def max_num() -> int:
#     max_number: int = 0
#     while True:
#         n: int = int(input("Введите число: "))
#         if n == 0:
#             break
#         if n > max_number:
#             max_number = n
#     return max_number
# print(f"Максимальное значение  {max_num()} ")

# ДОП задача - Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать   как многочлен степени k.
# Пример: 
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint
# k = int(input('Введите натуральную степень k: '))
# a = randint(0, 100)
# b = randint(0, 100)
# print(f'{a}*x^{k} + {b}*x + 5 = 0')

# вариант 2 доделать

from random import randint
k = int(input('Введите натуральную максимальную степен: '))
sp = [randint(0,10) for _ in range(k+1)]
print(sp)
# [0,8,1,10] -> 8*x^2+x10=0