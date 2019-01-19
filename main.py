#from binascii import a2b_qp
# final from 20/09/2018. To jest ostateczna wersja
import gui
import sqlite3
from tkinter import ttk
###simple password checking method
def haslo():
            print("Ok, you can go")
            root2=gui.Toplevel()
            root2.geometry("880x425")
            root2['bg'] = 'black'
            frmenu = gui.FormMenu(root2)
            # frmenu._init_widgets()
            conn = sqlite3.connect("lcc")
            cur = conn.cursor()
            cur.execute("select* from invoices")
            print(cur.fetchone()[1])
            results = cur.fetchall()
            if __name__ == "__main__":
                root2.mainloop()

root=gui.Tk()
# root2=gui.Tk()
root.geometry("880x425")
lg=gui.Login(root)
# lg.pack()
# lg._init_widget()
root.mainloop()
haslo()
