import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Library import *
import copy


class AddMediaWindow(tk.Toplevel):
    """Class to hold window for user to enter data for creating isntances of media objects"""
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent #reference to main window
        self.withdraw() #initalize hidden
        self.frame = tk.Frame(self)
        self.frame.pack()
        self.title = "Add New Media"
        self.media_types = ["Book", "AudioBook","Dvd"] #current available media types
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
        
        #display the ubiquitous fields
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
        #display the appropriate entry fields
        if self.media_var.get() == "Book":
            
            self.pages_entry_label.grid(row=2,column=5)
            self.pages_entry.grid(row=3,column=5)

            self.book_type_combobox_label.grid(row=2,column=6)
            self.book_type_combobox.grid(row=3,column=6)

        elif self.media_var.get() == "AudioBook":
            
            self.pages_entry_label.grid(row=2,column=5)
            self.pages_entry.grid(row=3,column=5)

            self.book_type_combobox_label.grid(row=2,column=6)
            self.book_type_combobox.grid(row=3,column=6)

            self.duration_entry_label.grid(row=2, column=7)
            self.duration_entry.grid(row=3, column=7)

            self.narrator_entry_label.grid(row=2, column=8)
            self.narrator_entry.grid(row=3, column=8)

        elif self.media_var.get() == "Dvd":

            self.duration_entry_label.grid(row=2, column=5)
            self.duration_entry.grid(row=3, column=5)

            self.features_entry_label.grid(row=2, column=6)
            self.features_entry.grid(row=3, column=6)

    def add_media(self):
        """adds media to library contents from entry fields."""
        
        #validate entry fields
        fields = self.get_fields()
        validated_fields = self.validate_fields(fields)
        
        #get dictionary of input fields
        try:    
            if self.media_var.get() == "Book":
                self.parent.library.add_book(**validated_fields)
            elif self.media_var.get() == "AudioBook":
                self.parent.library.add_audiobook(**validated_fields)
            elif self.media_var.get() == "Dvd":
                self.parent.library.add_dvd(**validated_fields)
        except ValueError:
            #check that all fields are filled out. digits are validated separately 
            messagebox.showerror("Input Error", "Please fill all fields") 
            raise ValueError

    def validate_fields(self,fields: dict) -> dict:
        """validates entry inputs and raises appropriate errors if they are filled incorrectly, 
        otherwise returns dictionary of inputs
        
        Args:
            fields (dict): dictionary of all gathered input fields
        """
        #fields that need their digits checked
        digit_fields = ["year", "creator_dob", "pages", "duration"]        

        #ensure that the attribute exists before validating it
        for entry in digit_fields:
            if entry in fields:
                self.check_valid_digit(fields[entry],entry)

        #check that genre doesnt have any digits
        if all(c.isalpha() or c.isspace() or c == ',' for c in fields["genre"]):
            pass
        else:
            messagebox.showerror("Input Error", "Please input valid genre with no numbers or special characters")
            raise ValueError

        #return validated dictionary
        print("fields validated")
        return fields

    def check_valid_digit(self, entry: str, digit_type: str):
        """checks if the digit type matches expected length and format (year, pages, duration)
        
        Args:
            entry (str): data to be validated
            digit_type (str): year (or creator dob which is a year), pages, or duration
        
        """
        #I was really generous with the upper limits, honestly not sure if they're necessary
        if digit_type == "year" or digit_type == "creator_dob":
            check_len = 4
            lower, upper = 999, 9999
            digit_format = ", format: (0000)"
        elif digit_type == "pages":
            check_len = len(entry)
            digit_format =''
            lower, upper = 0, 100000
        elif digit_type == "duration":
            check_len = len(entry)
            lower, upper = 0, 200000
            digit_format = ''
        else: 
            messagebox.showerror("Input Error", f"Unknown field: {digit_type}")
            raise ValueError

        #check that they are digits and correct length
        if entry.isdigit() and len(entry) == check_len:
            try:
                #try converting to integer
                as_int = int(entry)
                #check that it is within limits
                if lower <= as_int <= upper:
                    return
                else:
                    messagebox.showerror("Input Error", f"Please input valid {digit_type} between {upper} and {lower}")
                    raise ValueError
            except ValueError:
                messagebox.showerror("Input Error", f"Please input valid {digit_type}{digit_format}")
                raise ValueError
        else:
            messagebox.showerror("Input Error", f"Please input valid {digit_type}{digit_format}")
            raise ValueError
 
    


    def get_fields(self):
        """creates dictionary from entry fields depending on selection in media_var from media_combo_box"""
        #add a validation step here to validate inputs
        fields = {}

        #get the ubiqutous fields
        fields['title'] = self.title_entry.get()
        fields['year'] = self.year_entry.get()
        fields['creator'] = self.creator_entry.get()
        fields['creator_dob'] = self.creator_dob_entry.get()
        fields['genre'] = self.genre_entry.get()
        
        #get the relevant fields depending on self.media_var set by self.media_combo_box
        if self.media_var.get() == "Book":
            fields['pages'] = self.pages_entry.get()
            fields['book_type'] = self.book_type_var.get()

        elif self.media_var.get() == "AudioBook":
            fields['pages'] = self.pages_entry.get()
            fields['book_type'] = self.book_type_var.get()
            fields['duration'] = self.duration_entry.get()
            fields['narrator'] = self.narrator_entry.get()

        elif self.media_var.get() == "Dvd":
            fields['genre'] = self.genre_entry.get()
            fields['duration'] = self.duration_entry.get()
            fields['features'] = self.features_entry.get()
        
        return fields

    def go_home(self):
        """hide add media window"""
        #clear entry fields
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
        #withdraw the window
        self.withdraw()

    def show_media_window(self):
        """raise add media window"""
        #forget existing widgets and clear entries. must be done so they can be placed dynamically
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
        
        #forget the update button if its there and replace with add button
        self.update_button.grid_forget()
        self.add_button.grid(row=4, column=1)
        self.deiconify() #raise add media window

    def show_edit_window(self, media_match: object):
        """raise add media window with update button instead of add button"""
        #save the object for reference
        self.media_match = media_match

        #preset the media_var combobox to show correct fields
        self.media_var.set(media_match.media_type)

        #show add media window with update button instead of add button
        self.show_media_window()
        self.add_button.grid_forget()
        self.update_button.grid(row=4, column=1)
        self.update_add_widget(None)

        #prepopulate entry fields with existing data
        self.title_entry.insert(0,media_match.title)
        self.year_entry.insert(0,media_match.year)
        self.creator_entry.insert(0,media_match.creator.name)
        self.creator_dob_entry.insert(0,media_match.creator.year_of_birth)
        self.genre_entry.insert(0,media_match.genre)

        #everything below must use get attribute incase that object does not have it
        #i.e. a book will not have a duration and a dvd will not have pages
        self.pages_entry.insert(0,getattr(media_match,"pages", ""))
       
        #except this one preselect the media type in the combobox
        if media_match.media_type == "Book" or media_match.media_type == "Audiobook":
            self.book_type_var.set(media_match.book_type)

        self.duration_entry.insert(0,getattr(media_match,"duration",""))
        self.narrator_entry.insert(0, getattr(media_match,"narrator",""))
        self.features_entry.insert(0, getattr(media_match, "features",""))
    
    def update_media(self):
        """saves updated object"""

        #get field names   
        unvalidated_fields = self.get_fields()

        fields = self.validate_fields(unvalidated_fields)

        #create reference to object in memory 
        media_to_update = self.parent.library.match_media(str(self.media_match)) 

        #creator name and dob are used to create instance of creator object 
        #first remove from dictionary 
        creator_name = fields.pop('creator')
        creator_dob = fields.pop('creator_dob')

        #create a copy of object for use in checking for duplcates
        media_match = copy.deepcopy(self.media_match)

        #pass them explicitly 
        media_match.creator.name = creator_name
        media_match.creator.year_of_birth = creator_dob

        #update attributes for object saved in self.media_match to check for duplicates
        for key, value in fields.items():

            if hasattr(media_match, key):
                setattr(media_match, key, value)
          
        #check for duplicates
        self.parent.library.check_for_duplicate(str(media_match))
        
        #update nested fields explicitly for object in memory
        media_to_update.creator.name = creator_name
        media_to_update.creator.year_of_birth = creator_dob

        #now set values for object in library memory
        for key, value in fields.items():

            if hasattr(media_to_update, key):
                setattr(media_to_update, key, value)

        #update library csv
        self.parent.library.update_media_file()

        self.parent.show_details(None)

        #update search results
        self.parent.perform_search()

        #reset self.media_match
        self.media_match = None 




