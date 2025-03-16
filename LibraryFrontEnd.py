import tkinter as tk
from tkinter import ttk
from Library import *
from AddMediaWindow import *


"""Holds main window class and main loop. run this file to start application"""

class LibraryApp(tk.Tk): 
    def __init__(self, library, title="Library", window_size="800x600"): 
        super().__init__() #initialize parent class tk.Tk
        self.library = library
        self.title(title)
        self.geometry(window_size)
        self.search_options = ["Title", "Creator", "Genre", "Year"] #default values for combobox options
        self.add_media_window = AddMediaWindow(self)

        #search bar label
        self.search_label = tk.Label(self,text="Library Search:")
        self.search_label.pack(pady=5)

        #frame for search grid
        self.search_frame = ttk.Frame(self)
        self.search_frame.pack()

        #Create drop down menu for search parameter
        self.search_type = tk.StringVar(value="Search By") #placeholder for selected value for combobox
        self.combobox = ttk.Combobox(self.search_frame, textvariable=self.search_type, values=self.search_options,state="readonly")
        self.combobox.current(0) #this is not working idk why
        self.combobox.grid(column=0,row=0)

        #entry widget for input
        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.grid(column=1,row=0)

        #search button. No fuction currently applied to event
        self.search_button = tk.Button(self.search_frame, text="Search",command=self.perform_search)
        self.bind("<Return>", lambda event: self.perform_search())
        self.search_button.grid(column=2, row=0)

        #show results in a tree with columns "Title" and "Creator"
        self.results_tree = ttk.Treeview(self, columns=("Title", "Creator","Type"), show="headings", height=10)
        self.results_tree.heading("Title", text="Title")
        self.results_tree.heading("Creator", text="Creator")
        self.results_tree.heading("Type", text="Type")
        self.results_tree.column("Title", width=250)
        self.results_tree.column("Creator", width=150)
        self.results_tree.column("Type", width=100)

        self.results_tree.pack(pady=10)

        #bind click event
        self.results_tree.bind("<ButtonRelease-1>", self.show_details)

        #show details in text
        self.details = tk.Text(self, height=6, width=80, wrap="word")
        self.details.config(state=tk.DISABLED)
        self.details.pack(pady=10)

        #add button to add new media
        self.sub_button_frame = ttk.Frame(self)
        self.sub_button_frame.pack(pady=5)
        self.add_button = tk.Button(self.sub_button_frame,text="Add New Media", command=self.go_to_add_media_window)
        self.delete_button = tk.Button(self.sub_button_frame, text="Delete Entry", command=self.remove_media)
        self.add_button.grid(row=0,column=0)
        self.delete_button.grid(row=0,column=1)


    def perform_search(self):
        """triggers search and updates treeview"""
        query = self.search_entry.get().strip()
        search_type = self.search_type.get()

        results = self.library.search_media(query, search_type)

        #clear results tree
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)

        if isinstance(results, list):
            for media in results:
                self.results_tree.insert("", "end", values=(media.title, media.creator,media.media_type), tags=(media,))
        else:
            self.results_tree.insert("","end", values=("No Results Found",""))

    def show_details(self,event):
        selected_item = self.results_tree.selection()
        if not selected_item:
            return
        media = self.results_tree.item(selected_item)["tags"][0]
        self.details.config(state=tk.NORMAL)
        self.details.delete("1.0", tk.END)
        self.details.insert(tk.END, media)
        self.details.config(state=tk.DISABLED)
    
    def remove_media(self):
        selected_item = self.results_tree.selection()
        media_str = self.results_tree.item(selected_item)["tags"][0]
        self.library.delete_media(media_str)
        self.details.config(state=tk.NORMAL)
        self.details.delete("1.0", tk.END)
        self.details.config(state=tk.DISABLED)
        self.perform_search()

    def go_to_add_media_window(self):
        self.add_media_window.show_media_window()

    def show(self):
        self.tkraise()
    





#start main loop
if __name__ == "__main__":
    file_name = "library.csv"
    library_object = Library(file_name)
    Library = LibraryApp(library_object)
    Library.mainloop()


    
