# Library
![alt text](https://i.imgur.com/Zt9jPnY.gif "Library gif")
# Library System for Media Management
## With GUI
A Library database program for entering, saving, editing, and searching for media. Library media is store in a CVS

## To Run
All dependencies are default to python. To run, clone repo and run LibraryFrontEnd.py

## Features
-Search by title, creator, genre, year\
-Filter by media type\
-Display results and select for details\
-Sort results by title, creator, media type, or date added\
-Add/delete/edit media via interface\
-Dynamically generates media input fields depending on input type\
-Basic validation for user inputs\
-Validation against duplicates\
-Loads from and saves to a csv file (see sample csv with examples)\
-If csv does not exist, it will generate itself

## Limitations
-search is handled by difflib get_close_matches. Not really optimal for keyword searches but handles phrases well\
-I really didn't design this to handle a large database, so don't push it too much\
-You cannot convert media types in editing. I have no idea why, it really should be possible but it just does not work and I am out of energy\
-the majority of the work went into building a GUI, which I decided to add after writing much of the back end. I did my best to document everything but it's a little messy under the hood.\
-almost forgot, but scrollbar is not working. Nasty one.
