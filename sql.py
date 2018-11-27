import sqlite3

class DB_SESSION:
    def __init__(self,conn):
        self.conn=conn
        self.cur=self.conn.cursor()

    def _query(self,q="""SELECT * from invoices"""):
        self.cur.execute(q)
        return self.cur.fetchall()
    def _find_vehicles(self,val):
        print (val)
        self.cur.execute("select * from vehicles where name like '%"+val+"%'")
        return self.cur.fetchall()
    def _find_customers(self,val):
        print(val)
        self.cur.execute("select * from customers where cusname like '%"+val+"%'")
        return self.cur.fetchall()
    def _delete_invoice(self,i_d):
        t=(i_d,)
        self.cur.execute('DELETE FROM invoices WHERE id=?',t)
        self.cur.execute('DELETE FROM invoiceitems WHERE invoiceid=?',t)
        self.conn.commit()

    def _add_vehicle(self,items):
        self.cur.execute('select MAX(id) from vehicles')
        i_d=self.cur.fetchone()[0] + 1
        items=(i_d,)+items
        self.cur.execute('INSERT INTO vehicles VALUES (?,?,?,?,?,?)',items)
        self.conn.commit()

    def _add_customer(self,items):
        self.cur.execute('select MAX(cusid) from customers')
        i_d=self.cur.fetchone()[0] + 1
        items=(i_d,)+items
        self.cur.execute('INSERT INTO customers VALUES (?,?,?)',items)
        self.conn.commit()

    def _add_invoice(self,inv,items):
        #items is a list comprising (id, invoiceid, vehicleid, quantity)
        #inv is a tuple comprising (id,customer, date, amount)
        self.cur.execute('INSERT INTO invoices VALUES (?,?,?,?)',inv)
        for t in items:
            self.cur.execute('INSERT INTO invoiceitems VALUES (?,?,?,?)',t)
        self.conn.commit()
        
    def _add_vehicle_cmd(self):
        self.cur.execute('select MAX(id) from vehicles')
        i_d=self.cur.fetchone()[0] + 1
        items=[]
        while True:
            name=input('Vehicle Model: ')
            if name =='': break
            desc=input('Vehicle type: ')
            price=input('Price: ')
            t=(i_d,name,desc,int(price))
            self.cur.execute('insert into vehicles values (?,?,?,?)', t)
            i_d+=1
        self.conn.commit()
    def _show_invoice(self,i_d):
        t=(i_d,)
        self.cur.execute('''select invoiceitems.id,name,quantity,description,price,price*quantity
        from invoiceitems,vehicles
        where invoiceitems.vehicleid=vehicles.id
        and invoiceitems.invoiceid=?''', t)
        return self.cur.fetchall()
    def _delete_vehicle(self,i_d):
        t=(i_d,)
        self.cur.execute('DELETE FROM vehicles WHERE id=?',t)
        self.conn.commit()
    def _delete_customer(self,i_d):
        t=(i_d,)
        self.cur.execute('DELETE FROM customers WHERE cusid=?',t)
        self.conn.commit()
    def close(self):
        self.conn.close()
    def _next_invoiceid(self):
        self.cur.execute('select MAX(id) from invoices')
        i_d=self.cur.fetchone()[0] + 1
        return i_d
'''    
    def _add_invoice(self):
        query="INSERT INTO invoices VALUES (0,'',0,0)"
        c=self.conn.cursor()
        c.execute(query)
        self.conn.commit()
        print (self._last_rowid())                       
    def _add_invoice_items(self):
        pass    
    def _update(self):
        query='UPDATE invoices SET invoiceid=4 WHERE id = "Smith"';        
    def _last_rowid(self):
        return int(self.c.lastrowid)
'''
session=DB_SESSION(sqlite3.connect('lcc'))
