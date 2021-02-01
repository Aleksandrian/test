#  Задание 2(продолжение функций 6)
# def palindrom(c):
#   if len(c) < 1:
#        return True
#    else:
#      if c[0] == c [-1]:
#           return palindrom(c[1:-1])

# n = str(input('write phrase: '))
# if palindrom(n) == True:
#    print('palindrom!')
# else:
#   print('is not a palindrome!')


# Задание 3(продолжение функций 6)

# def func_step(n):
#   if n <= 1:
#     return n
# else:
#   return func_step(n - 1) + func_step(n - 2)
# print(func_step(3))


# Задание 1(списки)
# sn = list(map(int,input('write the list with a space after the end press enter:').split()))
# summ=0
# for i in sn:
#    summ=summ+i
# print('сумма всех значений:',summ)
# print('минимальное значение:',min(sn))
# print('максимальное значение:',max(sn))
# print('среднее значение:', summ/len(sn))

# Задание 3(списки)
# def func_ser():
#   summ = 0
# for h in b:
#    return summ + h

# def func_proiz():
#    i = 0
# for k in b:
#    return ((i + k) / len(b))


# sn = list(map(int,input('write the list with a space after the end press enter:').split()))
# b = []
# for steps in sn[1:6]:
#   d = 2
#  if steps == 1:
#   pass
# elif steps <3:
#     b.append(steps)
# elif steps != d:
#   while not steps == d:
#        d = d + 1
#        if not steps % d and steps != d:
#             break
#          elif not steps % d and steps == d:
#               b.append(steps)
# print(b)

# l = input('рассчитать среднее или производную?(s/p)')
# if l == 'p':
#  print(func_proiz())

# else:
# print(func_ser())

# Задание 2(списки)
s = int(input('write the number of steps'))
v = []
for i in range(0, s + 1):
    for n in range(0, s + 1):
        if (2 * i) + n == s:
            v.append(n)
            v.append(i)
print(v)

