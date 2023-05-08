from tkinter import *
from tkinter import messagebox

# Import class connexion database
from backend.connexion import Connexion
# Import class user
from backend.user import User
# Import GUI Menu
from frontend.ui_menu import Ui_Menu 

class Ui_Login():
    def __init__(self,root):

        # Declare Object Database
        self.db = Connexion()
        # Declare root window object
        self.root =root
        self.root.title("Login")
        self.root.geometry("400x350")
        self.root.config(bg="#fff")
        self.root.resizable(False,False)

        # Login label
        self.login_label = Label(self.root,text="Login",fg="Black",bg="white",font=("Microsoft YaHei UI light",23,"bold"))
        self.login_label.pack(pady=30)

        # username label
        self.username_label = Label(self.root,text="Username : ",fg="black",bg="white",font=("Microsoft YaHei UI light",13,"bold",))
        self.username_label.pack(padx=20, side=TOP,anchor=NW)
        
        # username input
        self.username_input = Entry(self.root,width=50,border=0,fg="black",bg="white",font=("Microsoft YaHei UI light",13,))
        self.username_input.pack(padx=20,pady=0)

        # Frme
        self.frame_user= Frame(self.root,width=400,height=2,bg="black")
        self.frame_user.pack(padx=20, side=TOP,anchor=NW)

        # username label
        self.password_label = Label(self.root,text="password : ",fg="black",bg="white",font=("Microsoft YaHei UI light",13,"bold",))
        self.password_label.pack(padx=20, side=TOP,anchor=NW)
        
        # password input
        self.password_input = Entry(self.root,width=50,border=0,fg="black",bg="white",font=("Microsoft YaHei UI light",13,),show="*")
        self.password_input.pack(padx=20,pady=0)

        # Frame
        self.frame_passwd = Frame(self.root,width=400,height=2,bg="black")
        self.frame_passwd.pack(padx=20, side=TOP,anchor=NW)

        # Button login
        self.btn_login = Button(self.root,width=30,pady=7,bg="black",fg="white",text="Login",border=0,command=self.login)
        self.btn_login.pack(padx=20,pady=15,side=TOP)
        
        self.root.mainloop()


    def login(self):
        # get username and password value
        username = self.username_input.get()
        password = self.password_input.get()
        # check username & password empty
        if username == "" or password == "":
            # display usrname & password empty error
            messagebox.showwarning(title='Error', message='Please enter both username and password')
        else:
            user = User(db=self.db)
            result = user.ckeckUserExsist(username=username,password=password)
            # check if result lis null or not
            if not result:
                messagebox.showwarning(title="Invalid",message="Username and password invalid")
            else:
                # Display success message if login successful
                messagebox.showinfo(title="Success",message="Welcome,{} to menu page".format(username))

                # id & name user
                user_id = result[0][0]
                user_name = result[0][1]

                # destroy all widgets
                self.boxDestroy()

                # Show Menu window
                Ui_Menu(parent=self.root,id=user_id,username=user_name)

    def boxDestroy(self):
        # Destroy all widget
        self.login_label.destroy()
        #------------------------------
        self.username_label.destroy()
        self.username_input.destroy()
        self.frame_user.destroy()
        #------------------------------
        self.password_label.destroy()
        self.password_input.destroy()
        self.frame_passwd.destroy()
        #------------------------------
        self.btn_login.destroy()





                
        

    