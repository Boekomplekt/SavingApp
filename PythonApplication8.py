from gc import disable
import customtkinter as CTk
import tkinter
from tkinter import *
from tkinter import Canvas
from PIL import ImageTk, Image
import linecache


class ToplevelWindowInput(CTk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("AppLiser")
        self.resizable(False,False)
        self.input_window = CTk.CTkImage(dark_image= Image.open("input.png"),size=(400,300))
        self.input_image = CTk.CTkLabel(master=self,text = "",image=self.input_window)
        self.input_image.grid(row=0,column=0)
        
       

        self.grid_rowconfigure(0, weight=1)  
        self.grid_columnconfigure(0, weight=1)

        self.text_login = tkinter.StringVar(value="Login")

        self.label_login = CTk.CTkButton(master=self,
                               textvariable=self.text_login,
                               width=120,
                               height=25,
                               fg_color=("#2E69CA"),
                               text_color = ("black"),
                               font=('Helvetica', 18, 'bold'),
                               corner_radius=5,
                               command=self.login_input)
        self.label_login.place(relx=0.3, rely=0.75, anchor=tkinter.CENTER)

        self.text_app_inp = ""
        self.text_login_inp = ""
        self.text_pass_inp = ""
        

        self.text_pass = tkinter.StringVar(value="Password")

        self.label_pass = CTk.CTkButton(master=self,
                               textvariable=self.text_pass,
                               width=120,
                               height=25,
                               fg_color=("#C7298B"),
                               text_color = ("black"),
                               font=('Helvetica', 18, 'bold'),
                               corner_radius=5,
                               command=self.password_input)
        self.label_pass.place(relx=0.7, rely=0.25, anchor=tkinter.CENTER)
        
        self.text_exit = tkinter.StringVar(value="Exit")
        
        self.label_exit = CTk.CTkButton(master=self,
                               textvariable=self.text_exit,
                               width=85,
                               height=25,
                               fg_color=("lightblue"),
                               text_color = ("black"),
                               font=('Helvetica', 17, 'bold'),
                               corner_radius=5,
                               command=self.exit)
        self.label_exit.place(relx=0.70, rely=0.80, anchor=tkinter.CENTER)

        self.text_save = tkinter.StringVar(value="Save&Exit")
        
        self.label_save = CTk.CTkButton(master=self,
                               textvariable=self.text_save,
                               width=85,
                               height=25,
                               fg_color=("lightblue"),
                               text_color = ("black"),
                               font=('Helvetica', 17, 'bold'),
                               corner_radius=5,
                               command=self.save_exit)
        self.label_save.place(relx=0.70, rely=0.90, anchor=tkinter.CENTER)

        self.text_app = tkinter.StringVar(value="App")
        
        self.label_app = CTk.CTkButton(master=self,
                               textvariable=self.text_app,
                               width=85,
                               height=25,
                               fg_color=("#7B68EE"),
                               text_color = ("black"),
                               font=('Helvetica', 17, 'bold'),
                               corner_radius=5,
                               command=self.app)
        self.label_app.place(relx=0.3, rely=0.25, anchor=tkinter.CENTER)

        
    def login_input(self):
        self.dialog_login = CTk.CTkInputDialog(text="Type in a login:", title="Login")
        self.text_login_inp = tkinter.StringVar(value = self.dialog_login.get_input() )
        self.label_login_inp = CTk.CTkLabel(master=self,
                               textvariable=self.text_login_inp,
                               width=120,
                               height=25,
                               fg_color=("#2E69CA"),
                               text_color = ("black"),
                               font=('Helvetica', 18, 'bold'),
                               corner_radius=5)
        self.label_login_inp.place(relx=0.3, rely=0.65, anchor=tkinter.CENTER)     


    def password_input(self):
       self.dialog_pass = CTk.CTkInputDialog(text="Type in a password:", title="Password")
       self.text_pass_inp = tkinter.StringVar(value = self.dialog_pass.get_input() )

       self.label_pass_inp = CTk.CTkLabel(master=self,
                               textvariable=self.text_pass_inp,
                               width=120,
                               height=25,
                               fg_color=("#C7298B"),
                               text_color = ("black"),
                               font=('Helvetica', 18, 'bold'),
                               corner_radius=5)
       self.label_pass_inp.place(relx=0.7, rely=0.35, anchor=tkinter.CENTER)

    def app(self):
       self.dialog_app = CTk.CTkInputDialog(text="Type name of app:", title="App")
       self.text_app_inp = tkinter.StringVar(value = self.dialog_app.get_input() )

       self.label_app_inp = CTk.CTkLabel(master=self,
                               textvariable=self.text_app_inp,
                               width=120,
                               height=25,
                               fg_color=("#7B68EE"),
                               text_color = ("black"),
                               font=('Helvetica', 18, 'bold'),
                               corner_radius=5)
       self.label_app_inp.place(relx=0.3, rely=0.35, anchor=tkinter.CENTER)
       

    def save_exit(self):
        if isinstance(self.text_app_inp, str):
            str_app = self.text_app_inp
        else:
            str_app = self.text_app_inp.get()
        if isinstance(self.text_pass_inp, str):
            str_pass = self.text_pass_inp
        else:
            str_pass = self.text_pass_inp.get()
        if isinstance(self.text_login_inp, str):
            str_log = self.text_login_inp
        else:
            str_log = self.text_login_inp.get()
        bool_app=str_app.isascii()
        bool_log=str_log.isascii()
        bool_pass=str_pass.isascii()
        if bool_app and bool_log and bool_pass == True:
          if len(str_app) and len(str_log) and len(str_pass) != 0:
              with open('file.txt', 'a') as f:
               f.write(self.text_app_inp.get()+ '\n')
               f.write(self.text_login_inp.get()+ '\n')
               f.write(self.text_pass_inp.get() + '\n')
              f.close()
              self.destroy()
          else:
              self.text_empty = tkinter.StringVar(value="Epmty space")

              self.label_empty = CTk.CTkLabel(master=self,
                                    textvariable=self.text_empty,
                                    width=180,
                                    height=50,
                                    fg_color=("#2E69CA"),
                                    text_color = ("black"),
                                    font=('Helvetica', 18, 'bold'),
                                    corner_radius=5)
              self.label_empty.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER) 
         
        else: 

          self.text_notascii = tkinter.StringVar(value="Incorect input")

          self.label_notascii = CTk.CTkLabel(master=self,
                                textvariable=self.text_notascii,
                                width=180,
                                height=50,
                                fg_color=("#2E69CA"),
                                text_color = ("black"),
                                font=('Helvetica', 18, 'bold'),
                                corner_radius=5)
          self.label_notascii.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER) 
        

        
        

    def exit(self):
        self.destroy()
       

