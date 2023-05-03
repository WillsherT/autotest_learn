# Задание 1: Получить периметр, площадь и диагональ квадрата.
square_side = 5

p_of_square = square_side * 4
s_of_square = square_side ** 2
d_of_square = 2 ** 0.5 * square_side

print('Ответ к заданию 1:')
print('Периметр = ' + str(p_of_square))
print('Площадь = ' + str(s_of_square))
print('Диагональ = ' + str(d_of_square), '\n')

# Задание 2: Найти корни квадратного уравнения имеющего положительный дискриминант.
a = 1
b = 2
c = 3
D = 123

x1 = (-b + D ** 0.5) / (2 * a)
x2 = (-b - D ** 0.5) / (2 * a)

print('Ответ к заданию 2:')
print(f'Первый корень: {round(x1, 2)}, Второй корень: {round(x2, 2)} \n')

# Задание 3: Сложить две строки разделив их пробелом и поменяв два первых символа каждой строки местами
string1 = 'первая строка'
string2 = 'вторая строка'

new_string1 = string2[:2] + string1[2:]
new_string2 = string1[:2] + string2[2:]

print('Ответ к заданию 3:')
print(new_string1 + ' ' + new_string2 + '\n')

# Задание 4: Вывести название файла, имя диска и корневую папку имея полный путь с расширением
path_to_file = r'C:\lessons\first_lesson.txt'

index_of_filename_start = path_to_file.rfind('\\') + 1
index_of_filename_end = path_to_file.rfind('.')
filename = path_to_file[index_of_filename_start:index_of_filename_end]

index_of_disc_name_end = path_to_file.find(':')
disc_name = path_to_file[:index_of_disc_name_end]

index_of_main_folder_start = path_to_file.find('\\') + 1
path_without_disk = path_to_file[index_of_main_folder_start:]
index_of_main_folder_end = path_without_disk.find('\\')
main_folder_name = path_without_disk[:index_of_main_folder_end]

print('Ответ к заданию 4:')
print('Имя файла: ' + filename)
print('Диск: ' + disc_name)
print('Корневая папка: ' + main_folder_name, '\n')

# Задание 5: Включить сумму и произведение двух чисел внутрь строки используя форматирование
a = 5
b = 7

result_5 = f"""Сумма чисел: a + b = {a + b}
Произведение чисел: a * b = {a * b}
"""

print('Ответ к заданию 5:')
print(result_5, '\n')

# Задание 6: Удаление символов с НЕчетным индексом из строки
string = 'Строка без символов с нечетным индексом'

result_6 = string[::2]

print('Ответ к заданию 6:')
print(result_6, '\n')

# Задание 7: Найти срез минимальной длины из символов из первой строки встречающихся во второй
first_string = 'wtf'
second_string = 'сwm fjord bank glyphs vext quiz'

index_of_first = second_string.find(first_string[0])
index_of_second = second_string.find(first_string[1])
index_of_third = second_string.find(first_string[2])

start_slice = min(index_of_first, index_of_second, index_of_third)
end_slice = max(index_of_first, index_of_second, index_of_third)

result_7 = second_string[start_slice:end_slice + 1]

print('Ответ к заданию 7:')
print(result_7 + '\n')
