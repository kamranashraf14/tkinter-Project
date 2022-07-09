from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.title("My Paint")
root.geometry("450x400")
def paint(event):
    x1,y1,x2,y2=(event.x-3),(event.y-3),(event.x+3),(event.y+3)
    widget.create_line(x1,y1,x2,y2,fill= "red")

def hello():
    tmsg.askokcancel("New File","New file will be opened")
def help():
    tmsg.showinfo("Help","Double click and drag to draw")
def rate_us():
    value=tmsg.askquestion("Experience","was your experience good?")
    if value=="yes":
        msg="Rate us on Play Store!"
    else:
        msg="Tell us your problem we will contact you"
    tmsg.showinfo("Info",msg)
def saved():
    value=tmsg.askyesnocancel("SAVE","Do You Want To Save?")


# create a toplevel menu
my_menu=Menu(root)
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New....", command=hello)
file_menu.add_command(label="Open..")
file_menu.add_separator()
file_menu.add_command(label="Save As..",command=saved)
file_menu.add_command(label="Quit!", command=root.quit)

edit_menu=Menu(my_menu)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="edit")
edit_menu.add_separator()
edit_menu.add_command(label="save")

help_menu=Menu(my_menu)
my_menu.add_cascade(label="Hints",menu=help_menu)
help_menu.add_command(label="Help!",command=help)

rate_menu=Menu(my_menu)
my_menu.add_cascade(label="Rate us",menu=rate_menu)
rate_menu.add_command(label="Rate us",command=rate_us)

# display the menu
root.config(menu=my_menu)


#Button(root,text="Exit",bg="black",fg="red",command=quit,padx=13,pady=13).pack(anchor="se",side=BOTTOM,padx=12,pady=12)
widget=Canvas(root,width=400,height=300)
#Button(root,text="File",fg="black",padx=1,pady=1).pack(anchor="nw",side=LEFT,padx=1,pady=3)
#Button(root,text="Edit",fg="black",padx=1,pady=1).pack(anchor="nw",side=LEFT,padx=1,pady=3)
#Button(root,text="Help",fg="black",padx=1,pady=1).pack(anchor="nw",side=LEFT,padx=3,pady=3)
widget.bind("<B1-Motion>",paint)
Label(root,text="Double click and drag to draw.",bg="black",fg="red",height=1,width=30).pack(padx=15,pady=3)
widget.pack()
root.mainloop()
