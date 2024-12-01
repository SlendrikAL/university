with open('example.txt', encoding='utf8') as file:
    content = file.read()
print(content)

with open('example.txt', encoding='utf8') as file:
    for line in file:
        print(line)

