import customtkinter
import tkinter

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("700x600")
        self.title(" xyz")
        self.switch_var = customtkinter.StringVar(value="off")  #stores if tables are present or no
        self.switch_1 = customtkinter.CTkSwitch(self, text="Dark", command=self.change_appearance_mode_event,variable=self.switch_var, onvalue="on", offvalue="off")
        self.switch_1.place(relx = 0.1, rely=0.8)
        self.hot = tkinter.IntVar()
        self.checkbox_1 = customtkinter.CTkCheckBox(master=self,text= "hot",variable=self.hot)
        self.checkbox_1.place(relx=0.1,rely=0.2)
        self.cold = tkinter.IntVar()
        self.checkbox_2 = customtkinter.CTkCheckBox(master=self,text= "cold",variable=self.cold)
        self.checkbox_2.place(relx=0.4,rely=0.2)
        self.m = tkinter.IntVar()
        self.checkbox_3 = customtkinter.CTkCheckBox(master=self,text= "male",variable=self.m)
        self.checkbox_3.place(relx=0.1,rely=0.3)
        self.f = tkinter.IntVar()
        self.checkbox_4 = customtkinter.CTkCheckBox(master=self,text= "female",variable=self.f)
        self.checkbox_4.place(relx=0.4,rely=0.3)
        self.formal = tkinter.IntVar()
        self.checkbox_5 = customtkinter.CTkCheckBox(master=self,text= "formal",variable=self.formal)
        self.checkbox_5.place(relx=0.1,rely=0.4)
        self.casual = tkinter.IntVar()
        self.checkbox_6 = customtkinter.CTkCheckBox(master=self,text= "casual",variable=self.casual)
        self.checkbox_6.place(relx=0.4,rely=0.4)
        self.ward=customtkinter.CTkButton(self, text = 'Input your wardrobe',command = self.open_f,border_width=0,corner_radius=8)
        self.ward.place(relx=0.1,rely=0.1)
        self.ward1=customtkinter.CTkButton(self, text = 'Choose the apparel',command = self.open_f1,border_width=0,corner_radius=8)
        self.ward1.place(relx=0.6,rely=0.6)
        self.confirm=customtkinter.CTkButton(self, text = 'confirm',command = self.yity,border_width=0,corner_radius=8)
        self.confirm.place(relx=0.1,rely=0.7)

        self.lim=[]
    def yity(self):
        if self.hot.get():
            self.lim.append("hot")
        else:
            self.lim.append("cold")
        if self.m.get():
            self.lim.append("male")
        else:
            self.lim.append("female")
        if self.formal.get():
            self.lim.append("formal")
        else:
            self.lim.append("casual")
        print(self.lim)
        print(self.choice)

    def open_f1(self):
        self.choice=tkinter.filedialog.askopenfilename(initialdir="D://",title="select the wardrobe")
        
    def open_f(self):
        self.wardrobe=tkinter.filedialog.askopenfilenames(initialdir="D://",title="select the wardrobe")
        print(self.wardrobe)
    def change_appearance_mode_event(self):
        if self.switch_var.get()=="on":
            customtkinter.set_appearance_mode("Dark")

        else:
            customtkinter.set_appearance_mode("Light")
            customtkinter.set_default_color_theme("green")
if __name__ == "__main__":
    app = App()
    app.mainloop()