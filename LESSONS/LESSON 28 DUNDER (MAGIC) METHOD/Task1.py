# Create a Book class with title and author attributes. 
# Implement __str__ so that print(my_book) outputs: "The Hobbit by J.R.R. Tolkien".

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

my_book = Book("The Hobbit","J.R.R. Tolkien")

print(my_book)
        
