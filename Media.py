class Creator: #might move to own file
    def __init__(self, name, year_of_birth):
        self.name = name
        self.year_of_birth = int(year_of_birth)

    def __str__(self):
        return f"{self.name} ({self.year_of_birth})"

class Media():
    def __init__(self, title, year, creator, creator_dob, genre):
        self.title = title
        self.year = int(year)
        self.creator = Creator(creator, int(creator_dob))
        self.genre = genre
    
class Book(Media):
    def __init__(self, title, year, creator, creator_dob, genre, pages, book_type):
        super().__init__(title, year, creator, creator_dob, genre)
        self.pages = int(pages)
        self.book_type = book_type


    def __str__(self):
        return f"Title: {self.title}, \nAuthor: {self.creator.name}, \nPublished: {self.year}, \nType: {self.book_type}, \nGenre: {self.genre}"
        

class AudioBook(Book):
    def __init__(self, title, year, creator, creator_dob, genre, pages, book_type, duration, narrator):
        super().__init__(title, year, creator, creator_dob, genre, pages, book_type)
        self.duration = int(duration)
        self.narrator = narrator

    def __str__(self):
        return f"Title: {self.title}, \nAuthor: {self.creator.name}, \nPublished: {self.year}, \nGenre: {self.genre},\nNarration By: {self.narrator}"
    
class Dvd(Media):
    def __init__(self, title, year, creator, creator_dob, genre, duration, features):
        super().__init__(self, title, year, creator, creator_dob, genre)
        self.duration = int(duration)
        self.features = features

    def __str__(self):
        return f"Title: {self.title}, \nDirector: {self.creator.name}, \nReleased: {self.year},\nGenre: {self.genre}, \nFeaturing:  {', '.join(self.features)}"
    

features = ["brand pitt", 'angelina jolie']

print(f"featuring: {', '.join(features)}")



    




 