from tkinter import *

my_window = Tk()
my_window.title("Tkinter Python")
my_window.wm_minsize(width=600, height=600)
my_window.config(padx=20, pady=20)

my_label = Label(text="my label")
my_label.config(bg="black", fg="white", )
my_label.config(padx=10, pady=10)
my_label.pack()

#button
def button_clicked():
    print("button clicked")
    print(my_text.get("1.0",END))

my_button = Button(text="bas bana", command= button_clicked, bg="green")
my_button.config(padx=10, pady=10)
my_button.pack()

entry=Entry(width=20)
entry.pack()

my_text = Text(width=30, height=10)
#my_text.focus()
my_text.pack()

#scale
def scale_selected(value):
    print(value)


my_scale = Scale(from_=0, to=50, command=scale_selected)

my_scale.pack()

#spinbox

def spinbox_selected():
    print(my_spinbox.get())


my_spinbox= Spinbox(from_=0, to=50, command=spinbox_selected)
my_spinbox.pack()

#chechk_button
def checkbutton_selected():
    print(check_state.get())

check_state =   IntVar()

my_checkbutton= Checkbutton(text="check", variable= check_state, command=checkbutton_selected)
my_checkbutton.pack()

#radio button

def radio_selected():
    print(radio_check_state.get())

radio_check_state= IntVar()
my_radiobutton = Radiobutton(text="first option",value=10,variable=radio_check_state,command=radio_selected)
my_radiobutton_2 = Radiobutton(text="second option",value=20,variable=radio_check_state,command=radio_selected)
my_radiobutton.pack()
my_radiobutton_2.pack()

#listbox

def listbox_selected():
    print(my_listbox.get(my_listbox.curselection()))

my_listbox = Listbox()
name_list = ["Hasan","Huseyin","Mert"]

for i in range(len(name_list)):
    my_listbox.insert(i,name_list[i])

my_listbox.bind('<<ListboxSelected>>', listbox_selected)
my_listbox.pack()



my_window.mainloop()