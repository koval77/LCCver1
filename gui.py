from tkinter import *  # importing Tkinter GUI
from tkinter.ttk import *  # importing theme tool kit
import sql  # imports sql which imports sqlite3
import sys  # sys library, used later for finishing application after clicking quit button
from guiwidgets.listview import MultiListbox
from blackbox import _init_toolbar # module for toolbar
from datetime import datetime  # to understanding current date
import tkinter.messagebox as tkMessageBox # for displaying messages
import pickle  # serialization library

def label_entry(frmlblent, txtlbl, txtlbl2=None):
    label = Label(frmlblent, text=txtlbl)
    # The "place" geometry manager organizes widgets in blocks before placing them in the parent widget.
    label.pack(side=LEFT)
    frmlblent._entry = Entry(frmlblent)
    frmlblent._entry.pack(side=LEFT)
    if txtlbl2:
        label2 = Label(frmlblent, text=txtlbl2)
        label2.pack(side=LEFT)
        frmlblent._entry2 = Entry(frmlblent)
        frmlblent._entry2.pack(side=LEFT)

class Employee:
    """Every time new Employee object is instantiated new element is added to the list.
     Apart from following object variables for details there are two magic methods for overloading representations of employee objects
      (I have used them to debug program in the console)."""
    #class variables storing how many new workers are added
    staffAdded_count=0
    staffAdded_list=[]
    def __init__(self, name, surname, address, login, password,salary):
        self.name=name
        self.surname=surname
        self.address=address
        self.login=login
        self.password=password
        self.salary=salary
        #increments number of workers after each initialisation
        Employee.staffAdded_count+=1
        Employee.staffAdded_list.append(self)
        #dunder or magic methods to change functionality of usual operators or functions, here to to represent objects
    def __repr__(self):
        return "Name: "+self.name+" Surname: "+self.surname+" Address: "+self.address+" Login: "+self.login+" Password: "+self.password+" Salary: "+self.salary
    def __str__(self):
        return self.name+self.surname+self.address+self.login+self.password+self.salary
    # def sack(self):
    #     print("{} is being sacked!".format(self.name))
    #
    #     Employee.staff_count -= 1
    #
    #     if Employee.staff_count == 0:
    #         print("{} was the last one.".format(self.name))
    #     else:
    #         print("There are still {:d} people working.".format(
    #             Employee.staff_count))
    #
    # @classmethod
    # def how_many(cls):
    #     """Prints the current workforce number."""
    #     print("We have {:d} robots.".format(cls.staff_count))

class Manager(Employee):
    """Managers are employers that after login will have access to managment options"""
    # def __init__(self):
    #     super().staff_count=list(Manager.read_from_pickle())+super().staff_count+1
    # self.department=departmdent
    # workersList=list(Manager.read_from_pickle())
    # todo
    def __add_bonus(self,to_who,amount):
        pass
    #implementing class/factory by help of decorators to remove employee from gui
    @classmethod
    def addNewEmployeeByManager(cls):
        return cls(4)
    @classmethod
    def removeEmployeeByManager(cls):
        return cls(6)

    @staticmethod
    def delfile():
        open('staff.bin','w').close()

    @staticmethod
    def restlist():
        """This is for resetting pickle with one manager."""
        mng1=Manager("Bill","Gates","USa","bill","bill","30000")
        binary_file = open('staff.bin',mode='wb')
        my_pickled_mary = pickle.dump(mng1, binary_file)
        binary_file.close()

    @staticmethod
    def pickle_updated_list_to_file(x):
        """Taking list as an arguments and iterates through its elements storing them into file. It use ab mode which
        means that elemets are added(not just written which would save only last element from the list.
         The data is unreadable by humans because of b (BINARY) mode. """
        # tym=list(Manager.read_from_pickle())
        # print("tim list before pop: {}".format(tym))
        # tym.pop()
        # print("tim list after pop: {}".format(tym))
        for it in x:
            binary_file = open('staff.bin',mode='ab')
            my_pickled_mary = pickle.dump(it, binary_file)
            binary_file.close()

    #by adding decorator I am creating static method for managers for serialisation
    @staticmethod
    def read_from_pickle():
        """Yields generic iterable. Later I will convert it to list."""
        with open('staff.bin', 'rb') as fileForEmployees:
            try:
                while True:
                    yield pickle.load(fileForEmployees)
            except EOFError:
                pass

    @staticmethod
    def write_object_to_file(who):
        binary_file = open('staff.bin',mode='wb')
        my_pickled_mary = pickle.dump(who, binary_file)
        binary_file.close()

    @staticmethod
    def append_object_to_file(who):
        binary_file = open('staff.bin',mode='ab')
        my_pickled_mary = pickle.dump(who, binary_file)
        binary_file.close()

'''Experimenting in the console part. It provides menu starting menu for adding, listing and deleting employees. 
Choose 0 to skip it and go to man program which will load the Login widget.'''
employees_list=[]
def menu():
    print("*"*80)
    print("Pick your choice:\n0.Exit\n1.Add new employee\n2.List employees\n3.Delete employee\n")

def remove_employee():
    employees_list_toremove=list(Manager.read_from_pickle())
    who_to_remove=str(input("What is the person login?"))
    for sack in employees_list_toremove:
        print("to jest sack:{}".format(sack))
        if sack.__getattribute__("login")=="zosia":
            print("znalazlem zosie!!!!! Zosia lives in{}".format(sack.__getattribute__("address")))
            gdzie=employees_list_toremove.index(sack)
            print("I am deleting element of index: {}".format(gdzie))
        else:
            print("Zosia is not here:(")