class ToplevelWindowTable(CTk.CTkToplevel):
  
     
  def __init__(self, *args, **kwargs,):
        super().__init__(*args, **kwargs)
        self.geometry("700x600")
        self.title("AppLiser")
        self.resizable(False,False)
        w = self.winfo_width()
        h = self.winfo_height()
        self.table_window = CTk.CTkImage(dark_image= Image.open("table.png"),size=(w,h))
        self.window_image = CTk.CTkLabel(master=self,text = "",image=self.table_window)
        self.window_image.grid(row=0,column=0)
        self.grid_rowconfigure(0, weight=1)  
        self.grid_columnconfigure(0, weight=1)
        self.text_buttons = tkinter.StringVar(value="")




        self.g = 1
        
       
        self.right_image = CTk.CTkImage(dark_image= Image.open("right.png"),
                                     size = ( 50,40))
        self.right = CTk.CTkButton(master=self,
                               image=self.right_image,
                               textvariable=self.text_buttons,
                               width=60,
                               height=40,
                               fg_color=("#151e2f"),
                               text_color = ("black"),
                               font=('Helvetica', 18, 'bold'),
                               command=self.next)
        self.right.place(relx=0.93, rely=0.8, anchor=tkinter.CENTER)
        
        self.left_image = CTk.CTkImage(dark_image= Image.open("left.png"),
                                     size = ( 50,40))
                                  

        self.left = CTk.CTkButton(master=self,
                               image=self.left_image,
                               textvariable=self.text_buttons,
                               width=60,
                               height=40,
                               fg_color=("#151e2f"),
                               text_color = ("black"),
                               font=('Helvetica', 18, 'bold'),
                               command=self.previous)
        self.left.place(relx=0.06, rely=0.2, anchor=tkinter.CENTER)

        self.text_exit = tkinter.StringVar(value="Exit")
        
        self.label_exit = CTk.CTkButton(master=self,
                               textvariable=self.text_exit,
                               width=90,
                               height=30,
                               fg_color=("#1B1D39"),
                               text_color = ("white"),
                               font=('Helvetica', 17, 'bold'),
                               corner_radius=5,
                               command=self.exit)
        self.label_exit.place(relx=0.07, rely=0.82, anchor=tkinter.CENTER)


        app_line = linecache.getline('file.txt',self.g)

        self.text_app_tab = tkinter.StringVar(value="App: " + app_line)

        self.label_app_tab = CTk.CTkLabel(master=self,
                               textvariable=self.text_app_tab,
                               width=120,
                               height=50,
                               fg_color=("#2F336C"),
                               text_color = ("black"),
                               font=('Helvetica', 18, 'bold'),
                               corner_radius=5)
        self.label_app_tab.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)  
        

        login_line = linecache.getline('file.txt',self.g+1)

        self.text_log_tab = tkinter.StringVar(value="Login: " + login_line)

        self.label_log_tab = CTk.CTkLabel(master=self,
                               textvariable=self.text_log_tab,
                               width=120,
                               height=50,
                               fg_color=("#2F336C"),
                               text_color = ("black"),
                               font=('Helvetica', 18, 'bold'),
                               corner_radius=5)
        self.label_log_tab.place(relx=0.5, rely=0.50, anchor=tkinter.CENTER)   

        pass_line = linecache.getline('file.txt',self.g+2)

        self.text_pass_tab = tkinter.StringVar(value="Password: " + pass_line)

        self.label_pass_tab = CTk.CTkLabel(master=self,
                               textvariable=self.text_pass_tab,
                               width=120,
                               height=50,
                               fg_color=("#2F336C"),
                               text_color = ("black"),
                               font=('Helvetica', 18, 'bold'),
                               corner_radius=5)
        self.label_pass_tab.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)   
        
  def next(self):
      global g
      count = len(open("file.txt").readlines(  ))
      
      if self.g > count-3:
          
          self.right.configure(state = "disabled")
      else:
        self.left.configure(state = "normal")
        self.g+=3
        linecache.checkcache('file.txt')
        app_line = linecache.getline('file.txt', self.g)
        self.text_app_tab = tkinter.StringVar(value="App: " + app_line)
        self.label_app_tab.configure(textvariable= self.text_app_tab)
        log_line = linecache.getline('file.txt', self.g+1)
        self.text_log_tab = tkinter.StringVar(value="Login: " + log_line)
        self.label_log_tab.configure(textvariable= self.text_log_tab)
        pass_line = linecache.getline('file.txt', self.g+2)
        self.text_pass_tab = tkinter.StringVar(value="Password: " + pass_line)
        self.label_pass_tab.configure(textvariable= self.text_pass_tab)

  def previous(self):
      global g
  
      
      if self.g < 3:
          self.left.configure(state = "disabled")
      else:
        self.right.configure(state = "normal")
        self.g-=3
        linecache.checkcache('file.txt')
        app_line = linecache.getline('file.txt', self.g)
        self.text_app_tab = tkinter.StringVar(value="App: " + app_line)
        self.label_app_tab.configure(textvariable= self.text_app_tab)
        log_line = linecache.getline('file.txt', self.g+1)
        self.text_log_tab = tkinter.StringVar(value="Login: " + log_line)
        self.label_log_tab.configure(textvariable= self.text_log_tab)
        pass_line = linecache.getline('file.txt', self.g+2)
        self.text_pass_tab = tkinter.StringVar(value="Password: " + pass_line)
        self.label_pass_tab.configure(textvariable= self.text_pass_tab)
  def exit(self):
        self.destroy()
        


