"""
contains Media class 
"""

class Creator: #might move to own file
    """represents author or director"""
    def __init__(self, name, year_of_birth):
        self.name = name
        self.year_of_birth = int(year_of_birth)

    def __str__(self):
        return f"{self.name} ({self.year_of_birth})"

class Media():
    """base class for all library media"""
    def __init__(self, title, year, creator, creator_dob, genre, date_added):
        self.title = title
        self.year = int(year)
        self.creator = Creator(creator, int(creator_dob))
        self.genre = genre
        self.date_added = date_added
    
class Book(Media):
    """Book type media class"""
    def __init__(self, title, year, creator, creator_dob, genre, date_added, pages, book_type):
        super().__init__(title, year, creator, creator_dob, genre, date_added)
        self.pages = int(pages)
        self.book_type = book_type
        self.media_type = "Book"

    def __str__(self):
        return f"Title: {self.title}, \nAuthor: {self.creator.name}, \nPublished: {self.year}, \nType: {self.book_type}, \nGenre: {self.genre}"
        

class AudioBook(Book):
    """AudioBook type media class"""
    def __init__(self, title, year, creator, creator_dob, genre, date_added,pages, book_type, duration, narrator):
        super().__init__( title, year, creator, creator_dob, genre, date_added, pages, book_type)
        self.duration = int(duration)
        self.narrator = narrator
        self.media_type = "AudioBook"

    def __str__(self):
        return f"Title: {self.title}, \nAuthor: {self.creator.name}, \nPublished: {self.year}, \nGenre: {self.genre},\nNarration By: {self.narrator}"
    
class Dvd(Media):
    """DVd type media class. I dont even own a dvd player."""
    def __init__(self, title, year, creator, creator_dob, genre, date_added, duration, features):
        super().__init__(title, year, creator, creator_dob, genre, date_added)
        self.duration = int(duration)
        self.features = features
        self.media_type = "Dvd"


    def __str__(self):
        return f"Title: {self.title}, \nDirector: {self.creator.name}, \nReleased: {self.year},\nGenre: {self.genre}, \nFeaturing: {", ".join(self.features)}"
    




    




 