choice=""
# mng1=Manager("Bill","Gates","USa","bill","bill","30000")
# clr1=Employee("Jarek","Cash","PL65","jar","jar","600")
# clr2=Employee("Zocha","Zolza","N17as","zocha","zocha","3000")
# employees_list.append(mng1)
# employees_list.append(clr1)
# employees_list.append(clr2)
# Manager.pickle_updated_list_to_file(employees_list)
# Manager.write_object_to_file(mng1)
# Manager.append_object_to_file(clr1)
# Manager.append_object_to_file(clr2)
# filnam=('logins')
# while True:
#     menu()
#     print("type of manager.readfrompicke{}".format(Manager.read_from_pickle()))
#     choice=str(input("What is your choice?"))
#     if choice=="1":
#         print("Give new employee details: Name,Surname,Address,Login,Password,Salary")
#         namen=str(input("Name:"))
#         surnamen= str(input("Surname:"))
#         addressn= str(input("Address:"))
#         loginn=str(input("Login:"))
#         passwordn=str(input("Password:"))
#         salaryn=input("Salary:")
#         clerk_next=Employee(namen,surnamen,addressn,loginn,passwordn,salaryn)
#         employees_list.append(clerk_next)
#         Manager.pickle_updated_list_to_file(employees_list)
#     elif choice=="2":
#         tym=list(Manager.read_from_pickle())
#         print("tym list is: {}".format(tym))
#         for item in tym:
#             print(repr(item))
#             print(type(item))
#     elif choice=="3":
#         print("What is the login name of the person you want to erase?")
#         remove_employee()
#     else:
#         break
# Manager.restlist()
class StaffTableWidget:
    """Tkinter widgets. It uses TopLevel widget which open in separate windows."""
    def __init__(self,dad):
        self.dad=dad
        self._init_widget()
        self.populateTable()
        self.colors()
    def _init_widget(self):
        """Drawing sub-widgets using pack geometry manager. Main part is treeView which is workers table.
        The most important variable is staffTable which is list of employees from file."""
        self.staffList=list(Manager.read_from_pickle())
        self.staffTable=Toplevel(self.dad,width=20,height=100)
        self.staffCountLbl=Label(self.staffTable,text="Workers available")
        self.staffCountLbl.pack(padx=5,pady=5,side=TOP)
        self.staffCountLbl2=Label(self.staffTable,text=len(self.staffList))
        self.staffCountLbl2.pack(padx=5,pady=5,side=TOP)
        self.forNewGuys=LabelFrame(self.staffTable)
        self.forNewGuys.pack(padx=5,pady=5,side=RIGHT)
        self.entryName=Entry(self.forNewGuys)
        self.entryName.pack(padx=5,pady=5,side=TOP)
        self.entrySurname=Entry(self.forNewGuys)
        self.entrySurname.pack(padx=5,pady=5,side=TOP)
        self.entryAddress=Entry(self.forNewGuys)
        self.entryAddress.pack(padx=5,pady=5,side=TOP)
        self.entryLogin=Entry(self.forNewGuys)
        self.entryLogin.pack(padx=5,pady=5,side=TOP)
        self.entryPass=Entry(self.forNewGuys)
        self.entryPass.pack(padx=5,pady=5,side=TOP)
        self.entrySalary=Entry(self.forNewGuys)
        self.entrySalary.pack(padx=5,pady=5,side=TOP)
        self.forbuttons=LabelFrame(self.staffTable)
        self.forbuttons.pack(padx=5,pady=5,side=RIGHT)
        self.newEmpbtn=Button(self.forbuttons,text="New employee",command=self.newEmp)
        self.newEmpbtn.pack(padx=5,side=TOP)
        self.newMngbtn=Button(self.forbuttons,text="New manager",command=self.newMng)
        self.newMngbtn.pack(padx=5,side=TOP)
        self.delemplbtn=Button(self.forbuttons,text="Delete employee",command=self.delete)
        self.delemplbtn.pack(padx=5,side=TOP)
        # self.savebtn=Button(self.forbuttons,text="Save Changes",command=self.updateRec)
        # self.savebtn.pack(padx=5,side=TOP)
        self.myTree=Treeview(self.staffTable,columns=("ID","Name","Surname","Address","Login","Salary","Delete"))
        self.myTree.heading('#0')
        self.myTree.heading('#1', text='ID')
        self.myTree.heading('#2', text='Name')
        self.myTree.heading('#3', text='Surname')
        self.myTree.heading('#4', text='Address')
        self.myTree.heading('#5', text='Login')
        self.myTree.heading('#6', text='Salary')
        # self.myTree.heading('#7', text='Delete')
        self.myTree.column('#0', width=2)
        self.myTree.column('#1', stretch=YES, width=50)
        self.myTree.column('#2', stretch=YES, width=100)
        self.myTree.column('#3', stretch=YES)
        self.myTree.column('#4', stretch=YES)
        self.myTree.column('#5', stretch=YES)
        self.myTree.column('#6', stretch=YES)
        # self.myTree.column('#7', stretch=YES)
        self.myTree.pack()
        # self.myTree.grid(row=4, columnspan=4, sticky='nsew')
        # self.treeview = self.myTree
        # Initialize the counter
        self.i = 0
    def populateTable(self):
        """Inserts values from list into treeView."""
        # self.staffList=list(Manager.read_from_pickle())
        # self.myTree.insert('','end',values=("Alfred","Kowlaksi","Prucha 7","alfi"))
        # self.myTree.insert('','end',values=("Jim","Rotten","nw16as","jim"))
        self.ind=0
        for entry in self.staffList:
            self.ind=self.ind+1
            #  I am using floor division to divide entries on odd and even ones tags.
            if self.ind%2!=0:
                self.myTree.insert('','end',values=(self.ind,entry.__getattribute__("name"),entry.__getattribute__("surname"),
                                                entry.__getattribute__("address"),entry.__getattribute__("login"),
                                                    entry.__getattribute__("salary")),tags = ('oddrow',))
            else:
                self.myTree.insert('','end',values=(self.ind,entry.__getattribute__("name"),entry.__getattribute__("surname"),
                                                    entry.__getattribute__("address"),entry.__getattribute__("login"),
                                                    entry.__getattribute__("salary")),tags = ('evenrow',))
    def colors(self):
        """By using tags change the colors of rows."""
        self.myTree.tag_configure("evenrow",background='white',foreground='black')
        self.myTree.tag_configure("oddrow",background='grey',foreground='black')
    def delete(self):
        """Removing selected row using delete method. Next calls Manager stactic method to update the list."""
        selected_item = self.myTree.selection()[0]  # get selected item
        # print("select_item 1: {}".format(selected_item()[1]))
        for item in self.myTree.selection():
            self.item_text=self.myTree.item(item,"values")
            print(self.item_text)
        self.indtodel=int(self.item_text[0])-1
        for i in range(len(selected_item[3])):
            print("this was in selected items: {}".format(selected_item[3][i]))
        self.myTree.delete(selected_item)
        self.staffList.pop(self.indtodel)
        print("stafflist after pop: {}".format(self.staffList))
        # Manager.restlist()
        Manager.delfile()
        Manager.pickle_updated_list_to_file(self.staffList)
        print("Deleting from table")
    def newEmp(self):
        """Inserts new employee into table and calls updating static method from Mamager."""
        self.nname=self.entryName.get()
        self.nsurname=self.entrySurname.get()
        self.naddress=self.entryAddress.get()
        self.nlogin=self.entryLogin.get()
        self.npassword=self.entryPass.get()
        self.nsalary=self.entrySalary.get()
        empl=Employee(self.nname,self.nsurname,self.naddress,self.nlogin,self.npassword,self.nsalary)
        if self.ind%2!=0:
            self.myTree.insert('','end',values=(self.ind,empl.__getattribute__("name"),empl.__getattribute__("surname"),
                                                empl.__getattribute__("address"),empl.__getattribute__("login"),
                                                empl.__getattribute__("salary")),tags = ('oddrow',))
        else:
            self.myTree.insert('','end',values=(self.ind,empl.__getattribute__("name"),empl.__getattribute__("surname"),
                                                empl.__getattribute__("address"),empl.__getattribute__("login"),
                                                empl.__getattribute__("salary")),tags = ('evenrow',))
        self.staffList.append(empl)
        # Manager.restlist()
        Manager.delfile()
        Manager.pickle_updated_list_to_file(self.staffList)
        print("stafflist after adding new employee: {}".format(self.staffList))
        print("lenght of stafflist after adding new employee: {}".format(len(self.staffList)))
    #  ToDo
    def newMng(self):
        """Creates new manager (same as employee)"""
        pass


    # '''myTree.get_children gives the row id. what i did was get the row id from a loop,
    # then use the id withing myTree.set(id) to get a dictionary of the values. and format the output from there.
    # '''
    # def updateRec(self):
    #
    #     self.list = " "
    #     self.info = self.myTree.get_children()
    #     for i in self.info:
    #         self.info2 = self.myTree.set(i)
    #         for a in self.info2:
    #             print(a,":",self.info2[a])
    #             self.list=self.list + a +": "+ self.info2[a]+'\n'
    #
    #     self.msg ="{} \n" .format(self.list)
    #     print("list from updatereC: {}".format(self.list))

