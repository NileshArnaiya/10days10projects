# code to implement bookstore using tkinter as seen in a udemy online course
from tkinter import *
import backend

#gets current selected item in the list of books
def get_selected_row(event):
    global selected
    try:
        index = displayList.curselection()[0]
        selected = displayList.get(index) #getting item at the index
    except:
        pass

def view_command():
    list_delete()
    for row in backend.view():
        displayList.insert(END,row)

def list_delete():
    displayList.delete(0,END)

def search_command():
    list_delete()
    for row in backend.search(
        titleText.get(),authorText.get(),yearText.get(),isbnText.get()):
        displayList.insert(END,row)

def add_command():
    if titleText.get() == '' and authorText.get() == '':
        displayList.insert(0, "You're dead")
        pass
    else:
        backend.insert(titleText.get(),authorText.get(),yearText.get(),isbnText.get())
        list_delete()
        displayList.insert(END,
        (titleText.get(),authorText.get(),yearText.get(),isbnText.get()))

def delete_command():
    backend.delete(selected[0])
    print("It's deleted ")

def update_command():
    backend.update(selected[0],titleText.get(),authorText.get(),yearText.get(),isbnText.get())
    print("It's deleted ")

window = Tk()

window.wm_title("Book Boys")

title = Label(window,text ="Title")
title.grid(row=0,column=0)

author = Label(window,text ="Author")
author.grid(row=0,column=2)

year = Label(window,text ="Year")
year.grid(row=1,column=0)

isbn = Label(window,text ="ISBN")
isbn.grid(row=1,column=2)

titleText = StringVar()
e1 = Entry(window, textvariable= titleText)
e1.grid(row=0,column=1)

authorText = StringVar()
e2 = Entry(window, textvariable= authorText)
e2.grid(row=0,column=3)

yearText = StringVar()
e3 = Entry(window, textvariable= yearText)
e3.grid(row=1,column=1)

isbnText = StringVar()
e4 = Entry(window, textvariable= isbnText)
e4.grid(row=1,column=3)

displayList = Listbox(window, height=6, width=35)
displayList.grid(row=2,column=0,rowspan=6,columnspan=2)

scrolling = Scrollbar(window)
scrolling.grid(row=2,column=2,rowspan=6)

displayList.configure(yscrollcommand = scrolling.set)
scrolling.configure(command=displayList.yview)

displayList.bind('<<ListboxSelect>>',get_selected_row)

view = Button(window,text="View All", width=12, command= view_command)
view.grid(row=2,column=3)

search = Button(window,text="Search a book", width=15, command = search_command)
search.grid(row=3,column=3)

add = Button(window,text="Insert your book", width=15, command = add_command)
add.grid(row=4,column=3)

update = Button(window,text="Change data", width=14, command = update_command)
update.grid(row=5,column=3)

delete = Button(window,text="Delete it now", width=14, command = delete_command)
delete.grid(row=6,column=3)

close = Button(window,text="Close", width=12, command = window.destroy)
close.grid(row=7,column=3)


window.mainloop()
