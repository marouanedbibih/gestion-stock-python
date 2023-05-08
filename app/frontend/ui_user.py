from backend.connexion import Connexion
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from backend.user import User

class Ui_User():
    def __init__(self,id):
        # Variables

        self.user = Tk()
        self.id = id
        self.db = Connexion()


        # Declare Window
        self.user.title("User Managment")
        self.user.geometry("580x550+100+20")
        self.user.config(bg="#fff")
        self.user.resizable(False,False)

        self.label = Label(self.user, text='User Management System', font=('Arial', 16),bg="white")
        self.label.pack(side='top', padx=10, pady=10)

        self.frame = Frame(self.user,width=500,height=200,bg='red')
        self.frame.pack()

        # Create Treeview
        self.tree = ttk.Treeview(self.frame, height=10,columns=('id','username'))

        self.tree.column("#0",width=0,minwidth=0)
        self.tree.column("id",anchor=CENTER,width=100)
        self.tree.column("username",anchor=W,width=150)


        self.tree.heading("#0",text="#")
        self.tree.heading("id",text="ID")
        self.tree.heading("username",text="Username")


        self.tree.pack(side='left',fill='both', expand=True,anchor=W)

        self.username_label = Label(self.user,text="Username : ",fg="black",bg="white",font=("Microsoft YaHei UI light",13,"bold",))
        self.username_label.pack(padx=20, side=TOP,anchor=NW)
        
        # username input
        self.username_input = Entry(self.user,width=50,border=3,fg="black",bg="white",font=("Microsoft YaHei UI light",13,))
        self.username_input.pack(padx=20,pady=0)

        # username label
        self.password_label = Label(self.user,text="Password : ",fg="black",bg="white",font=("Microsoft YaHei UI light",13,"bold",))
        self.password_label.pack(padx=20, side=TOP,anchor=NW)
        
        # password input
        self.password_input = Entry(self.user,width=50,border=3,fg="black",bg="white",font=("Microsoft YaHei UI light",13,),show="*")
        self.password_input.pack(padx=20,pady=0)

        self.confirme_label = Label(self.user,text="Confirme : ",fg="black",bg="white",font=("Microsoft YaHei UI light",13,"bold",))
        self.confirme_label.pack(padx=20, side=TOP,anchor=NW)

        self.confirme_input = Entry(self.user,width=50,border=3,fg="black",bg="white",font=("Microsoft YaHei UI light",13,),show="*")
        self.confirme_input.pack(padx=20,pady=0)


        self.button_add_user = Button(self.user, text='Add User',width=12,pady=7,bg="black",fg="white",border=0,command=self.add)
        self.button_add_user.place(x=40,y=500)

        # button delete
        self.button_delete_user = Button(self.user, text='Delete User',width=12,pady=7,bg="black",fg="white",border=0,command=self.delete)
        self.button_delete_user.place(x=140,y=500)

        # button modify
        self.button_update_user = Button(self.user, text='Update User',width=12,pady=7,bg="black",fg="white",border=0,command=self.update)
        self.button_update_user.place(x=240,y=500)

        # button user managment   
        self.button_save = Button(self.user, text='Save',width=15,pady=7,bg="black",fg="white",border=0,command=self.save)
        self.button_save.place(x=340,y=500)
        
        self.insert()
        self.user.mainloop()

    def emptyBox(self):
        self.username_input.delete(0, END)
        self.password_input.delete(0, END)
        self.confirme_input.delete(0, END)

    def refresh(self):
        self.tree.delete(*self.tree.get_children())
        self.insert()
        
    def insert(self):
        self.db.connect()
        user = User(db=self.db)
        resultat = user.display_user()
        for row in resultat:
            print("list of products is ",row)
            self.tree.insert("","end",values=row)

    def add(self):
        # get username and password value
        username = self.username_input.get()
        password = self.password_input.get()
        confirme = self.confirme_input.get()

        user = User(db=self.db)

        # check username & password empty
        if username == "" or password == "" or confirme == "":
            # display usrname & password empty error
            messagebox.showwarning(title='Empty', message='Entre username and password')
        # check Password
        elif  len(password) < 8 :
            messagebox.showwarning(title='Lenght error', message='Password most to be more 8 charactere')
        elif password != confirme :
            messagebox.showwarning(title='password error', message='Enter same password')
        else:
            resultat = user.checkUsername(username)

            if resultat:
                messagebox.showwarning(title='username error', message='Username exist')
                return
            # Insert User and passsword in DataBase
            user.addUser(username,password)
            self.refresh()
            self.emptyBox()

            messagebox.showinfo(title="success",message="insertion valider")
            
    def delete(self):
        selected_item = self.tree.selection()[0]
        item_id = self.tree.item(selected_item)['values'][0]

        if item_id == self.id:
            messagebox.showerror(title="User",message="You can delet your self")
        #elif self.id !=1 or self.id != 2:
        #    messagebox.showerror(title="Admin",message="you most be super admin for delete user")
        else:
            user = User(db=self.db)
            user.deleteUser(item_id)
            self.refresh()

    def update(self):
    # Clear entry boxes
        self.emptyBox()
    # Grab record number                    
        selected = self.tree.focus()
    # Grab record values
        values = self.tree.item(selected, 'values')
    # output to entry boxes
        self.username_input.insert(0, values[1])

    def save(self):

        username =self.username_input.get()
        password =self.password_input.get()
        confirme = self.confirme_input.get()

        selected = self.tree.focus()
        # Grab record values
        values = self.tree.item(selected, 'values')
        id = int(values[0])
   

        if password != confirme:
            messagebox.showwarning(title='Update',message="Entre same password")
        elif password == "" or confirme == "" or username == "":
            messagebox.showwarning(title='Update',message="entry is empty")
        else:
            user = User(db=self.db)
            user.updateUser(username,password,id)
            self.refresh()
            self.emptyBox()
            messagebox.showinfo(title="success",message="Username update")
            


        



            

