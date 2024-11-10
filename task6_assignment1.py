'''
შექმენით კლასი, სახელად Book.
კლასს კონსტრუქტორებად უნდა ჰქონდეს title, author, genre, availability=True.
კლასს უნდა ჰქონდეს 3 ფუნქცია:
1. check_availability, რომელიც დააბრუნებს მის ხელმისაწვდომობას.
2. borrow_book, რომელიც თუ ხელმისაწვდომია წიგნი, დაპრინტავს "წიგნი გატანილია!" და შესაბამისად,
წიგნი ხელმისაწვდომი აღარ უნდა იყოს. ხოლო თუ არ არის ხელმისავდომი, უნდა დაიპრინტოს "ეს წიგნი არ არის ხელმისაწვდომი!".
3. return_book, რომელმაც უნდა დაპრინტოს "წიგნი დაბრუნებულია!" და შესაბამისად, წიგნი ხელმისაწვდომი უნდა იყოს.
შექმენით Book კლასის ობიექტი და დატესტეთ თქვენი შექმნილი ფუნქციები.
'''

class Book:
    def __init__(self, title, author, genre, availability=True):

        self.title=title
        self.author=author
        self.genre =genre
        self.availability=availability

    def check_availability(self):
        return self.availability

    def borrow_book(self):
        if self.availability:
            print("წიგნი გატანილია!")
            self.availability=False
        else:
            print("ეს წიგნი არ არის ხელმისაწვდომი!")

    def return_book(self):
        print("წიგნი დაბრუნებულია!")
        self.availability=True

if __name__ == '__main__':
    abc_book=Book("ABC", "Vaja", "school")
    other_book=Book("Noname", "unknown", "unknown")
    print(abc_book.title, abc_book.author, abc_book.genre, abc_book.availability)
    print(other_book.title, other_book.author, other_book.genre, other_book.availability)
    print(abc_book.check_availability())
    abc_book.borrow_book()
    abc_book.borrow_book()
    print(abc_book.check_availability())
    abc_book.return_book()
    print(abc_book.check_availability())