class Login:
    """Login screen. This class is responsible for logging and checking credentials."""
    def __init__(self, parent):
        """Initialising widget and setting styling theme using ttk funcion."""
        self.parent=parent
        parent.title("London Car Company Sales System")
        s=Style()
        #applying the chosen theme to all existing widgets
        s.theme_use(themename='clam')
        self._init_widget()

    def check_password(self):
        """Use Tkinter variables to read values from entered credentials. Iterates through all objects in employee list to check if there a match,
         between entered values, and attributes of the object retrieved by _getattribute__ function. If credentaials are valid the state of
         managments buttons are changed. If object is instance of Managers all of the buttons are enabled."""
        self.username=""
        self.password=""
        self.username=self.us_name_to_function.get()
        self.password=self.us_pass_to_function.get()
        self.credentialCheck=False
        #creating list of objects from Employee class (and Manager subclass) from pickle
        listOfStaff=list(Manager.read_from_pickle())
        # print("(debugging) listOfStaff is :{}".format(listOfStaff))
        for people in listOfStaff:
            if people.__getattribute__("login")==self.username and people.__getattribute__("password")==self.password:
                print("login and password is correct")
                #if credentials are correct, enable starting application button
                self.close_button['state']=NORMAL
                #assign to bool variable isinstance builtins function. It will be true if object is of class Manager
                checkForRole=isinstance(people,Manager)
                #if credentials belongs to manager, the group of corresponding buttons will be enabled
                if checkForRole:
                    self.addEmployee['state']=NORMAL
                    self.removeEmployee['state']=NORMAL
                    self.helpButton['state']=NORMAL
                tkMessageBox.showinfo("Success", "Login Successful!")
                self.credentialCheck=True
                break
            else:
                print("Incorrect details")
                print("username is:{}".format(self.username))
        if self.credentialCheck==False:
         tkMessageBox.showinfo("Failed","Please enter the correct username and password!")

    def check_passwordOldVersion(self):
        self.username=""
        self.password=""
        self.username=self.us_name_to_function.get()
        self.password=self.us_pass_to_function.get()
        if self.username=="admin":
            print("username is admin !!!")
            self.close_button['state']=NORMAL
        else:
            print("username is not admin")
            print("username is:{}".format(self.username))

        while (self.username != "admin" or self.password != "admin"):
                tkMessageBox.showinfo("Failed","Please enter the correct username and password!")
                self.odp="pop"
                return self.odp

        tkMessageBox.showinfo("Success", "Login Successful!")
        #self.destroy()
        return

    def wypad(self):
        print("Jestem w wypad!!!!!!!!!!!!!")
        sys.exit()

    #Method for initialisating widget for employees table
    def listStaffTopWidget(self):
        self.staffTable=StaffTableWidget(self.parent)

    def _init_widget(self):
        """Weakly private method drawing Tkinter widgets. Grid geometry is used this time."""
        #Using Tkinter variables
        self.us_name_to_function=StringVar()
        self.us_pass_to_function=StringVar()
        #Widget for group of child buttons
        self.buttonsPanel=LabelFrame(self.parent)
        self.buttonsPanel.grid(row=4,column=1,columnspan=4,sticky="W")
        #alternatively could have use parent.destroy maybe (or is it only for pack?)
        self.close_button = Button(self.buttonsPanel, text="Start the application",state=DISABLED, command=self.parent.quit, width=20)
        self.close_button.grid(row=5,column=1,sticky="W",padx=10,pady=1)
        #providing handler for method which will create staff table widget. Disabled by default.
        self.removeEmployee = Button(self.buttonsPanel,text=" Employee List",state=DISABLED, width=20, command=self.listStaffTopWidget)
        self.removeEmployee.grid(row=6,column=1,sticky="W",padx=10,pady=1)
        self.addEmployee = Button(self.buttonsPanel,text="Add new employee",state=DISABLED, width=20)
        self.addEmployee.grid(row=7,column=1,sticky="W",padx=10,pady=1)
        self.helpButton = Button(self.buttonsPanel,text="Help",state=DISABLED, width=20)
        self.helpButton.grid(row=8,column=1,sticky="W",padx=10,pady=1)
        self.background_label =Label(self.parent,text="London Car Company",font=("Helvetica",20,"bold"))
        self.background_label.grid(row=2,column=1,sticky="W")
        self.user=Label(self.parent,text="Username:",font=20)
        self.user.grid(row=3,column=1,padx=450,sticky="w")
        self.username=Entry(self.parent,width=40, textvariable=self.us_name_to_function)
        self.username.grid(row=3,column=1,padx=550,sticky="w")
        self.passwordLabel=Label(self.parent,text="Password:",font=20)
        self.passwordLabel.grid(row=4,column=1,padx=450,sticky="w",pady=5)
        self.password=Entry(self.parent,width=40,show="*", textvariable=self.us_pass_to_function)
        self.password.grid(row=4,column=1,padx=550,sticky="w")
        self.btnLogin=Button(self.parent,text="Login",width=10,command=self.check_password)
        self.btnLogin.grid(row=5,column=1,sticky="w",padx=620)

