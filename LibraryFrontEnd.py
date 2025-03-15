import tkinter as tk
from tkinter import ttk
from Library import *

"""Holds main window class and main loop. run this file to start application"""

class LibraryApp(tk.Tk): 
    def __init__(self, library, title="Library", window_size="800x600"): 
        super().__init__() #initialize parent class tk.Tk
        self.library = library
        self.title(title)
        self.geometry(window_size)
        self.search_options = ["Title", "Creator", "Genre", "Year"] #default values for combobox options

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
        #self.search_button.bind("<Enter>", self.perform_search)
        self.search_button.grid(column=2, row=0)

        #show results in a tree with columns "Title" and "Creator"
        self.results_tree = ttk.Treeview(self, columns=("Title", "Creator"), show="headings", height=10)
        self.results_tree.heading("Title", text="Title")
        self.results_tree.heading("Creator", text="Creator")
        self.results_tree.column("Title", width=250)
        self.results_tree.column("Creator", width=150)
        self.results_tree.pack(pady=10)

        #bind click event
        self.results_tree.bind("<ButtonRelease-1>", self.show_details)

        #show details in text
        self.details = tk.Text(self, height=6, width=80, wrap="word")
        self.details.config(state=tk.DISABLED)
        self.details.pack(pady=10)


    def perform_search(self):
        """triggers search and updates listbox"""
        query = self.search_entry.get().strip()
        search_type = self.search_type.get()

        results = self.library.search_media(query, search_type)

        #clear results tree
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)

        if isinstance(results, list):
            for media in results:
                self.results_tree.insert("", "end", values=(media.title, media.creator), tags=(media,))
        else:
            self.results_tree.insert("","end", values=("No Results Found",""))

    def show_details(self,event):
        selected_item = self.results_tree.selection()
        if not selected_item:
            return
        media = self.results_tree.item(selected_item)["tags"][0]

        self.details.config(state=tk.NORMAL)
        self.details.delete("1.0", tk.END)
        self.details.insert(tk.END, str(media))
        self.details.config(state=tk.DISABLED)




        

#start main loop
if __name__ == "__main__":
    file_name = "library.csv"
    initialize_library = Library(file_name)
    Library = LibraryApp(initialize_library)
    Library.mainloop()


    
