import tkinter as tk
import pywhatkit as kit
def sending():
    global num
    global text
    global hour
    global minu
    num=x.get()
    text=y.get()
    hour=h.get()
    minu=m.get()
    root.destroy()
    kit.sendwhatmsg(num,text,hour,minu)
root=tk.Tk()
root.geometry('400x200')
root.title("Whatsapp Automation")
root.configure(bg='black')
x=tk.StringVar()
y=tk.StringVar()
h=tk.IntVar()
m=tk.IntVar()
label1=tk.Label(root,text="Enter your Number:").grid(row=0,column=0)
label2=tk.Label(root,text="Enter your Text:").grid(row=1,column=0)
label3=tk.Label(root,text="Enter time in hour:").grid(row=2,column=0)
label4=tk.Label(root,text="Enter time in minutes:").grid(row=3,column=0)
entry1=tk.Entry(root,textvariable=x).grid(row=0,column=1)
entry2=tk.Entry(root,textvariable=y).grid(row=1,column=1)
entry3=tk.Entry(root,textvariable=h).grid(row=2,column=1)
entry4=tk.Entry(root,textvariable=m).grid(row=3,column=1)
bt=tk.Button(root,text="send",command=sending).grid(row=4,column=1,ipadx=10,ipady=10)
root.mainloop()