class FormMenu():
    """This is the main form being displayed after operator has valid credentials after clicking Start Application button.
    The main parts:
    -----------------------
    --++> Label that display LCC.
        --++> Vehicles-   OnClick display FormVehicles,
        --++> Invoices-   OnClick display FormInvoices,
        --++> Customers-  OnClick display FormCustomers
    --++> An Image
    """
    def __init__(self, rootfrm):
        self.rootfrm = rootfrm
        self.frm_invoices = None
        self._init_widgets()

    def _init_widgets(self):
        """Again weakly private method (I will be using similar pattern for all drawing classes below) for drawing. """
        # initiate toolbar
        self.toolbar = Frame(self.rootfrm)
        lbl0 = Label(self.toolbar, text='LCC').pack(side=LEFT)
        self.toolbar.pack(side='top', fill='x')
        style = Style()
        style.configure("BW.TLabel", foreground="white", background="black")
        # buttons frame
        # --------------------------------------------
        self.buttons = Frame(self.rootfrm, style="BW.TLabel")
        # button for vehicles
        self.btnvehicles = Button(self.buttons, command=self.vehicle_click)
        self.imgprdt = PhotoImage(file="img/vehicles.gif")
        self.btnvehicles['image'] = self.imgprdt
        self.btnvehicles.pack(side='top')  # , fill='x')
        lbl1 = Label(self.buttons, text="Vehicles", style="BW.TLabel").pack()
        # button for invoices
        self.btninvoices = Button(self.buttons, text='Invoices', command=self.invoices_click)
        self.imginv = PhotoImage(file="img/invoices.gif")
        self.btninvoices['image'] = self.imginv
        self.btninvoices.pack(side='top')
        lbl2 = Label(self.buttons, text="Invoices", style="BW.TLabel").pack()
        # button for customers
        self.btncustomers = Button(self.buttons, text='Customers', command=self.customers_click)
        self.imgcust = PhotoImage(file="img/customers.gif")
        self.btncustomers['image'] = self.imgcust
        self.btncustomers.pack(side='top')
        lbl3 = Label(self.buttons, text="Customers", style="BW.TLabel").pack()
        # quit button
        self.btnquit = Button(self.buttons, text='Quit', command=self.quit_click)
        self.imgquit = PhotoImage(file="img/quit.gif")
        self.btnquit['image'] = self.imgquit
        self.btnquit.pack(side='top')
        lbl4 = Label(self.buttons, text="Quit", style="BW.TLabel").pack()
        self.buttons.pack(side='left', padx=10)
        #Background,subsample changes dimensions
        self.imgback = PhotoImage(file="img/back.gif").subsample(2,3)
        self.lblbackground = Label(self.rootfrm, style="BW.TLabel", borderwidth=0)
        self.lblbackground.pack(side='top',fill='both',ipadx=30,ipady=1)
        self.lblbackground['image'] = self.imgback

    def quit_click(self):
        """Uses sys standard Python library for finishing the application."""
        print("Goodbay")
        sys.exit()

    def vehicle_click(self):
        """Disabling and enabling corresponding buttons after clicking vehicle."""
        print("vehicles")
        self.btnvehicles['state'] = DISABLED
        self.btninvoices['state'] = DISABLED
        self.btncustomers['state'] = DISABLED
        self.frm_vehicles = FormVehicles()
        self.rootfrm.wait_window(self.frm_vehicles.frame)
        self.btnvehicles['state'] = NORMAL
        self.btninvoices['state'] = NORMAL
        self.btncustomers['state'] = NORMAL

    def invoices_click(self):
        """Disabling and enabling corresponding buttons after clicking invoice."""
        print("invoices")
        self.btnvehicles['state'] = DISABLED
        self.btninvoices['state'] = DISABLED
        self.btncustomers['state'] = DISABLED
        self.frm_invoices = FormInvoices()
        self.rootfrm.wait_window(self.frm_invoices.frame)
        self.btnvehicles['state'] = NORMAL
        self.btninvoices['state'] = NORMAL
        self.btncustomers['state'] = NORMAL

    def customers_click(self):
        """Disabling and enabling corresponding buttons after clicking customer."""
        print("customers")
        self.btnvehicles['state'] = DISABLED
        self.btninvoices['state'] = DISABLED
        self.btncustomers['state'] = DISABLED
        self.frm_customers = FormCustomers()
        self.rootfrm.wait_window(self.frm_customers.frame)
        self.btnvehicles['state'] = NORMAL
        self.btninvoices['state'] = NORMAL
        self.btncustomers['state'] = NORMAL
        print("customers alle co dalej?")

