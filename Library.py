import csv
import os
from Media import *

class Library:
    def __init__(self,file_name):
        self.library_contents = self.load_library_from_csv(file_name)
        self.file_name = file_name
    
    def media_maker(row):
        media_type = row["type"]
        if media_type == "Book":
            return Book(row["title"], int(row["year"]), row["creator"], row["creator_dob"], row["genre"], row["pages"], row["book_type"])
        elif media_type == "AudioBook":
            return AudioBook(row["title"], int(row["year"]), row["creator"], row["creator_dob"], row["genre"], row["duration"], row["narrator"])
        elif media_type == "Dvd":
            return Dvd(row["title"], int(row["year"]), row["creator"], row["creator_dob"], row["genre"], row["duration"], row["features"])
        else:
            raise ValueError(f"Unknown media type: {media_type}")
        
    def load_library_from_csv(self,file_name):
        library_list = []
        file_exists = os.path.isfile(file_name)
        if file_exists:
            with open(file_name, "r",newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    library_list.append(self.media_maker(row))
                return library_list
        else:
            with open(file_name, "w",newline="") as file:
                pass
            print("Library empty! Please add media.")


    def add_book(self, title, year, creator, creator_dob, genre, pages, book_type):
        book = Book(title, year, creator, creator_dob, genre, pages, book_type)
        self.library_contents.append(book)
        self.save_to_file(book, self.file_name)


    def add_audiobook(self, title, year, creator, creator_dob, genre, pages, book_type, duration, narrator):
        audio_book = AudioBook(title, year, creator, creator_dob, genre, pages, book_type, duration, narrator)
        self.library_contents.append(audio_book)
        self.save_to_file(audio_book, self.file_name)


    def add_dvd(self,title, year, creator, creator_dob, genre, duration, features):
        dvd = Dvd(title, year, creator, creator_dob, genre, duration, features)
        self.library_contents.append(dvd)
        self.save_to_file(dvd, self.file_name)

    def save_to_file(self,media,file_name):
        with open(file_name, "a", newline='') as file:
            fieldnames = ["title", "year", "creator", "creator_dob","genre", "pages", "duration", "narrator", "features", "book_type"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            row = {
                "title" : media.title,
                "year" : media.year,
                "creator" : media.creator.name,
                "creator_dob" : media.creator.year_of_birth,
                "genre" : media.genre,
                "pages" : media.pages,
                "book_type" : media.book_type,
                "duration" : media.duration,
                "narrator" : media.narrator,
                "features" : media.features
            }
            writer.writerow(row)

    def media_search(self):
        pass

    def creator_search(self):
        pass

    def genre_search(self):
        pass

library_test = Library("library.csv")

#book = Book("Dilla Time", 2022, "Dan Charnas", 1967, "Biography", 480,"Nonfiction" )
library_test.add_book("Dilla Time", 2022, "Dan Charnas", 1967, "Biography", 480,"Nonfiction")
print(type(library_test.library_contents))
     
#user input 
#not a valid input, type help for


#type help for list of commands
#Add new book
#search book by title
#seatch by author
#search by genre
#remove book
#display by recently added
#display genres
#filter results by genre, author etc

#book class
#fiction subclass
#nonfiction subclass


#library class
#search functions

#csv to store dictionary


#