class App(CTk.CTk):
    f = open("file.txt","a")
    f.close()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("460x370")
        self.title("AppLiser")
        self.resizable(False,False)
        self.logo = CTk.CTkImage(dark_image= Image.open("menu.png"),size=(460,300))
        self.logo_label = CTk.CTkLabel(master=self,text = "",image=self.logo)
        self.logo_label.grid(row=0,column=0)


        self.app_frame = CTk.CTkFrame(master=self,fg_color="lightblue")
        self.app_frame.grid(row=1,column=0,pady = (0,0),padx=(0,0),sticky = "nsew")

        self.button_inp = CTk.CTkButton(master=self.app_frame,
                                 width=100,
                                 height=25,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Input",
                                 command=self.open_toplevel_input)
        self.button_inp.place(relx=0.5, rely=0.09, anchor=tkinter.CENTER)

   
       
        self.button_tab = CTk.CTkButton(master=self.app_frame,
                                 width=100,
                                 height=25,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Table",
                                 command=self.open_toplevel_table)
        self.button_tab.place(relx=0.5, rely=0.26, anchor=tkinter.CENTER)
        self.toplevel_window = None

        
        

    def open_toplevel_table(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindowTable(self) 
        else:
            self.toplevel_window.focus()  

    def open_toplevel_input(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindowInput(self) 
        else:
            self.toplevel_window.focus()

    def change_appearance_mode_option_event(self,new_appearance_mode):

        CTk.set_appearance_mode(new_appearance_mode) 


  
        
    

if __name__ == "__main__":
    app = App()
    app.mainloop()   
    
    