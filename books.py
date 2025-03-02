class books:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.rating = 0

    def book_title(self, title):
        self.title = title
        return title

    def book_author(self, author):
        self.author = author
        return author
    
    def book_rating(self, rating):
        self.rating = rating
        return rating
    
    def book_inputs(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating
        
        self.book_title(title)
        self.book_author(author)
        self.book_rating(rating)
        
        return {
            'title': self.title,
            'author': self.author,
            'rating': self.rating
        }

    
