from tkinter import*
root=Tk()
root.title("calculator")

#LABELS
num_1=Label(root,text='enter number 1:',font='arial 16')
num_1.grid(row=0,column=0)
num_2=Label(root,text='enter number 2:',font='arial 16')
num_2.grid(row=1,column=0)

res_label=Label(root,text="result:",font='arial 14')
res_label.grid(row=3,column=0)

#ENTRY
num1=Entry(root,width=20)
num1.grid(row=0,column=1)

num2=Entry(root,width=20)
num2.grid(row=1,column=1)

res_entry=Entry(root,width=20)
res_entry.grid(row=3,column=1)

#functions

def add_butt():
    first=int(num1.get())
    second=int(num2.get())
    result=first+second
    res_entry.delete(0,END)
    res_entry.insert(0,result)

def sub_butt():
    first=int(num1.get())
    second=int(num2.get())
    result=first-second
    res_entry.delete(0,END)
    res_entry.insert(0,result)

def multi_butt():
    first=int(num1.get())
    second=int(num2.get())
    result=first*second
    res_entry.delete(0,END)
    res_entry.insert(0,result)

def div_butt():
    first=int(num1.get())
    second=int(num2.get())
    result=first/second
    res_entry.delete(0,END)
    res_entry.insert(0,result)


#buttons
add_butt=Button(root,text='ADD', command=add_butt)
add_butt.grid(row=2,column=0,padx=10,pady=10,columnspan=1)

sub_butt=Button(root,text='SUB',command=sub_butt)
sub_butt.grid(row=2,column=1,padx=10,pady=10,columnspan=1)

multi_butt=Button(root,text='MULTI', command=multi_butt)
multi_butt.grid(row=2,column=2,padx=10,pady=10,columnspan=1)

div_butt=Button(root,text='DIV',command=div_butt)
div_butt.grid(row=2,column=3,padx=10,pady=10,columnspan=1)

root.mainloop()

## in command you cannot  add a function or pass a function with parameter  directly, it will throw a error
## you have use lambda function