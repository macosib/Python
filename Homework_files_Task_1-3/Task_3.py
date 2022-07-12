import os

file_path_1 = os.path.join(os.getcwd(), '1.txt')
file_path_2 = os.path.join(os.getcwd(), '2.txt')
file_path_3 = os.path.join(os.getcwd(), '3.txt')
file_path_result = os.path.join(os.getcwd(), 'result.txt')

with open(file_path_1, encoding='UTF-8') as text_file_1, \
        open(file_path_2, encoding='UTF-8') as text_file_2, \
        open(file_path_3, encoding='UTF-8') as text_file_3, \
        open(file_path_result, 'w', encoding='UTF-8') as result_file:
    result = []

    for text in [text_file_1, text_file_2, text_file_3]:
        data = [os.path.basename(text.name)]
        count = 0
        for row in text.readlines():
            count += 1
            data.append(row.rstrip())
        data.insert(1, str(count))
        result.append(data)

    for text in sorted(result, key=len):
        for row in text:
            result_file.write(row + '\n')
