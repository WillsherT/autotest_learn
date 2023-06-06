# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
with open("test_file/task1_data.txt", "r", encoding='utf-8') as data_file:
    list_of_lines = data_file.readlines()
    for i in range(len(list_of_lines)):
        list_of_lines[i] = ''.join([ch for ch in list_of_lines[i] if not ch.isdigit()])

with open("test_file/task1_answer.txt", "w", encoding='utf-8') as answer_file:
    answer_file.writelines(list_of_lines)


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')