import tkinter as tk
from tkinter import ttk

"""Holds main window class and main loop. run this file to start application"""

class MainWindow(tk.Tk): 
    def __init__(self, title="Library", window_size="800x600"): 
        super().__init__() #initialize parent class tk.Tk
        self.title(title)
        self.geometry(window_size)
        self.search_options = ["Title", "Name", "Genre", "Year"] #default values for combobox options

        #search bar label
        search_label = tk.Label(self,text="Library Search:")
        search_label.pack(pady=5)

        #frame for search grid
        search_frame = ttk.Frame(self)
        search_frame.pack()

        #placeholder for selected value for combobox
        selected_option = tk.StringVar()

        #Create drop down menu for search parameter
        combobox = ttk.Combobox(search_frame, textvariable=selected_option, values=self.search_options)
        combobox.current(0) #this is not working idk why
        combobox.grid(column=0,row=0)

        #entry widget for input
        search_entry = tk.Entry(search_frame)
        search_entry.grid(column=1,row=0)

        #search button. No fuction currently applied to event
        search_button = tk.Button(search_frame, text="Search")
        search_button.grid(column=2, row=0)

        #to display returned search values I think??
        text_widget = tk.Text(self)
        text_widget.insert(tk.END, "placeholder")
        text_widget.pack(pady=10)
        

#start main loop
if __name__ == "__main__":
    Library = MainWindow()
    Library.mainloop()

    
