# Чтение списка из строки
# input() - получение строки с клавиатуры
# split() - разделение строки на части по пробелам (возвращает список строк)
# map(int, input().split()) - применение к каждому элементу списка функции int
# list(...) - преобразование в список
nums = list(map(int, input().split()))
print(nums)