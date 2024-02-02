import tkinter as tk
from tkinter import Label, Button
import time
localtime=time.asctime(time.localtime(time.time()))






class Apple:
    def __init__(self,top):
        self.top=top
        top.title("Restaurant Management")
        top.geometry("1028x500")
        top.configure(background="#091833")




        font10 ="{Courier New} 10 normal"
        font11="{U.S. 101} 30 bold"
        font12="Al-Aramco 11 bold"
        font13="{Courier New} 10 bold"
        font14="{Segoe UI} 15 bold"
        font15="Arail 13 bold"
        font16="{Segoe UI} 13 bold"


        self.Lablel1=tk.Label(master=top, text="Restaurant Management System",background="#091833",font=font14,foreground="#f2a343")
        self.Lablel1.place(relx=0.268,rely=0.02, height=51,width=507)


        localtime1=Label(master=top, text=localtime,background="#091833",font=font16,fg="steel blue")
        localtime1.place(relx=0.420,rely=0.12)


        self.Lablel12=tk.Label(master=top, text="Order Number :",background="#091833",font=font12,foreground="#bac8bd")
        self.Lablel12.place(relx=0.054,rely=0.25)
        self.Lablel12=tk.Label(master=top, text="Fried Patato :",background="#091833",font=font12,foreground="#bac8bd")
        self.Lablel12.place(relx=0.069,rely=0.32)
        self.Lablel12=tk.Label(master=top, text="Chk Burger :",background="#091833",font=font12,foreground="#bac8bd")
        self.Lablel12.place(relx=0.073,rely=0.4)
        self.Lablel12=tk.Label(master=top, text="Big King :",background="#091833",font=font12,foreground="#bac8bd")
        self.Lablel12.place(relx=0.093,rely=0.48)
        self.Lablel12=tk.Label(master=top, text="Chk Royal :",background="#091833",font=font12,foreground="#bac8bd")
        self.Lablel12.place(relx=0.083,rely=0.56)
        self.Lablel12=tk.Label(master=top, text="Veg Saled :",background="#091833",font=font12,foreground="#bac8bd")
        self.Lablel12.place(relx=0.080,rely=0.64)
        self.Lablel12=tk.Label(master=top, text="Drinksr :",background="#091833",font=font12,foreground="#bac8bd")
        self.Lablel12.place(relx=0.098,rely=0.71)




        self.entry1=tk.Entry(master=top,background="#d9d9d9",selectbackground="#f2a343",foreground="#c60000",font=font13)
        self.entry1.place(relx=0.18,rely=0.26)
        self.entry1=tk.Entry(master=top,background="#d9d9d9",selectbackground="#f2a343",foreground="#c60000",font=font13)
        self.entry1.place(relx=0.18,rely=0.33)
        self.entry1=tk.Entry(master=top,background="#d9d9d9",selectbackground="#f2a343",foreground="#c60000",font=font13)
        self.entry1.place(relx=0.18,rely=0.40)
        self.entry1=tk.Entry(master=top,background="#d9d9d9",selectbackground="#f2a343",foreground="#c60000",font=font13)
        self.entry1.place(relx=0.18,rely=0.48)
        self.entry1=tk.Entry(master=top,background="#d9d9d9",selectbackground="#f2a343",foreground="#c60000",font=font13)
        self.entry1.place(relx=0.18,rely=0.56)
        self.entry1=tk.Entry(master=top,background="#d9d9d9",selectbackground="#f2a343",foreground="#c60000",font=font13)
        self.entry1.place(relx=0.18,rely=0.64)
        self.entry1=tk.Entry(master=top,background="#d9d9d9",selectbackground="#f2a343",foreground="#c60000",font=font13)
        self.entry1.place(relx=0.18,rely=0.71)




        self.entry1=tk.Entry(master=top,background="#d9d9d9",selectbackground="#f2a343",foreground="#c60000",font=font13)
        self.entry1.place(relx=0.705,rely=0.24,height=35,relwidth=0.267)

        self.Button1=tk.Button(master=top, text='''7''',font=font14,background='#122c63',foreground='#ffffff',borderwidth='0')
        self.Button1.place(relx=0.705,rely=0.34,height=44,width=67)
        self.Button1=tk.Button(master=top, text='''8''',font=font14,background='#122c63',foreground='#ffffff',borderwidth='0')
        self.Button1.place(relx=0.780,rely=0.34,height=44,width=67)
        self.Button1=tk.Button(master=top, text='''9''',font=font14,background='#122c63',foreground='#ffffff',borderwidth='0')
        self.Button1.place(relx=0.856,rely=0.34,height=44,width=67)
        self.Button1=tk.Button(master=top, text='''/''',font=font14,background='#122c63',foreground='#ffffff',borderwidth='0')
        self.Button1.place(relx=0.930,rely=0.34,height=44,width=37)

        self.Button1=tk.Button(master=top, text='''4''',font=font14,background='#122c63',foreground='#ffffff',borderwidth='0')
        self.Button1.place(relx=0.705,rely=0.44,height=44,width=67)
        self.Button1=tk.Button(master=top, text='''5''',font=font14,background='#122c63',foreground='#ffffff',borderwidth='0')
        self.Button1.place(relx=0.780,rely=0.44,height=44,width=67)
        self.Button1=tk.Button(master=top, text='''6''',font=font14,background='#122c63',foreground='#ffffff',borderwidth='0')
        self.Button1.place(relx=0.856,rely=0.44,height=44,width=67)
        self.Button1=tk.Button(master=top, text='''X''',font=font14,background='#122c63',foreground='#ffffff',borderwidth='0')
        self.Button1.place(relx=0.930,rely=0.44,height=44,width=37)


        self.Button1=tk.Button(master=top, text='''1''',font=font14,background='#122c63',foreground='#ffffff',borderwidth='0')
        self.Button1.place(relx=0.705,rely=0.54,height=44,width=67)
        self.Button1=tk.Button(master=top, text='''2''',font=font14,background='#122c63',foreground='#ffffff',borderwidth='0')
        self.Button1.place(relx=0.780,rely=0.54,height=44,width=67)
        self.Button1=tk.Button(master=top, text='''3''',font=font14,background='#122c63',foreground='#ffffff',borderwidth='0')
        self.Button1.place(relx=0.856,rely=0.54,height=44,width=67)
        self.Button1=tk.Button(master=top, text='''-''',font=font14,background='#122c63',foreground='#ffffff',borderwidth='0')
        self.Button1.place(relx=0.930,rely=0.54,height=44,width=37)

        self.Button1=tk.Button(master=top, text='''0''',font=font14,background='#122c63',foreground='#ffffff',borderwidth='0')
        self.Button1.place(relx=0.705,rely=0.64,height=35,width=146)
        self.Button1=tk.Button(master=top, text='''.''',font=font14,background='#122c63',foreground='#ffffff',borderwidth='0')
        self.Button1.place(relx=0.856,rely=0.64,height=35,width=67)
        self.Button1=tk.Button(master=top, text='''+''',font=font14,background='#122c63',foreground='#ffffff',borderwidth='0')
        self.Button1.place(relx=0.930,rely=0.64,height=35,width=37)
        self.Button1=tk.Button(master=top, text='''=''',font=font14,background='#f2a343',foreground='#ffffff',borderwidth='0')
        self.Button1.place(relx=0.705,rely=0.72,height=34,width=272)


        self.Lablel12=tk.Label(master=top, text="Cost :",background="#091833",font=font12,foreground="#e16740")
        self.Lablel12.place(relx=0.40,rely=0.32)
        self.Lablel12=tk.Label(master=top, text="Service Charge :",background="#091833",font=font12,foreground="#bac8bd")
        self.Lablel12.place(relx=0.35,rely=0.4)
        self.Lablel12=tk.Label(master=top, text="Tax :",background="#091833",font=font12,foreground="#bac8bd")
        self.Lablel12.place(relx=0.40,rely=0.48)
        self.Lablel12=tk.Label(master=top, text="Subtotal :",background="#091833",font=font12,foreground="#bac8bd")
        self.Lablel12.place(relx=0.38,rely=0.56)
        self.Lablel12=tk.Label(master=top, text="Total :",background="#091833",font=font12,foreground="#bac8bd")
        self.Lablel12.place(relx=0.40,rely=0.64)



        self.entry13=tk.Entry(master=top,background="#d9d9d9",selectbackground="#f2a343",foreground="#c60000",font=font13)
        self.entry13.place(relx=0.454,rely=0.33,relwidth=0.145)
        self.entry13=tk.Entry(master=top,background="#d9d9d9",selectbackground="#f2a343",foreground="#c60000",font=font13)
        self.entry13.place(relx=0.480,rely=0.41,relwidth=0.120)
        self.entry13=tk.Entry(master=top,background="#d9d9d9",selectbackground="#f2a343",foreground="#c60000",font=font13)
        self.entry13.place(relx=0.445,rely=0.49,relwidth=0.155)
        self.entry13=tk.Entry(master=top,background="#d9d9d9",selectbackground="#f2a343",foreground="#c60000",font=font13)
        self.entry13.place(relx=0.460,rely=0.57,relwidth=0.140)
        self.entry13=tk.Entry(master=top,background="#d9d9d9",selectbackground="#f2a343",foreground="#c60000",font=font13)
        self.entry13.place(relx=0.455,rely=0.65,relwidth=0.145)





        self.Button2=tk.Button(master=top,text="PRICE",background="#e16740",font=font16)
        self.Button2.place(relx=0.039,rely=0.86,height=34,width=107)
        self.Button2=tk.Button(master=top,text="TOTAL",background="#e16740",font=font16)
        self.Button2.place(relx=0.156,rely=0.86,height=34,width=107)
        self.Button2=tk.Button(master=top,text="RESET",background="#e16740",font=font16)
        self.Button2.place(relx=0.272,rely=0.86,height=34,width=107)
        self.Button2=tk.Button(master=top,text="EXIT",background="#e16740",font=font16)
        self.Button2.place(relx=0.389,rely=0.86,height=34,width=107)











root=tk.Tk()
my_gui=Apple(root)
root.mainloop()
