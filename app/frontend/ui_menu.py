from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# date methodes and widgets
from tkcalendar import DateEntry
from datetime import datetime
# Import class connexion database
from backend.connexion import Connexion
# Import class Product
from backend.product import Product
# Import GUI user
from frontend.ui_user import Ui_User


class Ui_Menu():
    def __init__(self,parent,id,username):

        # Variables
        self.parent =parent

        self.id = id
        self.username = username

        self.id_product = None

        self.db = Connexion()
        
        # Declare Window
        self.parent.title("Menu")
        self.parent.geometry("1200x600+20+20")
        self.parent.config(bg="#fff")
        self.parent.resizable(False,False)

        # Create a Label widget
        self.label_title = Label(self.parent, text='Product Management System', font=('Arial', 16),bg="white")
        self.label_title.pack(side='top', padx=10, pady=10)

        # Frame
        self.frame = Frame(width=700,height=450,bg='red')
        self.frame.place(x=40,y=50)

        # Create Treeview
        self.tree = ttk.Treeview(self.frame, height=20,columns=('id','user','name', 'description', 'price',  'quantity', 'alert','last_entry_date','last_exit_day'))

        # Create Column
        self.tree.column("#0",width=0,minwidth=0)
        self.tree.column("id",width=25,minwidth=0)
        self.tree.column("user",width=75,minwidth=0)
        self.tree.column('name', width=75,anchor=W)
        self.tree.column('description', width=200)
        self.tree.column('price', width=40,anchor=CENTER)
        self.tree.column('quantity', width=55,anchor=CENTER)
        self.tree.column('alert', width=40,anchor=CENTER)
        self.tree.column('last_entry_date', width=100)
        self.tree.column('last_exit_day', width=100)

        # Create heading
        self.tree.heading("#0",text="#")
        self.tree.heading("id",text="Id")
        self.tree.heading("user",text="User")
        self.tree.heading('name', text='Name')
        self.tree.heading('description', text='Description')
        self.tree.heading('price', text='Price')
        self.tree.heading('quantity', text='Quantity')
        self.tree.heading('alert', text='Alert')
        self.tree.heading('last_entry_date', text='last entry date')
        self.tree.heading('last_exit_day', text='last exit date')

        # Frame
        self.frame_box = Frame(width=350,height=500,bg='white')
        self.frame_box.place(x=800,y=50)

        # Pack the Treeview widget, Label widget, and Button widgets in the parent window
        self.tree.pack(side='left',fill='both', expand=True,anchor=W)

        # ----------------------Create Boxs----------------------

        self.title_label = Label(self.frame_box,text="Manager Product",fg="black",bg="white",font=("Microsoft YaHei UI light",18,"bold"))
        self.title_label.pack(pady=15)

        # create label and entry widgets for product name
        self.name_label = Label(self.frame_box, text="Product Name:",fg="black",bg="white",font=("Microsoft YaHei UI light",10,"bold"))
        self.name_entry = Entry(self.frame_box,width=50,border=0,fg="black",bg="white",font=("Microsoft YaHei UI light",8,))
        self.name_label.pack(padx=20, pady=5,side=TOP, anchor=NW)
        self.name_entry.pack(padx=20, pady=5,side=TOP, anchor=NW)
        Frame(self.frame_box,width=300,height=2,bg="black").pack(padx=20, side=TOP,anchor=NW)

        # create label and entry widgets for product description
        self.desc_label = Label(self.frame_box, text="Product Description:",fg="black",bg="white",font=("Microsoft YaHei UI light",10,"bold"))
        self.desc_entry = Entry(self.frame_box,width=50,border=0,fg="black",bg="white",font=("Microsoft YaHei UI light",8,))
        self.desc_label.pack(padx=20, pady=5,side=TOP, anchor=NW)
        self.desc_entry.pack(padx=20, pady=5,side=TOP, anchor=NW)
        Frame(self.frame_box,width=300,height=2,bg="black").pack(padx=20, side=TOP,anchor=NW)

        # create label and entry widgets for product price
        self.price_label = Label(self.frame_box, text="Product Price:",fg="black",bg="white",font=("Microsoft YaHei UI light",10,"bold"))
        self.price_entry = Entry(self.frame_box,width=50,border=0,fg="black",bg="white",font=("Microsoft YaHei UI light",8,))
        self.price_label.pack(padx=20, pady=5,side=TOP, anchor=NW)
        self.price_entry.pack(padx=20, pady=5,side=TOP, anchor=NW)
        Frame(self.frame_box,width=300,height=2,bg="black").pack(padx=20, side=TOP,anchor=NW)

        # create label and entry widgets for product quantity
        self.quantity_label = Label(self.frame_box, text="Product Quantity:",fg="black",bg="white",font=("Microsoft YaHei UI light",10,"bold"))
        self.quantity_entry = Entry(self.frame_box,width=50,border=0,fg="black",bg="white",font=("Microsoft YaHei UI light",8,))
        self.quantity_label.pack(padx=20, pady=5,side=TOP, anchor=NW)
        self.quantity_entry.pack(padx=20, pady=5,side=TOP, anchor=NW)
        Frame(self.frame_box,width=300,height=2,bg="black").pack(padx=20, side=TOP,anchor=NW)  

        # create label and entry widgets for alert threshold
        self.threshold_label = Label(self.frame_box, text="Alert Threshold:",fg="black",bg="white",font=("Microsoft YaHei UI light",10,"bold"))
        self.threshold_entry = Entry(self.frame_box,width=50,border=0,fg="black",bg="white",font=("Microsoft YaHei UI light",8,))
        self.threshold_label.pack(padx=20, pady=5,side=TOP, anchor=NW)
        self.threshold_entry.pack(padx=20, pady=5,side=TOP, anchor=NW)
        Frame(self.frame_box,width=300,height=2,bg="black").pack(padx=20, side=TOP,anchor=NW)

        # create label and entry widgets for last entry date
        self.entry_date_label = Label(self.frame_box, text="Last Entry Date:",fg="black",bg="white",font=("Microsoft YaHei UI light",10,"bold"))
        self.entry_date_entry = DateEntry(self.frame_box,width=50,border=0,fg="black",bg="white",font=("Microsoft YaHei UI light",8,))
        self.entry_date_label.pack(padx=20, pady=5,side=TOP, anchor=NW)
        self.entry_date_entry.pack(padx=20, pady=5,side=TOP, anchor=NW)
        Frame(self.frame_box,width=300,height=2,bg="black").pack(padx=20, side=TOP,anchor=NW)

        # create label and entry widgets for last exit date
        self.exit_date_label = Label(self.frame_box, text="Last Exit Date:",fg="black",bg="white",font=("Microsoft YaHei UI light",10,"bold"))
        self.exit_date_entry = DateEntry(self.frame_box,width=50,border=0,fg="black",bg="white",font=("Microsoft YaHei UI light",8,))
        self.exit_date_label.pack(padx=20, pady=5,side=TOP, anchor=NW)
        self.exit_date_entry.pack(padx=20, pady=5,side=TOP, anchor=NW)
        Frame(self.frame_box,width=300,height=2,bg="black").pack(padx=20, side=TOP,anchor=NW)

        # ----------------------Create Buttons----------------------

        # button user
        self.button_add = Button(self.parent, text='Add Product',width=20,pady=7,bg="black",fg="white",border=0,command=self.add_product)
        self.button_add.place(x=40,y=500)

        # button delete
        self.button_delete = Button(self.parent, text='Delete Product',width=20,pady=7,bg="black",fg="white",border=0,command=self.delete_product)
        self.button_delete.place(x=200,y=500)

        # button modify
        self.button_update = Button(self.parent, text='Modify Product',width=20,pady=7,bg="black",fg="white",border=0,command=self.update_product)
        self.button_update.place(x=360,y=500)

        # button user managment   
        self.button_user = Button(self.parent, text='User Managment',width=20,pady=7,bg="black",fg="white",border=0,command=self.user_managment)
        self.button_user.place(x=520,y=500)

        # button user managment   
        self.button_save = Button(self.parent, text='Save',width=15,pady=7,bg="black",fg="white",border=0,command=self.save)
        self.button_save.place(x=680,y=500)

        
        # Insert all data
        self.insert()

        self.parent.mainloop()

