from tkinter import Tk, Label, Button
import pickle

employees_list=[]
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()
        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

class Employee:
    def __init__(self, name, surname, address, login, password):
        self.name=name
        self.surname=surname
        self.address=address
        self.login=login
        self.password=password
    def __repr__(self):
        return "Name: "+self.name+" Surname: "+self.surname+" Address: "+self.address+" Login: "+self.login
    def __str__(self):
        return self.name+self.surname+self.address+self.login

def menu():
    print("*"*80)
    print("Pick your choice:\n0.Exit\n1.Add new employee\n2.List employees\n3.Delete employee\n")
def read_from_pickle():
    with open('employees.bin', 'rb') as file:
        try:
            while True:
                yield pickle.load(file)
        except EOFError:
            pass

def remove_employee():
    employees_list_toremove=list(read_from_pickle())
    who_to_remove=str(input("What is the person login?"))
    for sack in employees_list_toremove:
        print("to jest sack:{}".format(sack))
        # print(("And this is type of sack: {}".format(type(sack))))
        # ind=0
        # while ind<len(employees_list_toremove):
        if sack.__getattribute__("login")=="zosia":
                 print("znalazlem zosie kurwa!!!!! Zosia lives in{}".format(sack.__getattribute__("address")))
                 gdzie=employees_list_toremove.index(sack)
                 print("I am deleting element of index: {}".format(gdzie))
        else:
            print("Zosia is not here:(")

for item in read_from_pickle():
    print(repr(item))

choice=""
filnam=('logins')
while True:
    menu()
    choice=str(input("What is your choice?"))
    if choice=="1":
        print("Give new employee details: login,password/saving dictionarty")
        namen=str(input("Name:"))
        surnamen= str(input("Surname:"))
        addressn= str(input("Address:"))
        loginn=str(input("Login:"))
        passwordn=str(input("Password:"))
        clerk_next=Employee(namen,surnamen,addressn,loginn,passwordn)
        employees_list.append(clerk_next)
        binary_file = open('employees.bin',mode='ab')
        my_pickled_mary = pickle.dump(clerk_next, binary_file)
        binary_file.close()
    elif choice=="2":
        read_from_pickle()
        for item in read_from_pickle():
             print(repr(item))
    elif choice=="3":
        print("What is the login name of the person you want to erase?")
        remove_employee()
    else:
        break

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()