# # #Menu form finished here
#####VehiclesForm class
class FormVehicles:
    '''The Vehicles window with toolbar and a datagrid of cars'''

    def __init__(self):
        self.frame = Toplevel()
        _init_toolbar(self)
        self._init_gridbox()
        self.frm_addvehicle = None
        self.frm_editvehicle = None
        self.addvehicleflag = False

    def _init_gridbox(self):
        self.mlb = MultiListbox(self.frame, (
        ('id #', 3), ('vehicle', 25), ('Description', 25), ('Price', 12), ('PlateNumber', 10), ('Year', 12)))
        tbvehicles = sql.session._query("select * from vehicles")
        self.update_mlb(tbvehicles)
        self.mlb.pack(expand=YES, fill=BOTH)

    # form vehicles add button clicked()
    def btn_add_click(self):
        if self.addvehicleflag: return 0
        print('not exist')
        self.addvehicleflag = True
        self.frm_addvehicle = FormAddvehicle()
        self.frame.wait_window(self.frm_addvehicle.frame)
        if self.frm_addvehicle._okbtn_clicked == 1:
            tbvehicle = sql.session._query("select * from vehicles")
            self.update_mlb(tbvehicle)
        self.addvehicleflag = False

    #ToDo
    def btn_edit_click(self):
        print('edit')

    def btn_del_click(self):
        if self.mlb.item_selected == None: return 'please select first'
        print(self.mlb.item_selected[1])
        sql.session._delete_vehicle(int(self.mlb.item_selected[1]))
        self.mlb.delete(self.mlb.item_selected[0])
        self.mlb.item_selected = None
    #ToDo
    def btn_find_click(self):
        fnd = self.entryfind.get()

        tbvehicles = sql.session._find_vehicles(fnd)
        self.update_mlb(tbvehicles)

    def update_mlb(self, tb):
        self.mlb.delete(0, END)
        for row in tb:
            self.mlb.insert(END, (int(row[0]),
                                  row[1],
                                  row[2],
                                  int(row[3]),
                                  row[4],
                                  row[5]))
# Vehicle form finishes here

# ---------------Form add vehicle class---------------------

