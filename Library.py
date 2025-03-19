import csv
import os
from Media import *
import datetime
from difflib import get_close_matches
from tkinter import messagebox


"""Contains Library Class"""

class Library:
    """class that holds the library collection. contains methods for loading, adding, and deleting media"""
    def __init__(self,file_name):
        self.library_contents = self.load_library_from_csv(file_name) #load into memory
        self.file_name = file_name #name of csv
    
    def media_maker(self,row: dict) -> object:
        """Create media objects from row dict
        
        Args:
            row (dict): a dictionary from csv row with header as keys

        Returns:
            object: an instance of a Book, Audiobook, or Dvd object

        """
        media_type = row["media_type"]
        if media_type == "Book":
            return Book(row["title"], int(row["year"]), row["creator"], row["creator_dob"], row["genre"], row["date_added"], row["pages"], row["book_type"])
        elif media_type == "AudioBook":
            return AudioBook(row["title"], int(row["year"]), row["creator"], row["creator_dob"], row["genre"], row["date_added"], row["pages"], row["book_type"], row["duration"], row["narrator"])
        elif media_type == "Dvd":
            return Dvd(row["title"], int(row["year"]), row["creator"], row["creator_dob"], row["genre"], row["date_added"], row["duration"], row["features"])
        else:
            raise ValueError(f"Unknown media type: {media_type}")
        
    def load_library_from_csv(self,file_name: str) -> list:
        """load media from csv and convert to objects. returns a list, creates csv if it doesnt exist.
        
        Args:
            file_name (str): string with pathway to file

        Returns:
            list: list containing isntances of library objects (Book, Audiobook, Dvd) (returns empty list if new file)

        """
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
    def add_book(self, title: str, year:str, creator:str, creator_dob:str, genre:str, pages:str, book_type:str) ->object:
        """adds book type media to media list and saves to csv. Checks for duplicate entry
        
        Args:
            title (str): title of book
            year (str): year book was published
            creator (str): author name
            creator_dob (str): author dob
            genre (str): book genre
            pages (str or int): num of pages
            booktype (Str): fiction or nonfiction
        
        Returns:
            object: Book object
        """
        book = Book(title, year, creator, creator_dob, genre,str(datetime.datetime.now()), pages, book_type)
        self.check_for_duplicate(str(book)) #check for duplicates
        self.library_contents.append(book) #add to library_contents in memory
        self.save_to_file(book, self.file_name) #append new row to file


    def add_audiobook(self, title, year, creator, creator_dob, genre, pages, book_type, duration, narrator):
        """adds audio book type media to media list and saves to csv"""
        audio_book = AudioBook(title, year, creator, creator_dob, genre,str(datetime.datetime.now()), pages, book_type, duration, narrator)
        self.check_for_duplicate(str(audio_book))
        self.library_contents.append(audio_book)
        self.save_to_file(audio_book, self.file_name)


    def add_dvd(self,title, year, creator, creator_dob, genre, duration, features):
        """adds DVD type media to media list and saves to csv"""
        dvd = Dvd(title, year, creator, creator_dob, genre,str(datetime.datetime.now()),duration, features)
        self.check_for_duplicate(str(dvd))
        self.library_contents.append(dvd)
        self.save_to_file(dvd, self.file_name)

    def check_for_duplicate(self, media:str):
        """raises error if duplcate of media exists
        
        Args:
            media (str): string representation of a media object
        """
        duplicate = self.match_media(str(media))
        if duplicate == "No Match":
            return
        else:
            messagebox.showerror("Duplicate warning", f"Duplicate Media Found:\n{duplicate}")
            raise


    def save_to_file(self,media,file_name):
        """uses media object to create new line in csv
        
        Args:
            media (obj): Instance of Book, Audiobook, or Dvd object
            file_name (str): path to file directory

        """
        with open(file_name, "a", newline='') as file:
            #again should probably handle fieldnames dynamically buuuuuuuuuuuuuuuuuuuuuuuut
            fieldnames = ["date_added","media_type","title", "year", "creator", "creator_dob","genre", "pages", "book_type","duration", "narrator", "features"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            row = {
                "date_added" : str(datetime.datetime.now()),
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

    def delete_media(self, media: str):
        """removes media from memory/file selected in treeview. media in the treeview is a str, not an object
        
        Args:
            media (str): String representation of media
        """
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
        """searches for matching media entry in memory (library.library_contents)
        
        Args:
            media (str): string representation of a media object

        Returns:
            (object) : returns any object matching the string, or None if no matches
        """
        for other_media in self.library_contents: #library_contents is in memory
                if  str(other_media) == str(media): #media is a str because it comes from the treeview selection
                    return other_media #return matching media
        return "No Match"


    #def is_duplicate(self, media, other_media):
    #    return media.media_type == other_media.media_type and str(media) == str(other_media)

    # def print_from_list(self, list):
    #     """because search results will be a list, \n will not be interpreted correctly"""
    #     return [print(item) for item in list]

    def is_close_match(self, term:str, media:str, cutoff:float=0.4):
        """returns True if term is a near match. this isnt the best way to do searches because it doesnt work with short keyword searches
        
        Args:
            term (str): search term
            media (str): corresponding media attribute to match search term to
            cutoff (float): match ratio, 0-1.0 with 1 the stricktist match, 

        Returns:
            Bool: True if it is a closematch, Flase if not
        """
        media_list = [media]
        return len(get_close_matches(term,media_list, cutoff=cutoff)) == 1

    def search_media(self, query:str, search_type:str)-> list:
        """title search, returns a list. Does not need to be exact match
        
        Args:
            query (str): search term 
            search_type: 'Title', 'Creator', or 'Genre' type search

        Returns:
            list: list containing search results
            str: "No Results" if no results found
        """
        results = []
        if search_type == "Title":
            results = [media for media in self.library_contents if self.is_close_match(query, media.title)]
        elif search_type == "Creator":
            results = [media for media in self.library_contents if self.is_close_match(query, media.creator.name)]
        elif search_type == "Genre":
            results = [media for media in self.library_contents if self.is_close_match(query, media.genre)]
        #note that printing from this list directly will screw up formatting
        return results if len(results)>0 else "No results"

