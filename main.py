#from binascii import a2b_qp
# final from 20/09/2018. To jest ostateczna wersja
import gui
import sqlite3
from tkinter import ttk
###simple password checking method
def haslo():
        a=input("Admin: ")
        p=input("Password: ")
        if a=="admin" and p=="admin":
            print("Ok, you can go")
            root=gui.Tk()
            root.geometry("1600x800+600+300")
            root['bg'] = 'black'
            frmenu = gui.FormMenu(root)
            # frmmenu._init_menu()
            frmenu._init_widgets()

            conn = sqlite3.connect("lcc")
            cur = conn.cursor()
            cur.execute("select* from invoices")
            print(cur.fetchone()[1])
            results = cur.fetchall()
            if __name__ == "__main__":
        #Example(root).pack(fill="both", expand=True)
                root.mainloop()
        else:
            print("Nope, you are not the right person")
            raise NameError("Invalid")
haslo()
