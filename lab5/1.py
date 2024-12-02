class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return ('Название книги:',self.title,',','Автор:',self.author,',','Год издания:',self.year)

book1 = Book('Мартин Иден','Джек Лоднон',1909)
book2 = Book('Горе от ума','Александр Грибоедов',1825)

print(book1.get_info())
print(book2.get_info())
