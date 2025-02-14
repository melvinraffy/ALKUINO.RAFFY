class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")


book1 = Book("Robinson Crusoe", "Daniel Defoe", 1719)
book2 = Book("Gulliver's Travels", "Jonathan Swift", 1726)
book3 = Book("The Pilgrim's Progress", "John Bunyan", 1678)


book1.describe()
print()  
book2.describe()
print()  
book3.describe()