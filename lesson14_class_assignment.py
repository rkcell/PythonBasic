''' Task 1:
Create a class Book with the following attributes:
title (string)
author (string)
year (integer)
Then, add a method get_info() that returns a string containing all the information about the book.
'''

class Book:
    def __init__(self, title, author, year):
        self.title = str(title)
        self.author= str(author)
        self.year=int(year)

    def get_info(self):
        result = f"Title: {self.title} \nAuthor: {self.author} \n Year: {self.year}"
        return result



