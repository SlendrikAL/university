with open('user_input.txt','a',encoding='utf8') as file:
    inf = input('Введите текст')
    file.write(inf)