#Notepad
from tkinter import *


def newFile():
    global file
    root.title("Untitled-Notepad")
    file=None
    TextArea.delete(1.0,END)


def openFile():
    global file
    file =askopenfilename(defaultextension=".txt",
                          filetypes=[("All Files","*.*"),
                                    ("Text Documents","*.txt")])
    if file=="":
        file =None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file==None:
        file = asksaveasfilename(initialfile="untitled.txt",defaultextension=".txt",
                          filetypes=[("All Files","*.*"),
                                    ("Text Documents","*.txt")])

        if file=="":
            file=None
        else:
            f=open(file, "w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"- Notepad")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()



def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate("<<Cut>>")
def copy():
    TextArea.event_generate("<<Copy>>")
def paste():
    TextArea.event_generate("<<Paste>>")
def about():
    showinfo("Notepad","I am Keetarp")





if __name__ == '__main__':
    #Basic tkinter setup
    root =Tk()
    root.geometry("788x544")
    root.title("Notepad")
    root.wm_iconbitmap("notepad.ico")

#Add text area
    TextArea = Text(root,font=13)
    file = None
    TextArea.pack(expand=True,fill=BOTH)

    #Create menubar
    MenuBar = Menu(root)

    #File menu starts
    FileMenu = Menu(MenuBar,tearoff=0)
    #To open new file
    FileMenu.add_command(label ="New",command=newFile)

    #To Open already existing file
    FileMenu.add_command(label="Open",command=openFile)

    #To save the current file
    FileMenu.add_command(label="Save",command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    MenuBar.add_cascade(label="File",menu=FileMenu)

    #file menu ends

    #Edit menu starts
    EditMenu = Menu(MenuBar,tearoff=0)
    #TO give a feature of cut ,copy ,paste
    EditMenu.add_command(label= "Cut",command=cut)
    EditMenu.add_command(label= "Copy",command=copy)
    EditMenu.add_command(label= "Paste",command=paste)
    MenuBar.add_cascade(label="Edit",menu =EditMenu)
    #Edit menu ends

    #Help menu starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="Aout Notepad",command =about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    #Help menu ends

    root.config(menu=MenuBar)

    #Adding scrllbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)



root.mainloop()