class FormAddvehicle:
    """New vehicle, three labels,three textboxes,OK button are added. TopLevel widget for adding,
    deleting vehicles here and into sql."""
    def __init__(self):
        self.frame = Toplevel()
        self.frame.protocol("WM_DELETE_WINDOW", self.callback)  # user quit the screen
        self._init_widgets()

    def _init_widgets(self):
        """Weakly private method for drawing Tkinter widgets."""
        self.label1 = Label(self.frame, text="Vehicle #")
        self.label1.grid(row=0, sticky=W)
        self.entry1 = Entry(self.frame)
        self.entry1.grid(row=1, column=0)
        self.label2 = Label(self.frame, text="Sales Price")
        self.label2.grid(row=1, column=1, sticky=W)
        self.entry2 = Entry(self.frame)
        self.entry2.grid(row=2, column=1)
        self.label3 = Label(self.frame, text="Description.")
        self.label3.grid(row=3, sticky=W, columnspan=2)
        self.entry3 = Entry(self.frame)
        self.entry3.grid(row=4, sticky=W + E, columnspan=2)
        self.label4 = Label(self.frame, text="PlateNumber.")
        self.label4.grid(row=5, sticky=W, columnspan=2)
        self.entry4 = Entry(self.frame)
        self.entry4.grid(row=6, sticky=W + E, columnspan=2)
        self.label5 = Label(self.frame, text="Year.")
        self.label5.grid(row=7, sticky=W, columnspan=2)
        self.entry5 = Entry(self.frame)
        self.entry5.grid(row=8, sticky=W + E, columnspan=2)
        self.btn_ok = Button(self.frame, text="OK", width=7, command=self.btn_ok_click)
        self.btn_ok.grid(row=9, column=1, sticky=E)

    def btn_ok_click(self):
        """Read values from entry widgets. Checks if every entry is filled and send it to sql.
        Destroys the frame (this window) at the end."""
        items = (self.entry1.get(), self.entry3.get(), int(self.entry2.get()), self.entry4.get(), self.entry5.get())
        if '' in items:
            print('please fill everywhere')
            return 'break'
        sql.session._add_vehicle(items)
        self._okbtn_clicked = 1
        print('operator exits clicking ok button')
        self.frame.destroy()

    def callback(self):
        self._okbtn_clicked = 0
        print('operator exits the screen')
        self.frame.destroy()
# AddVehicle for finishes here------------------

class FormInvoices:
    """TopLevel widget for browsing, adding and editing invoices here in the GUI and into sql."""
    def __init__(self):
        self.frame = Toplevel()
        _init_toolbar(self)
        self._init_gridbox()
        self.frm_addinvoice = None
        self.addinvoiceflag = False
        self.editinvoiceflag = False

    def _init_gridbox(self):
        self.mlb = MultiListbox(self.frame, (('id #', 5), ('Customer', 25), ('Date', 15), ('Total Amount', 15)))
        tbvehicles = sql.session._query("select * from invoices")
        self.update_mlb(tbvehicles)
        self.mlb.pack(expand=YES, fill=BOTH)

    def update_mlb(self, tb):
        self.mlb.delete(0, END)
        for row in tb:
            self.mlb.insert(END, (int(row[0]),
                                  row[1],
                                  row[2],
                                  int(row[3])))
        self.mlb.selection_set(0)  # set first row selected

    def btn_add_click(self):
        print('check if addwindow exist. If not, cmd will inform about it')
        if self.addinvoiceflag: return 0
        print('not existing')
        self.addinvoiceflag = True
        self.frm_addinvoice = FormAddInvoice()
        self.frame.wait_window(self.frm_addinvoice.master)
        print('form addinvoice does not exist. Add button will work')
        self.addinvoiceflag = False

    def btn_edit_click(self):
        if self.editinvoiceflag: return 0
        self.editinvoiceflag = True
        self.frm_editinvoice = FormEditInvoice()
        self.frm_editinvoice.init_entryboxes(self.mlb.item_selected[1:])  # (id,customer,date,amount)
        tbinvitems = sql.session._show_invoice(self.mlb.item_selected[1])
        self.frm_editinvoice.update_mlbitems(tbinvitems)
        self.frame.wait_window(self.frm_editinvoice.master)
        self.editinvoiceflag = False

    def btn_del_click(self):
        if self.mlb.item_selected == None: return 'please select first'
        print(self.mlb.item_selected[1])
        sql.session._delete_invoice(int(self.mlb.item_selected[1]))
        self.mlb.delete(self.mlb.item_selected[0])
        self.mlb.item_selected = None

    def btn_find_click(self):
        print('find')

# Invoice form finishes here-------------------------------

