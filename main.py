import tkinter

#window
window = tkinter.Tk()
window.title("Python Tkinter")
window.minsize(width=450,height=300)

def click_button():
    user_input = my_entry.get()
    print(user_input)

#label
my_label = tkinter.Label(text="this is a label",font=('New Times Roman','20','normal'))
#my_label.config(bg="black",fg="white")
#my_label.pack(side="top")
#my_label.place(x=0,y=0)
my_label.grid(row=0, column=0)

#button
my_button= tkinter.Button(text="tikla bana" , command=click_button)
#my_button.pack(side="top")
#my_button.place(x=225-13, y=150-10)
#my_button.update()
#print(my_button.winfo_height())
#print(my_button.winfo_height())
my_button.grid(row=1 ,column=0)

#entry
my_entry = tkinter.Entry(width=20)
#my_entry.place(x=150,y=100)
#my_entry.pack(side="top")
my_entry.grid(row=0 ,column=5)

window.mainloop()