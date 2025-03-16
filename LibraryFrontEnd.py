import tkinter as tk
from tkinter import ttk
from Library import *
from AddMediaWindow import *


"""Holds main window class and main loop. run this file to start application"""

class LibraryApp(tk.Tk): 
    """Main Library App window"""
    def __init__(self, library, title="Library", window_size="800x600"): 
        super().__init__() #initialize parent class tk.Tk
        self.library = library
        self.title(title)
        self.geometry(window_size)
        self.search_options = ["Title", "Creator", "Genre", "Year"] #default values for combobox options
        self.add_media_window = AddMediaWindow(self) #instance of window for adding new media, 

        #search bar label
        self.search_label = tk.Label(self,text="Library Search:")
        self.search_label.pack(pady=5)

        #frame for search grid
        self.search_frame = ttk.Frame(self)
        self.search_frame.pack()

        #Create drop down menu for search parameter
        self.search_type = tk.StringVar(value="Search By") #placeholder for selected value for combobox
        self.combobox = ttk.Combobox(self.search_frame, textvariable=self.search_type, values=self.search_options,state="readonly")
        self.combobox.current(0) #this is not working idk why, something to do with how python handles garabage collection
        self.combobox.grid(column=0,row=0)

        #entry widget for input
        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.grid(column=1,row=0)

        #search button. No fuction currently applied to event
        self.search_button = tk.Button(self.search_frame, text="Search",command=self.perform_search)
        self.bind("<Return>", lambda event: self.perform_search())
        self.search_button.grid(column=2, row=0)

        #show results in a tree with columns "Title" and "Creator"
        self.columns = ["Title", "Creator","Type"]
        self.results_tree = ttk.Treeview(self, columns=self.columns, show="headings", height=10)
        for col in self.columns:
            self.results_tree.heading(col, text=col, command=lambda c=col: self.sort_treeview(self.results_tree, c, False))
        self.results_tree.column("Title", width=250)
        self.results_tree.column("Creator", width=150)
        self.results_tree.column("Type", width=100)
        self.results_tree.pack(pady=10)
        self.sort_order = {col: False for col in self.columns}  # False = ascending, True = descending


        #add scrollbar to treeview
        self.scrollbar = ttk.Scrollbar(self, orient='vertical',command=self.results_tree.yview) #initialize scrollbar in frame
        self.results_tree.config(yscrollcommand= self.scrollbar.set) #make srollbar change y axis when scrolled 
        self.scrollbar.pack(side='right', fill='y')

        #bind click event for selecting from combobox
        self.results_tree.bind("<ButtonRelease-1>", self.show_details)

        #show details in textbox
        self.details = tk.Text(self, height=6, width=80, wrap="word")
        self.details.config(state=tk.DISABLED)
        self.details.pack(pady=10)

        #add button to add new media
        self.sub_button_frame = ttk.Frame(self)
        self.sub_button_frame.pack(pady=5)
        self.add_button = tk.Button(self.sub_button_frame,text="Add New Media", command=self.go_to_add_media_window)
        
        #add delete button for deleting media
        self.delete_button = tk.Button(self.sub_button_frame, text="Delete Entry", command=self.remove_media)
        self.add_button.grid(row=0,column=0, padx=5, pady=5)
        self.delete_button.grid(row=0,column=1, padx=5, pady=5)

        #add edit button
        self.edit_button = tk.Button(self.sub_button_frame, text="Edit Media", command=self.go_to_edit_window)
        self.edit_button.grid(row=0,column=2, padx=5,pady=5)


    def perform_search(self):
        """triggers search and updates treeview"""
        query = self.search_entry.get().strip()
        search_type = self.search_type.get()

        results = self.library.search_media(query, search_type)#using get_close_matches. its okay, not the best

        #clear old results tree
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)

        #results will be a string 'no results' if there are no results
        #it will be a list if anything is found
        #a combobox is organized as a dictionary if I recall correctly
        if isinstance(results, list): 
            for media in results:
                self.results_tree.insert("", "end", values=(media.title, media.creator,media.media_type), tags=(media,))
        else:
            self.results_tree.insert("","end", values=("No Results Found",""))

    def show_details(self,event):
        """display string representation of media upong selection from combobox"""
        selected_item = self.results_tree.selection() #this is a string
        if not selected_item: 
            return
        media = self.results_tree.item(selected_item)["tags"][0]
        self.details.config(state=tk.NORMAL) #reconfig the text widget to be editable
        self.details.delete("1.0", tk.END) #clear it
        self.details.insert(tk.END, media) #insert new details
        self.details.config(state=tk.DISABLED) #disable text widget again
    
    def remove_media(self):
        """removes selected media from library contents"""
        selected_item = self.results_tree.selection() #get selection
        media_str = self.results_tree.item(selected_item)["tags"][0]
        self.library.delete_media(media_str) #remove from library
        self.details.config(state=tk.NORMAL) #enable text widget
        self.details.delete("1.0", tk.END) #clear it
        self.details.config(state=tk.DISABLED) #disable again
        self.perform_search() #consider trying to just remove the selected item from the combobox instead of rerunning the search

    def go_to_add_media_window(self):
        "unhides the add media window"
        self.add_media_window.show_media_window()

    def go_to_edit_window(self):
        """opens add media window to edit selection"""
        try:
            selected_item = self.results_tree.selection() #get selection
            media_str = self.results_tree.item(selected_item)["tags"][0]
            media_match = self.library.match_media(media_str)
            self.add_media_window.show_edit_window(media_match)
        except IndexError:
            messagebox.showerror("Input Error", "Nothing Selected")

    # Sorting function
    def sort_treeview(self,tree, col, descending):
        """Sorts the Treeview column when clicked."""
        # Get data from tree
        data_list = [(tree.set(item, col), item) for item in tree.get_children("")]

        # Try converting to integer for proper sorting (e.g., sorting years numerically)
        try:
            data_list = [(int(val), item) for val, item in data_list]
        except ValueError:
            pass  # Keep as strings if conversion fails

        # Sort data
        data_list.sort(reverse=descending)

        # Rearrange items in tree
        for index, (val, item) in enumerate(data_list):
            tree.move(item, "", index)

        # Toggle sorting order for next click
        self.sort_order[col] = not descending
        tree.heading(col, text=col, command=lambda: self.sort_treeview(tree, col, self.sort_order[col]))
    


#start main loop
if __name__ == "__main__":
    file_name = "library.csv"
    library_object = Library(file_name)
    Library = LibraryApp(library_object)
    Library.mainloop()


    
