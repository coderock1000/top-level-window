from tkinter import *
root = Tk()
root.geometry('400x400')
root.title("main")

def top_window():
    top = Toplevel()
    top.geometry("180x100")
    top.title('top level')
    l2 = Label(top, text="This is a top level window.")
    l2.pack()
    top.mainloop()

l = Label(root, text="This is a root wind.")
btn = Button(root, text = "click here to open top level window", command=top_window)

l.pack()
btn.pack()
root.mainloop()
