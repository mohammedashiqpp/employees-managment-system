import tkinter
import tkinter.messagebox
from PIL import ImageTk, Image
import pymysql

x=pymysql.connect(host='localhost',user='root',password='root123',db='emp')
cur=x.cursor()
# cur.execute("CREATE TABLE employees (employeeid int,name VARCHAR(255),age int,post VARCHAR(255),salary int)")
from tkinter import *


root = Tk()
root.title("employees")
root.geometry("320x240+125+125")
bg= ImageTk.PhotoImage(file='1.jpg')
b=tkinter.Label(root,image=bg)
b.place(x=0,y=0)


def check_employee( employeeid):
    sql = 'select * from employees where employeeid=%s'
    c = x.cursor()
    data = (employeeid,)
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def add():
    sub = Toplevel(root)
    sub.title("Sub Window")
    sub.geometry("320x240+125+125")
    Label(sub,text='Employee id').place(x=10, y=50)
    a1 = Entry(sub,width=25)
    a1.place( x=110, y=50)
    Label(sub, text='Name').place(x=10, y=80)
    a2 = Entry(sub, width=25)
    a2.place(x=110, y=80)
    Label(sub, text='age').place(x=10, y=110)
    a3 = Entry(sub, width=25)
    a3.place( x=110, y=110)
    Label(sub, text='post').place(x=10, y=140)
    a4 = Entry(sub, width=25)
    a4.place( x=110, y=140)
    Label(sub, text='salary').place(x=10, y=170)
    a5 = Entry(sub, width=25)
    a5.place( x=110, y=170)

    def adds():
        Id=a1.get()
        if (check_employee(Id) == True):
            tkinter.messagebox.showinfo("", "Employee Already taken")


        else:

            ab=a1.get()
            ab1 = a2.get()
            ab2 = a3.get()
            ab3 = a4.get()
            ab4 = a5.get()
            cur.execute('insert into employees values(%s,%s,%s,%s,%s)', (ab,ab1,ab2,ab3,ab4))
            x.commit()
            tkinter.messagebox.showinfo("", "add employee")
            x.close()


    Button(sub, text='ok', fg='red', width=5,command=adds).place(x=250, y=200)



Label(text='Add employee').place(x=10,y=30)
a1=btn = Button(root,
             text="Add",fg='green',width=20,
             command=add)
a1.place(x=110,y=30)

Label(text='Enter employee id').place(x=10,y=60)
a2=Entry(width=15)
a2.place(x=110,y=60)


def remove():
    Id=a2.get()

    if (check_employee(Id) == False):
        tkinter.messagebox.showinfo("","Employee does not  exists Try Again")


    else:
        sql = 'delete from employees where employeeid=%s'
        data = (Id)
        c = x.cursor()
        c.execute(sql, data)
        x.commit()
        tkinter.messagebox.showinfo("","Employee Removed")
b=btn = Button(root,
             text="Delete",bg='red',width=5,
             command=remove)
b.place(x=215,y=60)

Label(text='Enter employee id').place(x=10,y=90)
a6=Entry(width=15)
a6.place(x=110,y=90)
def update():
    Id = a6.get()

    if (check_employee(Id) == False):
        tkinter.messagebox.showinfo("", "Employee does not  exists Try Again")


    else:
        sub = Toplevel(root)
        sub.title("Sub Window")
        sub.geometry("320x240+125+125")
        Label(sub, text='Name').place(x=10, y=80)
        a2 = Entry(sub, width=25)
        a2.place(x=110, y=80)
        Label(sub, text='age').place(x=10, y=110)
        a3 = Entry(sub, width=25)
        a3.place(x=110, y=110)
        Label(sub, text='post').place(x=10, y=140)
        a4 = Entry(sub, width=25)
        a4.place(x=110, y=140)
        Label(sub, text='salary').place(x=10, y=170)
        a5 = Entry(sub, width=25)
        a5.place(x=110, y=170)

        def up():
            ab1 = a2.get()
            ab2 = a3.get()
            ab3 = a4.get()
            ab4 = a5.get()

            data = (ab1,ab2,ab3,ab4,Id)
            c = x.cursor()

            sql = 'update employees set name=%s,age=%s,post=%s,salary=%s where employeeid=%s'

            # Executing the SQL Query
            c.execute(sql, data)

            x.commit()
            tkinter.messagebox.showinfo("", "Employe updated")
            x.close()


        Button(sub, text='ok', fg='red', width=5, command=up).place(x=250, y=200)
b=btn = Button(root,
             text="update",bg='blue',width=5,
             command=update)
b.place(x=215,y=90)
Label(text='Enter employee id').place(x=10,y=120)
a4=Entry(width=15)
a4.place(x=110,y=120)




def out():
    Id = a4.get()
    if (check_employee(Id) == False):
        tkinter.messagebox.showinfo("", "Employee does not  exists Try Again")


    else:
        data=(Id,)
        sql = 'select * from employees where employeeid=%s'
        c = x.cursor()
        c.execute(sql,Id)
        r = c.fetchall()
        e = Label(root, width=10, text='id', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.place(x=10, y=160)
        e = Label(root, width=10, text='Name', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.place(x=50, y=160)
        e = Label(root, width=10, text='age', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.place(x=110, y=160)
        e = Label(root, width=10, text='post', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.place(x=180, y=160)
        e = Label(root, width=9, text='salary', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.place(x=250, y=160)

        for i in r:
                e = Label(root, width=10, text=i[0],
                          borderwidth=2, relief='ridge', anchor="w")
                e.place(x=10, y=180)
                e = Label(root, width=10, text=i[1],
                          borderwidth=2, relief='ridge', anchor="w")
                e.place(x=50, y=180)
                e = Label(root, width=10, text=i[2],
                          borderwidth=2, relief='ridge', anchor="w")
                e.place(x=110, y=180)
                e = Label(root, width=10, text=i[3],
                          borderwidth=2, relief='ridge', anchor="w")
                e.place(x=180, y=180)
                e = Label(root, width=9, text=i[4],
                          borderwidth=2, relief='ridge', anchor="w")
                e.place(x=250, y=180)






b=btn = Button(root,
             text="Result",bg='cyan',width=5,
             command=out)
b.place(x=215,y=120)

mainloop()