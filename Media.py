"""
contains Media class 
"""

class Creator: 
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
        return (
            f"Title: {self.title}\n"
            f"Author: {self.creator}\n"
            f"Published: {self.year}\n"
            f"Pages: {self.pages}\n"
            f"Type: {self.book_type}\n"
            f"Genre: {self.genre}"
        )
        

class AudioBook(Book):
    """AudioBook type media class"""
    def __init__(self, title, year, creator, creator_dob, genre, date_added,pages, book_type, duration, narrator):
        super().__init__( title, year, creator, creator_dob, genre, date_added, pages, book_type)
        self.duration = int(duration)
        self.narrator = narrator
        self.media_type = "AudioBook"

    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"Author: {self.creator}\n"
            f"Published: {self.year}\n"
            f"Genre: {self.genre}\n"
            f"Duration: {self.duration}min\n"
            f"Narration By: {self.narrator}"
        )
    
class Dvd(Media):
    """DVd type media class. I dont even own a dvd player."""
    def __init__(self, title, year, creator, creator_dob, genre, date_added, duration, features):
        super().__init__(title, year, creator, creator_dob, genre, date_added)
        self.duration = int(duration)
        self.features = features
        self.media_type = "Dvd"


    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"Director: {self.creator}\n"
            f"Released: {self.year}\n"
            f"Genre: {self.genre}\n"
            f"Duration: {self.duration}min\n"
            f"Featuring: {(self.features)}"
        )
    




    




 