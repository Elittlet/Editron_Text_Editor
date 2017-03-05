#############################################################
#	Simple Text Editor that opens, saves, and writes files. #
#				A work in Progress.							#
#															#
#															#
#															#
#															#
#															#
#############################################################




# Importing the neccesary modules #

from tkinter import *


from tkinter import filedialog
from tkinter import messagebox

# GUI contruction. Stating the size of the text box #

master = Tk()
master.title("Editron")
master.geometry("400x380")


text = Text(master, width = 400, height = 380, font = ("Andale Mono", 12), bd = 2)
text.pack()


# Function for opening a new session of the text editor #

def new():
	ask = messagebox.askquestion(title = "Save file", message = "Would you like to save the current file?")
	if ask is True:
		save()
	delete_all()

# Function for the opening of a file that is to be edited #

def open_file():
	new()
	file = filedialog.askopenfile()
	text.insert(INSERT, file.read())


# Function that asks the user if they want to say  #
def save():
	path = filedialog.asksaveasfilename()
	write = open(path, mode = 'w')
	write.write(text.get("1.0", END))


def rename():
	pass


# Closing the editor session  #

def close():
	save()
	master.quit()

# Defining and creating the cut ability #

def cut():
	master.clipboard_clear()
	text.clipboard_append(string = text.selection_get())
	text.delete(index1 = SEL_FIRST, index2 = SEL_LAST)

# Defining and creating the copy function #

def copy():
	master.clipboard_clear()
	text.clipboard_append(String = text.selection_get())

# Defining the paste function #

def paste():
	text.insert(INSERT, master.clipboard_get())

def delete():
	text.delete(index1 = SEL_FIRST, index2 = SEL_LAST)

def select_all():
	text.tag_add(SEL, "1.0", END)

def delete_all():
	text.delete(1.0, END)



#----------------- FILE MENU SETUP ---------------------- #

menu = Menu(master)
master.config(menu = menu)
file_menu = Menu(menu)
menu.add_cascade(label = "File", menu = file_menu)

file_menu.add_command(label = "New", command = new)
file_menu.add_command(label = "Open", command = open_file())
file_menu.add_separator()
file_menu.add_command(label = "Close", command = close)
file_menu.add_command(label = "Save", command = save)


#----------------- EDIT MENU SETUP ---------------------- #

edit_menu = Menu(menu)
menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Undo", comman = text.edit_undo)
edit_menu.add_command(label = "Redo", comman = text.edit_undo)
edit_menu.add_separator()
edit_menu.add_command(label = "Cut", command = cut)
edit_menu.add_command(label = "Copy", command = copy)
edit_menu.add_command(label = "Paste", command = paste)
edit_menu.add_command(label = "Delete", command = delete)

master.mainloop()