# Addinvoice form class------------------------------------------
class FormAddInvoice:
    '''New vehicles, three labels, three textboxes, OK button are added'''
    def __init__(self):
        self.master = Toplevel()
        self.master.protocol("WM_DELETE_WINDOW", self.callback)  # user quits
        self._init_widgets()

    def _init_widgets(self):
        self.frame0 = Frame(self.master)
        label_entry(self.frame0, 'Invoice# :')
        rowid = sql.session._next_invoiceid()
        self.frame0._entry.insert(END, str(rowid))
        self.frame0._entry['state'] = DISABLED
        self.frame0.pack(side=TOP)
        # frame1- lblinvoice, lbl_date, btn_date
        self.frame1 = Frame(self.master)
        label_entry(self.frame1, 'Customer:')
        self.lbl_date = Label(self.frame1, text='Date:' + str(datetime.today())[:10])
        self.lbl_date.pack(side=LEFT)
        self.btn_date = Button(self.frame1, text="PickDate", width=8,
                               command=self.btn_date_click)
        self.btn_date.pack(side=LEFT)
        self.frame1.pack(side=TOP)

        # frame2: lookuplist
        self.frame2 = LookupList(self.master)
        self.frame2.ent.focus()  # focusing to entry vehicle

        # frame3- quantity, ent_qty, btn_additem
        self.frame3 = Frame(self.master)
        self.lbl3_1 = Label(self.frame3, text="Quantity")
        self.lbl3_1.pack(side=LEFT)
        self.ent_qty = Entry(self.frame3)
        self.ent_qty.pack(side=LEFT)
        self.btn_additem = Button(self.frame3, text="AddItem", width=8,
                                  command=self.btn_additem_click)
        self.btn_additem.pack(side=LEFT)
        self.frame3.pack(side=TOP)

        # frame4- mlbitems
        self.frame4 = Frame(self.master)
        self.mlbitems = MultiListbox(self.frame4, (('LN#', 4), ('ID#', 6),
                                                   ('vehicle', 15), ('Quantity', 5), ('Description', 20),
                                                   ('UnitPrice', 10), ('Total', 10)))
        self.mlbitems.not_focus()  # don't take_focus
        self.mlbitems.pack(expand=YES, fill=BOTH, side=TOP)
        self.frame4.pack(side=TOP)

        # frame5-netamount-stringvar, paid, balance
        self.frame5 = Frame(self.master)
        self.lbl5_1 = Label(self.frame5, text="Net:")
        self.lbl5_1.pack(side=LEFT)
        self.netamount = StringVar()
        self.netamount.set('0')
        self.lbl5_2 = Label(self.frame5, textvariable=self.netamount, font=("Helvetica", 16))
        self.lbl5_2.pack(side=LEFT)
        self.lbl5_3 = Label(self.frame5, text="paid:")
        self.lbl5_3.pack(side=LEFT)
        self.ent_paid = Entry(self.frame5)
        self.ent_paid.pack(side=LEFT)
        self.ent_paid.bind("<KeyRelease>", self.ent_paid_change)
        self.balanceamount = StringVar()
        self.lbl5_4 = Label(self.frame5, text="Balance: ").pack(side=LEFT)
        # self.balanceamount.set('balance:')
        self.lblbal = Label(self.frame5, textvariable=self.balanceamount,
                            foreground='red', font=("Helvetica", 22)).pack(side=LEFT)
        self.frame5.pack(side=TOP)
        self.btn_ok = Button(self.master, text="OK", width=7, command=self.btnok_click)
        self.btn_ok.pack(side=TOP)

    def add_item(self):
        qty = self.ent_qty.get()
        if qty == '':
            print('no quantity set')
            return 0
        qty = int(qty)
        LN = self.mlbitems.size() + 1
        r, i_d, prdct, desc, price = self.frame2.mlb.item_selected
        self.mlbitems.insert(END, (LN, i_d, prdct, qty, desc, price, price * qty))
        net_amt = int(self.netamount.get()) + (price * qty)
        self.netamount.set(str(net_amt))
        self.frame2.ent.delete(0, END)  # clear entry vehicle
        self.ent_qty.delete(0, END)  # clear enter field for quantity
        self.frame2.ent.focus()  # focusing vehicle entry field

    def btn_date_click(self):
        print('date')

    def ent_paid_change(self, event):
        paid = self.ent_paid.get()
        if paid == '':
            return 0
        bal = int(paid) - int(self.netamount.get())
        self.balanceamount.set(str(bal))

    def btn_additem_click(self):
        self.add_item()

    def btnok_click(self):
        no_of_items = self.mlbitems.size()
        if no_of_items == 0:
            print('please select your vehicles first')
            return '0'
        print('okbutton clicked')
        i_d = int(self.frame0._entry.get())  # invoiceid
        tbinvitems_items = []
        for item in range(no_of_items):
            temp1 = self.mlbitems.get(item)
            tbinvitems_items.append((temp1[0],
                                     i_d, temp1[1], temp1[3],))

        tbinv_item = (i_d, self.frame1._entry.get(),
                      str(datetime.today())[:10], int(self.netamount.get()))
        sql.session._add_invoice(tbinv_item, tbinvitems_items)
        self._okbtn_clicked = 1
        print('operator quit by clicking ok button')
        self.master.destroy()

    def callback(self):

        self._okbtn_clicked = 0
        print('operator close window')
        self.master.destroy()


# class for LookupList
# Entry box and mlb for class FormAddInvoice
class LookupList:
    def __init__(self, master):
        self.frame = Frame(master)
        self.le_frame = Frame(self.frame)
        self.tblookup = sql.session
        lbl = Label(self.le_frame, text="vehicle").pack(side=LEFT)
        self.ent = Entry(self.le_frame)
        self.ent.pack(side=LEFT)
        self.ent.bind("<KeyRelease>", self.txtchange)  # <Key>",self.keypressed)
        self.le_frame.pack(side=TOP)
        self._init_gridbox()
        self.frame.pack(side=TOP, expand=NO)

    def _init_gridbox(self):
        self.mlb = MultiListbox(self.frame, (('id #', 5), ('Vehicle', 20), ('Type', 30), ('UnitPrice', 15)))
        self.update_mlb('')
        self.mlb.not_focus()
        self.mlb.pack(expand=YES, fill=BOTH, side=TOP)

    def txtchange(self, event):
        txtent = self.ent.get()
        self.update_mlb(txtent)

    def update_mlb(self, val):
        x = self.tblookup._query("select * from vehicles where name like '%" + val + "%' order by name")
        self.mlb.delete(0, END)
        for row in x:
            self.mlb.insert(END, (int(row[0]),
                                  row[1],
                                  row[2],
                                  int(row[3])))
        self.mlb.selection_set(0)  # setting first of the rows which is selected


