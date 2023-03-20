# Рекурсия
# 1. Должно быть условие на выход из рекурсии

# Сумма чисел от 1 до n
def sum_seq(n):
    if n <= 0:
        return 0
    return n + sum_seq(n - 1)


print(sum_seq(10))