#----------Functions----------
    def refresh(self):
        self.tree.delete(*self.tree.get_children())
        self.insert()

    # Insert product function
    def insert(self):
        self.db.connect()
        products = Product(db=self.db)
        resultat = products.display()

        for row in resultat:
            print("list of products is ",row)

            # format the date object in the desired format
            date_entry = datetime.strptime(str(row[7]), '%Y-%m-%d').date()
            date_exit = datetime.strptime(str(row[8]), '%Y-%m-%d').date()
            date_entry_tk = date_entry.strftime('%d/%m/%Y')
            date_exit_tk = date_exit.strftime('%d/%m/%Y')
            self.tree.insert("","end",values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],date_entry_tk,date_exit_tk))
            print(date_exit,date_entry)

        
    # Empty function 
    def emptyEntry(self):
        self.name_entry.delete(0, END)
        self.desc_entry.delete(0, END)
        self.price_entry.delete(0,END)
        self.quantity_entry.delete(0, END)
        self.threshold_entry.delete(0,END)
        self.entry_date_entry.delete(0, END)
        self.exit_date_entry.delete(0, END)

    def user_managment(self):
        Ui_User(self.id)

    # Add product function
    def add_product(self):
        name = self.name_entry.get()
        desc = self.desc_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        threshold =self.threshold_entry.get()
        last_date_entry = self.entry_date_entry.get()
        last_date_exit = self.exit_date_entry.get()
        date_entry = datetime.strptime(last_date_entry, '%m/%d/%Y').date()
        date_exit = datetime.strptime(last_date_exit, '%m/%d/%Y').date()

        if name == "" or desc == "" or price == "" or quantity =="" or threshold =="" or last_date_entry =="" or last_date_exit == "":
            messagebox.showwarning(title=("Empty"),message="Entry is empty")
        else:
            produit = Product(db=self.db)
            produit.add(self.id,name,desc,float(price),int(quantity),int(threshold),date_entry,date_exit)
            self.emptyEntry()
            self.refresh()

    # Delete product function
    def delete_product(self):
        selected_item = self.tree.selection()[0]
        item_id = self.tree.item(selected_item)['values'][0]
        query = "SELECT id_user FROM product WHERE id_product = %s "
        values = (item_id,)
        self.db.execute_query(query,values)
        rstl = self.db.fetch_all()
        user_product = rstl[0][0]
        if user_product == self.id:
            print(user_product)
            products = Product(db=self.db)
            prd = products.delete(id_product=item_id)
            if prd == True:
                self.tree.delete(selected_item)
        else : 
            messagebox.showerror(title="Permission",message="you not have the permission")
        
    
    def update_product(self):
        selected = self.tree.focus()
    # Grab record values
        values = self.tree.item(selected, 'values')

        if values[1] != self.username:
            messagebox.showerror(title="username permission",message="you are not the user of the product")
        else:
            self.emptyEntry()
            self.id_product = values[0]
            self.name_entry.insert(0,values[2])
            self.desc_entry.insert(0,values[3])
            self.price_entry.insert(0,float(values[4]))
            self.quantity_entry.insert(0,int(values[5]))
            self.threshold_entry.insert(0,int(values[6]))
            self.entry_date_entry.insert(0,values[7])
            self.exit_date_entry.insert(0,values[8])
            return self.id_product
    
    def save(self):
        self.id_product
        name = self.name_entry.get()
        desc = self.desc_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        threshold =self.threshold_entry.get()
        last_date_entry = self.entry_date_entry.get()
        last_date_exit = self.exit_date_entry.get()


        if name == "" or desc == "" or price == "" or quantity =="" or threshold =="" or last_date_entry == "" or last_date_exit =="":
            messagebox.showwarning(title=("Empty"),message="Entry is empty")
        else:
            produit = Product(db=self.db)
            date_entry = datetime.strptime(last_date_entry, '%d/%m/%Y').date()
            date_exit = datetime.strptime(last_date_exit, '%d/%m/%Y').date()
            produit.update(self.id_product,name,desc,float(price),int(quantity),int(threshold),date_entry,date_exit)
            self.emptyEntry()
            self.refresh()

            

       
