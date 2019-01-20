import gui
import sqlite3
from tkinter import ttk
#using magic method for printing tkinter version
print("Version of ttk wrapper is: {}".format(ttk.__version__))
def haslo():
            print("Ok, you can go")
            #Here I had to use Top level because tkinter doesn't allow to run more than one instances of Tk() running simultounesly
            root2=gui.Toplevel()
            root2.geometry("880x425+440+212")
            root2['bg'] = 'black'
            frmenu = gui.FormMenu(root2)
            conn = sqlite3.connect("lcc")
            cur = conn.cursor()
            cur.execute("select* from invoices")
            print(cur.fetchone()[1])
            results = cur.fetchall()
            if __name__ == "__main__":
                root2.mainloop()
#Tk() is the main widget of the application
root=gui.Tk()
# Make window 880x425 and place at position 440,212
root.geometry("880x425+440+212")
root.maxsize(800,600)
lg=gui.Login(root)
#main loop of the program that keeps repeating
root.mainloop()
haslo()
