import csv
import os
from Media import *
import datetime
from difflib import get_close_matches


"""Contains Library Class"""

class Library:
    """class that holds the library collection. contains methods for loading, adding, and deleting media"""
    def __init__(self,file_name):
        self.library_contents = self.load_library_from_csv(file_name) #load into memory
        self.file_name = file_name #name of csv
    
    def media_maker(self,row):
        """Create media objects from dict"""
        media_type = row["media_type"]
        if media_type == "Book":
            return Book(row["title"], int(row["year"]), row["creator"], row["creator_dob"], row["genre"], row["date_added"], row["pages"], row["book_type"])
        elif media_type == "AudioBook":
            return AudioBook(row["title"], int(row["year"]), row["creator"], row["creator_dob"], row["genre"], row["date_added"], row["pages"], row["book_type"], row["duration"], row["narrator"])
        elif media_type == "Dvd":
            return Dvd(row["title"], int(row["year"]), row["creator"], row["creator_dob"], row["genre"], row["date_added"], row["duration"], row["features"])
        else:
            raise ValueError(f"Unknown media type: {media_type}")
        
    def load_library_from_csv(self,file_name):
        """load media from csv and convert to objects. returns a list, creates csv if it doesnt exist"""
        library_list = [] #placeholder list for objects once created
        file_exists = os.path.isfile(file_name) #check if file exists
        if file_exists:
            with open(file_name, "r",newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    library_list.append(self.media_maker(row))
                print("library loaded")
                return library_list        
        #if file doesnt exist, create one with headers
        else:
            with open(file_name, "w",newline="") as file:
                #these field names should probably be handled dynamically
                fieldnames = ["date_added","media_type","title", "year", "creator", "creator_dob","genre", "pages", "book_type","duration", "narrator", "features"]
                writer = csv.writer(file)
                writer.writerow(fieldnames)
            print("Library empty! Please add media.")
            return []

    #I was going to make these all one function but maybe some other time
    def add_book(self, title, year, creator, creator_dob, genre, pages, book_type):
        """adds book type media to media list and saves to csv"""
        book = Book(title, year, creator, creator_dob, genre,datetime.datetime.now, pages, book_type)
        self.library_contents.append(book)
        self.save_to_file(book, self.file_name)


    def add_audiobook(self, title, year, creator, creator_dob, genre, pages, book_type, duration, narrator):
        """adds audio book type media to media list and saves to csv"""
        audio_book = AudioBook(title, year, creator, creator_dob, genre,datetime.datetime.now, pages, book_type, duration, narrator)
        self.library_contents.append(audio_book)
        self.save_to_file(audio_book, self.file_name)


    def add_dvd(self,title, year, creator, creator_dob, genre, duration, features):
        """adds DVD type media to media list and saves to csv"""
        dvd = Dvd(title, year, creator, creator_dob, genre,datetime.datetime.now,duration, features)
        self.library_contents.append(dvd)
        self.save_to_file(dvd, self.file_name)

    def save_to_file(self,media,file_name):
        """uses media object to create new line in csv"""
        with open(file_name, "a", newline='') as file:
            #again should probably handle fieldnames dynamically buuuuuuuuuuuuuuuuuuuuuuuut
            fieldnames = ["date_added","media_type","title", "year", "creator", "creator_dob","genre", "pages", "book_type","duration", "narrator", "features"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            row = {
                "date_added" : datetime.datetime.now(),
                "media_type" : media.media_type,
                "title" : media.title,
                "year" : media.year,
                "creator" : media.creator.name,
                "creator_dob" : media.creator.year_of_birth,
                "genre" : media.genre,
                #anything below this line depends on type of media object as they dont all have the same attributes
                #getattr allows us to return a default value if the attribute doesnt exist
                "pages" : getattr(media, "pages",None), 
                "book_type" : getattr(media, "book_type",None),
                "duration" : getattr(media, "duration",None),
                "narrator" : getattr(media, "narrator",None),
                "features" : getattr(media, "features",None)
            }
            writer.writerow(row)
            print("media saved")

    def delete_media(self, media):
        """removes media selected in treeview. media in the treeview is a str, not an object"""
        for other_media in self.library_contents: #library_contents is in memory
            if  str(other_media) == media: #media is a str
                self.library_contents.remove(other_media)
                print("Media Removed")

        #update file to match library in memory
        self.update_media_file()


    def update_media_file(self):
        """updates file to match library in memory"""
        #open file and rewrite library from memory into csv file. 
        with open(self.file_name, "w", newline='') as file:
            #rewrite headers. using a csv writer is redundant but I ran out of time and this works
            fieldnames = ["date_added","media_type","title", "year", "creator", "creator_dob","genre", "pages", "book_type","duration", "narrator", "features"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer = csv.writer(file) #lmao
            csv_writer.writerow(fieldnames) 
            for final_media in self.library_contents:
                row = {
                    "date_added" : str(final_media.date_added),#this is a datetime object so must be converted into a str
                    "media_type" : final_media.media_type,
                    "title" : final_media.title,
                    "year" : final_media.year,
                    "creator" : final_media.creator.name,
                    "creator_dob" : final_media.creator.year_of_birth,
                    "genre" : final_media.genre,
                    #anything below this line depends on type of media object as they dont all have the same attributes
                    #getattr allows us to return a default value if the attribute doesnt exist
                    "pages" : getattr(final_media, "pages",None), 
                    "book_type" : getattr(final_media, "book_type",None),
                    "duration" : getattr(final_media, "duration",None),
                    "narrator" : getattr(final_media, "narrator",None),
                    "features" : getattr(final_media, "features",None) 
                }
                writer.writerow(row)
        print("Data Updated")

    def match_media(self, media: str) -> object:
        """searches for matching media entry in memory (library.library_contents)"""
        condition = False
        while condition == False:
            for other_media in self.library_contents: #library_contents is in memory
                if  str(other_media) == media: #media is a str because it comes from the treeview selection
                    condition = True
                    return other_media #return matching media


    #def media_match(self, media, other_media):
    #    return media.media_type == other_media.media_type and str(media) == str(other_media)

    # def print_from_list(self, list):
    #     """because search results will be a list, \n will not be interpreted correctly"""
    #     return [print(item) for item in list]

    def is_close_match(self, term, media, cutoff=0.4):
        """returns True if term is a near match. this isnt the best way to do searches because it doesnt work with short keyword searches"""
        media_list = [media]
        return len(get_close_matches(term,media_list, cutoff=cutoff)) == 1

    def search_media(self, query, search_type):
        """title search, returns a list. Does not need to be exact match"""
        results = []
        if search_type == "Title":
            results = [media for media in self.library_contents if self.is_close_match(query, media.title)]
        elif search_type == "Creator":
            results = [media for media in self.library_contents if self.is_close_match(query, media.creator.name)]
        elif search_type == "Genre":
            results = [media for media in self.library_contents if self.is_close_match(query, media.genre)]
        #note that printing from this list directly will screw up formatting
        return results if len(results)>0 else "No results"

#library_test = Library("library.csv")

#book = Book("Dilla Time", 2022, "Dan Charnas", 1967, "Biography", 480,"Nonfiction" )
#library_test.add_book("Dilla Time", 2022, "Dan Charnas", 1967, "Biography", 480,"Nonfiction")
#library_test.add_dvd("The Abyss", 1989, "James Cameron", 1954 , "Action", 480,["Ed Harris","Mary Elizabeth Mastrantonio","Michael Biehn"])
#library_test.print_from_list(library_test.search_media("dilla", "Title"))

#dvd = Dvd("The Abyss", 1989, "James Cameron", "Sci-Fi", ["Ed Harris", "Mary Elizabeth Mastrantonio", "Michael Biehn"])

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
