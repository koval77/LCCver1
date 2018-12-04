from tkinter import *
from tkinter.ttk import *
import sql
import sys
from guiwidgets.listview import MultiListbox
from blackbox import _init_toolbar
from datetime import datetime  # to understanding currentdate
import tkinter.messagebox as tkMessageBox

#githubtest
###Form class
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


'''class MyFrame(Frame):
        def __init__(self):
            Frame.__init__(self)
            self.text = Label(self, text='Name')
            self.text.pack()
            self.name = Entry(self)
            self.name.pack()
            self.name.focus_set()
            self.submit = Button(self, text='Submit', width=10,
                                 command=self.callback)
            self.submit.pack()
            self.entered = Label(self, text='You entered: ')
            self.entered.pack()
            vcmd = parent.register(self.validate)
            self.name = Entry(self, validate='key', validatecommand=(vcmd, '%P'))
            self.name.pack()
        def callback(self):
             self.entered.config(text='You entered: ' + self.name.get())
             self.name.delete(0, END)
        def validate(self, P):
             self.submit.config(state=(NORMAL if P else DISABLED))
             return True
        def check(self)
             if self.entered='admin':
                 print("password is ok")'''


class FormMenu:
    """This is the main form that is shown after operator has login.
    It is built from
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
        #self.master.geometry("800x600")
        #self.master.maxsize(800,600)

    def _init_widgets(self):
        # initiate toolbar
        self.toolbar = Frame(self.rootfrm)
        lbl0 = Label(self.toolbar, text='LCC').pack(side=LEFT)
        # butcalc=Button(self.toolbar,text='Calc',command=self.calc_click).pack(side=LEFT)
        # butcalendar=Button(self.toolbar,text='Calander',command=self.calendar_click).pack(side=LEFT)
        self.toolbar.pack(side='top', fill='x')
        # self.proba=Toplevel(self.master)
        # self.proba.frame()
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

        # background image
        # -------------------------------------------
        self.imgback = PhotoImage(file="img/back.gif").subsample(2,3)
        self.lblbackground = Label(self.rootfrm, style="BW.TLabel", borderwidth=0)
        self.lblbackground.pack(side='top',fill='both',ipadx=30,ipady=1)
        self.lblbackground['image'] = self.imgback

    def quit_click(self):
        print("Goodbay")
        sys.exit()

    def vehicle_click(self):
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


#####vehicles class
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

    def btn_edit_click(self):
        print('edit')

    def btn_del_click(self):
        if self.mlb.item_selected == None: return 'please select first'
        print(self.mlb.item_selected[1])
        sql.session._delete_vehicle(int(self.mlb.item_selected[1]))
        self.mlb.delete(self.mlb.item_selected[0])
        self.mlb.item_selected = None

    def btn_find_click(self):
        fnd = self.entryfind.get()

        tbvehicles = sql.session._find_vehicles(fnd)
        self.update_mlb(tbvehicles)

    def update_mlb(self, tb):
        self.mlb.delete(0, END)
        # tbvehicles=sql.session._query(q)
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
    ''' New vehicle, three labels,three textboxes,OK button are added'''

    def __init__(self):
        self.frame = Toplevel()
        self.frame.protocol("WM_DELETE_WINDOW", self.callback)  # user quit the screen
        self._init_widgets()

    def _init_widgets(self):
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


# -----Invoice form-----------------------
class FormInvoices:
    def __init__(self):
        self.frame = Toplevel()
        _init_toolbar(self)
        self._init_gridbox()
        self.frm_addinvoice = None
        self.addinvoiceflag = False
        self.editinvoiceflag = False

    def _init_gridbox(self):
        self.mlb = MultiListbox(self.frame, (('id #', 5), ('Customer', 25), ('Date', 15), ('Grand Total', 15)))
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
