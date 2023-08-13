from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import random


def main():
    root=Tk()
    app=Details(root)
    
        
class Details:
    def __init__(self,root):
        self.root=root
        self.root.title("AI Project")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="IN AND OUT MOTION DETECTION",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)
    #======================================ALL VARIABLES====================================================
        

        self.search_by=StringVar()
        self.search_txt=StringVar()
                                                                      
    #======================================DETAILS FRAME====================================================


        Details_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Details_Frame.place(x=125,y=100,width=1030,height=530)

        lbl_search=Label(Details_Frame,text="Search By",bg="crimson",fg="white",font=("times new roman",10,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Details_Frame,textvariable=self.search_by,font=("times new roman",10,"bold"),state='readonly')
        combo_search['values']=("aadhar_no","name","contact","religion","qualification","maritual","occupation","gender","Mother_Tongue","area_pincode")
        combo_search.grid(row=0,column=1,pady=10,padx=20)

        txt_search=Entry(Details_Frame,textvariable=self.search_txt,width=25,font=("times new roman",10,"bold"),bd=4,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Details_Frame,text="Search",width=10,command=self.search_data).grid(row=0,column=3,padx=8,pady=10)
        showallbtn=Button(Details_Frame,text="Show All",width=10,command=self.fetch_data).grid(row=0,column=4,padx=8,pady=10)

    #=====================================TABLE FRAME=========================================================

        Table_Frame=Frame(Details_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=1000,height=440)

        lbl_search=Label(Details_Frame,text="Search By",bg="crimson",fg="white",font=("times new roman",10,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Details_Frame,textvariable=self.search_by,font=("times new roman",10,"bold"),state='readonly')
        combo_search['values']=("in_out","time","date")
        combo_search.grid(row=0,column=1,pady=10,padx=20)

        txt_search=Entry(Details_Frame,textvariable=self.search_txt,width=25,font=("times new roman",10,"bold"),bd=4,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Details_Frame,text="Search",width=10,command=self.search_data).grid(row=0,column=3,padx=8,pady=10)
        showallbtn=Button(Details_Frame,text="Show All",width=10,command=self.fetch_data).grid(row=0,column=4,padx=8,pady=10)

    #=====================================TABLE FRAME=========================================================

        Table_Frame=Frame(Details_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=1000,height=440)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.data_table=ttk.Treeview(Table_Frame,columns=("in/out","time","date"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.data_table.xview)
        scroll_y.config(command=self.data_table.yview)
        self.data_table.heading("in/out",text="In/Out")
        self.data_table.heading("time",text="Time")
        self.data_table.heading("date",text="Date")
        
        
        self.data_table['show']='headings'
        self.data_table.column("in/out",width=150)
        self.data_table.column("time",width=150)
        self.data_table.column("date",width=150)
        
        
        self.data_table.pack(fill=BOTH,expand=1)
        self.data_table.bind("<ButtonRelease-1>")
        self.fetch_data()
        self.data_table.pack()

    def add_comunity(self):
            self.fetch_data()
            
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',database='ai_project',user='root',password='')
        cur=conn.cursor()
        cur.execute("select * from data")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.data_table.delete(*self.data_table.get_children())
            for row in rows:
                self.data_table.insert("",END,values=row)
                conn.commit()
            conn.close()

        
    

    

    def search_data(self):
        conn=mysql.connector.connect(host='localhost',database='ai_project',user='root',password='')
        cur=conn.cursor()
        cur.execute("select * from data where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")      
        rows=cur.fetchall()
        if len(rows)!=0:
            self.data_table.delete(*self.data_table.get_children())
            for row in rows:
                self.data_table.insert("",END,values=row)
                conn.commit()
            conn.close()



if __name__ =='__main__':
    main()



