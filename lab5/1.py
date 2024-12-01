class Book:
    title = None
    author = None
    year = None
    def get_info(self):
        print('Название книги:',self.title,',','Автор:',self.author,',','Год издания:',self.year)
book1 = Book()
book1.title = 'Мартин Иден'
book1.author = 'Джек Лоднон'
book1.year = 1909

book2 = Book()
book2.title = 'Горе от ума'
book2.author = 'Александр Грибоедов'
book2.year = 1825


