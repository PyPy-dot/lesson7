def custom_write(file_name: str, strings: list) -> dict:
    file_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for ind, string in enumerate(strings):
            file_positions[(ind + 1, file.tell())] = string
            file.write(string + '\n')
    return file_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
