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

        self.book_type_var = tk.StringVar()
        self.book_type_combobox = ttk.Combobox(self.frame, textvariable=self.book_type_var, values=["Fiction","NonFiction"], state="readonly")
        self.book_type_combobox_label = ttk.Label(self.frame, text="Book Type")

        self.duration_entry = ttk.Entry(self.frame)
        self.duration_entry_label = ttk.Label(self.frame, text="Duration (min)")

        self.narrator_entry = ttk.Entry(self.frame)
        self.narrator_entry_label = ttk.Label(self.frame, text="Narration By")
        
        self.features_entry = ttk.Entry(self.frame)
        self.features_entry_label = tk.Label(self.frame, text="Actors featured (separate with ,)")

        #add button
        self.add_button = tk.Button(self.frame, text="Add to Library")

        #cancel button
        self.cancel_button = tk.Button(self.frame, text="Cancel", command=self.go_home)
        self.cancel_button.grid(row=4,column=0)

        #add button
        self.add_button = tk.Button(self.frame, text="Add Media To Library", command= lambda: [self.add_media(), self.go_home()])
        self.add_button.grid(row=4, column=1)

    def update_add_widget(self, event):

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
                features = self.features_entry.get().split(",")
                self.parent.library.add_dvd(title, year, creator, creator_dob, genre,duration,features)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))



    def go_home(self):
        self.withdraw()

    def show_media_window(self):
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
        self.deiconify()