# Class FormAddInvoice finishes here---------------------


# formeditinvoice class--------------------------

class FormEditInvoice:
    def __init__(self):
        self.master = Toplevel()
        self.frame1 = Frame(self.master)
        label_entry(self.frame1, 'Invoice#:')
        self.frame1.pack(side=TOP)

        self.frame2 = Frame(self.master)
        label_entry(self.frame2, 'Customer:', 'Date:')
        self.frame2.pack(side=TOP)

        lblprod = Label(self.master, text='Items').pack(side=TOP)
        self.frame3 = Frame(self.master)
        self.mlbitems = MultiListbox(self.frame3, (('LN#', 5),
                                                   ('Vehicle', 15), ('Quantity', 5), ('Type', 20),
                                                   ('UnitPrice', 10), ('Total', 10)))
        self.mlbitems.not_focus()
        self.mlbitems.pack(expand=YES, fill=BOTH, side=TOP)
        self.frame3.pack(side=TOP)

        self.frame4 = Frame(self.master)
        label_entry(self.frame4, 'Total amount:')
        self.frame4.pack(side=TOP)

    def init_entryboxes(self, val):
        self.frame1._entry.insert(END, val[0])
        self.frame1._entry['state'] = DISABLED
        self.frame2._entry.insert(END, val[1])
        self.frame2._entry2.insert(END, val[2])
        self.frame2._entry['state'] = DISABLED
        self.frame2._entry2['state'] = DISABLED
        self.frame4._entry.insert(END, val[3])
        self.frame4._entry['state'] = DISABLED

    def update_mlbitems(self, invitems):
        self.mlbitems.delete(0, END)
        for row in invitems:
            self.mlbitems.insert(END, (row[0], row[1], row[2], row[3], row[4], row[5]))
        self.mlbitems.selection_set(0)  # setting the first row which is selected


###Class of the FormCustomer
class FormCustomers:
    # The Vehicles window with toolbar and a datagrid
    def __init__(self):
        self.frame = Toplevel()
        _init_toolbar(self)
        self._init_gridbox()
        self.frm_addcustomers = None
        self.frm_editcustomers = None
        self.addcustomersflag = False  # frmaddvehicle doesn't exist

    def _init_gridbox(self):
        self.mlb = MultiListbox(self.frame, (('cusid #', 3), ('cusname', 25), ('cusad', 25)))
        tbcustomers = sql.session._query("select * from customers")
        self.update_mlb(tbcustomers)
        self.mlb.pack(expand=YES, fill=BOTH)

    # button is clicked() for form add vehicles
    def btn_add_click(self):
        if self.addcustomersflag: return 0
        print('not exist')
        self.addcustomersflag = True
        self.frm_addcustomer = FormAddCustomer()
        self.frame.wait_window(self.frm_addcustomer.frame)
        if self.frm_addcustomer._okbtn_clicked == 1:
            tbcustomers = sql.session._query("select * from customers")
            self.update_mlb(tbcustomers)
        self.addcustomerflag = False

    def btn_edit_click(self):
        print('edit')

    def btn_del_click(self):
        if self.mlb.item_selected == None: return 'Could you select first one, please?'
        print(self.mlb.item_selected[1])
        sql.session._delete_vehicle(int(self.mlb.item_selected[1]))
        self.mlb.delete(self.mlb.item_selected[0])
        self.mlb.item_selected = None

    def btn_find_click(self):
        fnd = self.entryfind.get()

        tbcustomers = sql.session._find_customers(fnd)
        self.update_mlb(tbcustomers)

    def update_mlb(self, tb):
        self.mlb.delete(0, END)
        # tbvehicles=sql.session._query(q)
        for row in tb:
            self.mlb.insert(END, (int(row[0]),
                                  row[1],
                                  row[2],))


# FormCustomer class ends here--------


# Class formaddcustomer---------------------------------------

class FormAddCustomer:
    '''Adding New vehicles,3 labels,3 textboxes, OK button'''

    def __init__(self):
        self.frame = Toplevel()
        self.frame.protocol("WM_DELETE_WINDOW", self.callback)  # operator close window
        self._init_widgets()

    def _init_widgets(self):
        self.label2 = Label(self.frame, text="CusName")
        self.label2.grid(row=0, column=1, sticky=W)
        self.entry2 = Entry(self.frame)
        self.entry2.grid(row=1, column=1)

        self.label3 = Label(self.frame, text="CusAddress.")
        self.label3.grid(row=2, sticky=W, columnspan=2)
        self.entry3 = Entry(self.frame)
        self.entry3.grid(row=3, sticky=W + E, columnspan=2)

        self.btn_ok = Button(self.frame, text="OK", width=7, command=self.btnok_click)
        self.btn_ok.grid(row=4, column=1, sticky=E)

    def btnok_click(self):
        items = (self.entry2.get(), self.entry3.get())
        if '' in items:
            print('Fill all fields, please')
            return 'break'
        sql.session._add_customer(items)

        self._okbtn_clicked = 1
        print('operator close the window by clicking ok button')
        self.frame.destroy()

    def callback(self):
        self._okbtn_clicked = 0
        print('operator close window')
        self.frame.destroy()

# Class FormAddCustomers ends here--------------------------------
