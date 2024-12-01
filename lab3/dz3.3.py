try:
    with open('abc.txt',encoding='utf8') as file:
        print(file.read())
except FileNotFoundError:
    print('Файла не существует')
