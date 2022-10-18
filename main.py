import os.path

# Задание 3
ROOT_PATH = os.getcwd()
FILE_NAMES = ['1.txt', '2.txt', '3.txt']
lines = {}
for file_name in FILE_NAMES:
    full_path = os.path.join(ROOT_PATH, file_name)
    with open(full_path, encoding='utf-8') as f:
        counter = 0
        for line in f:
            counter += 1
        lines[file_name] = counter
# сортировка по количеству строк
sorted_list = sorted(lines.items(), key=lambda kv: kv[1])

OUTPUT_FILE = 'output.txt'
full_out_path = os.path.join(ROOT_PATH, OUTPUT_FILE)
# открыть файл для записи
with open(full_out_path, 'wt', encoding='utf-8') as f_output:
    # открыть все исходные файлы для чтения
    for file in sorted_list:
        full_path = os.path.join(ROOT_PATH, file[0])
        with open(full_path, encoding='utf-8') as f:
            # склеивать и выводить строки
            output = file[0] + '\n' + str(file[1]) + '\n'
            f_output.write(output)
            for line in f:
                f_output.write(line)
            f_output.write('\n')
