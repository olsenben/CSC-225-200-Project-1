import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Library import *

class AddMediaWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.withdraw()
        self.frame = tk.Frame(self)
        self.frame.pack()
        self.title = "Add New Media"
        self.media_types = ["Book", "AudioBook","Dvd"]
        self.media_match = None #store media object to be updated

        #combobox label
        self.selection_label = ttk.Label(self.frame, text="Media Type")
        self.selection_label.grid(row=0,column=0,padx=5,pady=5)

        #combobox to select media type for entry
        self.media_var = tk.StringVar()
        self.media_combo_box = ttk.Combobox(self.frame, textvariable=self.media_var, values=self.media_types, state="readonly")
        self.media_combo_box.grid(row=1,column=0,padx=5,pady=5)
        self.media_combo_box.bind("<<ComboboxSelected>>", self.update_add_widget)

        #entry widgets "title", "year", "creator", "creator_dob","genre", "pages", "book_type","duration", "narrator", "features"
        #Labels for entry widgets
        #again I really have no idea how you're supposed to organize a massive group like this
        #probably generating them dynamically and storing in a list or dict
        #I have not included checks to ensure all fields are filled correctly. honor system lol
        self.title_entry = ttk.Entry(self.frame)
        self.title_entry_label = ttk.Label(self.frame, text="Title")

        self.year_entry = ttk.Entry(self.frame)
        self.year_entry_label = ttk.Label(self.frame, text="Year Published (xxxx)")

        self.creator_entry = ttk.Entry(self.frame)
        self.creator_entry_label = ttk.Label(self.frame, text="Author Name")

        self.creator_dob_entry = ttk.Entry(self.frame)
        self.creator_dob_entry_label = ttk.Label(self.frame, text="Author YOB (xxxx)")

        self.genre_entry = ttk.Entry(self.frame)
        self.genre_entry_label = ttk.Label(self.frame, text="Genre")

        self.pages_entry = ttk.Entry(self.frame)
        self.pages_entry_label = ttk.Label(self.frame, text="# of Pages")

        #restricting input with a combobox
        self.book_type_var = tk.StringVar()
        self.book_type_combobox = ttk.Combobox(self.frame, textvariable=self.book_type_var, values=["Fiction","NonFiction"], state="readonly")
        self.book_type_combobox_label = ttk.Label(self.frame, text="Book Type")

        self.duration_entry = ttk.Entry(self.frame)
        self.duration_entry_label = ttk.Label(self.frame, text="Duration (min)")

        self.narrator_entry = ttk.Entry(self.frame)
        self.narrator_entry_label = ttk.Label(self.frame, text="Narration By")
        
        self.features_entry = ttk.Entry(self.frame)
        self.features_entry_label = tk.Label(self.frame, text="Actors featured")

        #cancel button
        self.cancel_button = tk.Button(self.frame, text="Cancel", command=self.go_home)
        self.cancel_button.grid(row=4,column=0)

        #add or update button button
                    
        self.update_button = tk.Button(self.frame, text="Update", command= lambda: [self.update_media(), self.go_home()])
        self.add_button = tk.Button(self.frame, text="Save", command= lambda: [self.add_media(), self.go_home()])



    def update_add_widget(self, event):
        """dynamically show the correct entry widgets depending on the media type selected"""
       # clear the previous widgets 
        for widget in [
            self.title_entry,
            self.title_entry_label,
            self.year_entry,
            self.year_entry_label,
            self.creator_entry, 
            self.creator_entry_label,
            self.creator_dob_entry, 
            self.creator_dob_entry_label,
            self.genre_entry, 
            self.genre_entry_label, 
            self.pages_entry, 
            self.pages_entry_label,
            self.book_type_combobox,
            self.book_type_combobox_label,
            self.duration_entry, 
            self.duration_entry_label,
            self.narrator_entry, 
            self.narrator_entry_label, 
            self.features_entry,
            self.features_entry_label
            ]:
            widget.grid_forget()
        #display the appropriate entry fields
        if self.media_var.get() == "Book":
            self.title_entry_label.grid(row=2, column=0)
            self.title_entry.grid(row=3,column=0)

            self.year_entry_label.grid(row=2,column=1)
            self.year_entry.grid(row=3, column=1)

            self.creator_entry_label.grid(row=2, column=2)
            self.creator_entry.grid(row=3,column=2)
            
            self.creator_dob_entry_label.grid(row=2, column=3)
            self.creator_dob_entry.grid(row=3,column=3)

            self.genre_entry_label.grid(row=2, column=4)
            self.genre_entry.grid(row=3,column=4)
            
            self.pages_entry_label.grid(row=2,column=5)
            self.pages_entry.grid(row=3,column=5)

            self.book_type_combobox_label.grid(row=2,column=6)
            self.book_type_combobox.grid(row=3,column=6)

        elif self.media_var.get() == "AudioBook":

            self.title_entry_label.grid(row=2, column=0)
            self.title_entry.grid(row=3,column=0)

            self.year_entry_label.grid(row=2,column=1)
            self.year_entry.grid(row=3, column=1)

            self.creator_entry_label.grid(row=2, column=2)
            self.creator_entry.grid(row=3,column=2)
            
            self.creator_dob_entry_label.grid(row=2, column=3)
            self.creator_dob_entry.grid(row=3,column=3)

            self.genre_entry_label.grid(row=2, column=4)
            self.genre_entry.grid(row=3,column=4)
            
            self.pages_entry_label.grid(row=2,column=5)
            self.pages_entry.grid(row=3,column=5)

            self.book_type_combobox_label.grid(row=2,column=6)
            self.book_type_combobox.grid(row=3,column=6)

            self.duration_entry_label.grid(row=2, column=7)
            self.duration_entry.grid(row=3, column=7)

            self.narrator_entry_label.grid(row=2, column=8)
            self.narrator_entry.grid(row=3, column=8)

        elif self.media_var.get() == "Dvd":

            self.title_entry_label.grid(row=2, column=0)
            self.title_entry.grid(row=3,column=0)

            self.year_entry_label.grid(row=2,column=1)
            self.year_entry.grid(row=3, column=1)

            self.creator_entry_label.grid(row=2, column=2)
            self.creator_entry.grid(row=3,column=2)
            
            self.creator_dob_entry_label.grid(row=2, column=3)
            self.creator_dob_entry.grid(row=3,column=3)

            self.genre_entry_label.grid(row=2, column=4)
            self.genre_entry.grid(row=3,column=4)

            self.duration_entry_label.grid(row=2, column=5)
            self.duration_entry.grid(row=3, column=5)

            self.features_entry_label.grid(row=2, column=6)
            self.features_entry.grid(row=3, column=6)

    def update_edit_widget(self):
        """dynamically show the correct entry widgets depending on the media type selected"""
        """This one does not use an event and isnt tied to a button"""
       # clear the previous widgets 
        for widget in [
            self.title_entry,
            self.title_entry_label,
            self.year_entry,
            self.year_entry_label,
            self.creator_entry, 
            self.creator_entry_label,
            self.creator_dob_entry, 
            self.creator_dob_entry_label,
            self.genre_entry, 
            self.genre_entry_label, 
            self.pages_entry, 
            self.pages_entry_label,
            self.book_type_combobox,
            self.book_type_combobox_label,
            self.duration_entry, 
            self.duration_entry_label,
            self.narrator_entry, 
            self.narrator_entry_label, 
            self.features_entry,
            self.features_entry_label
            ]:
            widget.grid_forget()
        #display the appropriate entry fields
        if self.media_var.get() == "Book":
            self.title_entry_label.grid(row=2, column=0)
            self.title_entry.grid(row=3,column=0)

            self.year_entry_label.grid(row=2,column=1)
            self.year_entry.grid(row=3, column=1)

            self.creator_entry_label.grid(row=2, column=2)
            self.creator_entry.grid(row=3,column=2)
            
            self.creator_dob_entry_label.grid(row=2, column=3)
            self.creator_dob_entry.grid(row=3,column=3)

            self.genre_entry_label.grid(row=2, column=4)
            self.genre_entry.grid(row=3,column=4)
            
            self.pages_entry_label.grid(row=2,column=5)
            self.pages_entry.grid(row=3,column=5)

            self.book_type_combobox_label.grid(row=2,column=6)
            self.book_type_combobox.grid(row=3,column=6)

        elif self.media_var.get() == "AudioBook":

            self.title_entry_label.grid(row=2, column=0)
            self.title_entry.grid(row=3,column=0)

            self.year_entry_label.grid(row=2,column=1)
            self.year_entry.grid(row=3, column=1)

            self.creator_entry_label.grid(row=2, column=2)
            self.creator_entry.grid(row=3,column=2)
            
            self.creator_dob_entry_label.grid(row=2, column=3)
            self.creator_dob_entry.grid(row=3,column=3)

            self.genre_entry_label.grid(row=2, column=4)
            self.genre_entry.grid(row=3,column=4)
            
            self.pages_entry_label.grid(row=2,column=5)
            self.pages_entry.grid(row=3,column=5)

            self.book_type_combobox_label.grid(row=2,column=6)
            self.book_type_combobox.grid(row=3,column=6)

            self.duration_entry_label.grid(row=2, column=7)
            self.duration_entry.grid(row=3, column=7)

            self.narrator_entry_label.grid(row=2, column=8)
            self.narrator_entry.grid(row=3, column=8)

        elif self.media_var.get() == "Dvd":

            self.title_entry_label.grid(row=2, column=0)
            self.title_entry.grid(row=3,column=0)

            self.year_entry_label.grid(row=2,column=1)
            self.year_entry.grid(row=3, column=1)

            self.creator_entry_label.grid(row=2, column=2)
            self.creator_entry.grid(row=3,column=2)
            
            self.creator_dob_entry_label.grid(row=2, column=3)
            self.creator_dob_entry.grid(row=3,column=3)

            self.genre_entry_label.grid(row=2, column=4)
            self.genre_entry.grid(row=3,column=4)

            self.duration_entry_label.grid(row=2, column=5)
            self.duration_entry.grid(row=3, column=5)

            self.features_entry_label.grid(row=2, column=6)
            self.features_entry.grid(row=3, column=6)

    def add_media(self):
        """adds media to library contents from entry fields. ONLY CHECKS THAT ALL FIELDS ARE FILLED"""
        try:    
            if self.media_var.get() == "Book":
                title = self.title_entry.get()
                year = self.year_entry.get()
                creator = self.creator_entry.get()
                creator_dob = self.creator_dob_entry.get()
                genre = self.genre_entry.get()
                pages = self.pages_entry.get()
                book_type = self.book_type_var.get()
                self.parent.library.add_book(title, year, creator, creator_dob, genre, pages, book_type)
            elif self.media_var.get() == "AudioBook":
                title = self.title_entry.get()
                year = self.year_entry.get()
                creator = self.creator_entry.get()
                creator_dob = self.creator_dob_entry.get()
                genre = self.genre_entry.get()
                pages = self.pages_entry.get()
                book_type = self.book_type_var.get()
                duration = self.duration_entry.get()
                narrator = self.narrator_entry.get()
                self.parent.library.add_audiobook(title, year, creator, creator_dob, genre, pages, book_type, duration,narrator)
            elif self.media_var.get() == "Dvd":
                title = self.title_entry.get()
                year = self.year_entry.get()
                creator = self.creator_entry.get()
                creator_dob = self.creator_dob_entry.get()
                genre = self.genre_entry.get()
                duration = self.duration_entry.get()
                features = self.features_entry.get()
                self.parent.library.add_dvd(title, year, creator, creator_dob, genre,duration,features)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))#this is my only failsafe for entry mistakes. I will add more if I have time

    def go_home(self):
        """hide add media window"""
        for widget in [
            self.title_entry,
            self.year_entry,
            self.creator_entry, 
            self.creator_dob_entry, 
            self.genre_entry, 
            self.pages_entry, 
            self.book_type_combobox,
            self.duration_entry, 
            self.narrator_entry, 
            self.features_entry,
            ]:
            widget.delete(0,tk.END)
        self.withdraw()

    def show_media_window(self):
        """raise add media window"""
        #forget existing widgets and clear entries. I think the labels can be removed from this
        for widget in [
            self.title_entry,
            self.title_entry_label,
            self.year_entry,
            self.year_entry_label,
            self.creator_entry, 
            self.creator_entry_label,
            self.creator_dob_entry, 
            self.creator_dob_entry_label,
            self.genre_entry, 
            self.genre_entry_label, 
            self.pages_entry, 
            self.pages_entry_label,
            self.book_type_combobox,
            self.book_type_combobox_label,
            self.duration_entry, 
            self.duration_entry_label,
            self.narrator_entry, 
            self.narrator_entry_label, 
            self.features_entry,
            self.features_entry_label,
            ]:
            widget.grid_forget()
        
        self.update_button.grid_forget()
        self.add_button.grid(row=4, column=1)
        self.deiconify() #raise add media window

    def show_edit_window(self, media_match):
                

        self.media_match = media_match
        self.media_var.set(media_match.media_type)
        self.show_media_window()
        self.add_button.grid_forget()
        self.update_button.grid(row=4, column=1)
        self.update_edit_widget()
        self.title_entry.insert(0,media_match.title)
        self.year_entry.insert(0,media_match.year)
        self.creator_entry.insert(0,media_match.creator.name)
        self.creator_dob_entry.insert(0,media_match.creator.year_of_birth)
        self.genre_entry.insert(0,media_match.genre)
        #everything below must use get attribute
        self.pages_entry.insert(0,getattr(media_match,"pages", ""))
        #self.book_type_combobox.insert(0,getattr(media_match,"book_type", ""))
        if media_match.media_type == "Book" or media_match.media_type == "Audiobook":
            self.book_type_var.set(media_match.book_type)
        self.duration_entry.insert(0,getattr(media_match,"duration",""))
        self.narrator_entry.insert(0, getattr(media_match,"narrator",""))
        self.features_entry.insert(0, getattr(media_match, "features",""))
    
    def update_media(self):
        self.parent.library.delete_media(str(self.media_match))
        self.add_media()
        self.parent.perform_search()
        self.media_match = None #reset self.media_match




