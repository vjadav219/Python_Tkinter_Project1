from tkinter import *
from tkinter import ttk
import mysql.connector
import tkinter.messagebox as tmsg
from tkcalendar import Calendar
from ttkbootstrap.constants import*
import ttkbootstrap as ttk
from datetime import date
import datetime
root = ttk.Window() 
root.geometry("700x500")
root.title("Attandance Project")
root.iconbitmap("images.ico")
root.config(bg="light blue")

global b
Current_Date_Formatted = datetime.datetime.today().strftime ('%d-%m-%Y')
b=str(Current_Date_Formatted)

def date():         
    global b
    de=ttk.DateEntry(dateformat='%d-%m-%Y')
    de.pack()
    def date():
        global b
        l1.configure(text=de.entry.get())
        b=de.entry.get()
    b1=ttk.Button(root,text="show date",command=lambda:date())
    b1.pack(padx=2)
    l1=ttk.Label(root,text=" ")

######Class A attandance Start #############################################################################
def attandance_A():
    import mysql.connector
    import tkinter.messagebox as tmsg
    import ttkbootstrap as ttk
    import tkinter as tk

    root=ttk.Window()
    root.title("Class A Attandance")
    root.iconbitmap("images.ico")
    root.config(bg="light gray")
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH, expand=1)
    my_scrollbar=tk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame)
    number=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65']
    var1=ttk.IntVar(second_frame)
    var2=ttk.IntVar(second_frame)
    var3=ttk.IntVar(second_frame)
    var4=ttk.IntVar(second_frame)
    var5=ttk.IntVar(second_frame)
    var6=ttk.IntVar(second_frame)
    var7=ttk.IntVar(second_frame)
    var8=ttk.IntVar(second_frame)
    var9=ttk.IntVar(second_frame)
    var10=ttk.IntVar(second_frame)
    var11=ttk.IntVar(second_frame)
    var12=ttk.IntVar(second_frame)
    var13=ttk.IntVar(second_frame)
    var14=ttk.IntVar(second_frame)
    var15=ttk.IntVar(second_frame)
    var16=ttk.IntVar(second_frame)
    var17=ttk.IntVar(second_frame)
    var18=ttk.IntVar(second_frame)
    var19=ttk.IntVar(second_frame)
    var20=ttk.IntVar(second_frame)
    var21=ttk.IntVar(second_frame)
    var22=ttk.IntVar(second_frame)
    var23=ttk.IntVar(second_frame)
    var24=ttk.IntVar(second_frame)
    var25=ttk.IntVar(second_frame)
    var26=ttk.IntVar(second_frame)
    var27=ttk.IntVar(second_frame)
    var28=ttk.IntVar(second_frame)
    var29=ttk.IntVar(second_frame)
    var30=ttk.IntVar(second_frame)
    var31=ttk.IntVar(second_frame)
    var32=ttk.IntVar(second_frame)
    var33=ttk.IntVar(second_frame)
    var34=ttk.IntVar(second_frame)
    var35=ttk.IntVar(second_frame)
    var36=ttk.IntVar(second_frame)
    var37=ttk.IntVar(second_frame)
    var38=ttk.IntVar(second_frame)
    var39=ttk.IntVar(second_frame)
    var40=ttk.IntVar(second_frame)
    var41=ttk.IntVar(second_frame)
    var42=ttk.IntVar(second_frame)
    var43=ttk.IntVar(second_frame)
    var44=ttk.IntVar(second_frame)
    var45=ttk.IntVar(second_frame)
    var46=ttk.IntVar(second_frame)
    var47=ttk.IntVar(second_frame)
    var48=ttk.IntVar(second_frame)
    var49=ttk.IntVar(second_frame)
    var50=ttk.IntVar(second_frame)
    var51=ttk.IntVar(second_frame)
    var52=ttk.IntVar(second_frame)
    var53=ttk.IntVar(second_frame)
    var54=ttk.IntVar(second_frame)
    var55=ttk.IntVar(second_frame)
    var56=ttk.IntVar(second_frame)
    var57=ttk.IntVar(second_frame)
    var58=ttk.IntVar(second_frame)
    var59=ttk.IntVar(second_frame)
    var60=ttk.IntVar(second_frame)
    var61=ttk.IntVar(second_frame)
    var62=ttk.IntVar(second_frame)
    var63=ttk.IntVar(second_frame)
    var64=ttk.IntVar(second_frame)
    var65=ttk.IntVar(second_frame)
    new=[var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21,var22,var23,var24,var25,var26,var27,var28,var29,var30,var31,var32,var33,var34,var35,var36,var37,var38,var39,var40,var41,var42,var43,var44,var45,var46,var47,var48,var49,var50,var51,var52,var53,var54,var55,var56,var57,var58,var59,var60,var61,var62,var63,var64,var65]
    for i in new:
        i=i.set(1)
    def check():
        import os
        connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
        mycursor=connection.cursor()
        mycursor = connection.cursor()
        query9= "SELECT DISTINCT date FROM class_a ORDER BY date ASC"
        mycursor.execute(query9)
        row9 = mycursor.fetchall()
        date=[]

        for i in row9:
            v=i[0]
            date.append(v)
        for i in date:
            if(b==i):
                tmsg.showinfo("attandance","attandance has been taken already")
                os._exit(0)
            else:
                print("")
        for i,j,k in zip(new,ab,number):
            if(i.get()==1):
                connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
                mycursor=connection.cursor()
                mycursor.execute("INSERT INTO class_a VALUES (%s, %s,%s,%s)", (k, j,"present",b))
                connection.commit()
            else:
                connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
                mycursor=connection.cursor()  
                mycursor.execute("INSERT INTO class_a VALUES (%s, %s,%s,%s)", (k, j,"absent",b))          
                connection.commit()
        tmsg.showinfo("attandance","Saved Successfully")
    ab1=Label(second_frame,text="Unclick To Absent Student",justify=CENTER,padx=14,font="verdana  15 bold")
    ab1.grid(row=1,column=10,pady=10)
    ab=["BALDHA JEET RANCHHODBHAI","BARACH PAAWAN PIYUSHBHAI","BHATT JANVI SANDIPBHAI","BHENSADADIYA ESHA RAKESHBHAI","BHUT MEET DILIPBHAI","BHUVA JAYRAJ RAJUBHAI","CHAUHAN HARSH RAMESHBHAI","CHAUHAN RIDDHI CHANDULAL","CHAVDA MITESH DINESHBHAI","CHHAYANI VIRAJ BHARATBHAI","CHUDASAMA ABHAY PRAVINBHAI","DABHI HARPALBHAI RANJITBHAI","DADHANIYA MYUSI MANOJBHAI","DALAL KHUSHI YATINKUMAR","DASLANIYA DHRUVIL VIPULBHAI","DAVADA KRISHNA HITESHBHAI","DER SAHILKUMAR JITUBHAI","DHRANGI ASHISHKUMAR SHANKARBHAI","FALDU KESHVI RAJENDRAKUMAR","FATANIYA KEYUR HITESHBHAI","GADHIYA AFSIN NAUSHAD","GOHEL KRISH BHARATBHAI","GOR JEELKUMAR VIRENDRAKUMAR","GOSWAMI VINITPURI RAMESHPURI","GUNDIGARA ADITYA ROHITBHAI","HALAI AKSHAY NANJI","HIRANI SIDDHI NARANBHAI","JADAV KHUSHI NILESHBHAI","JADAV VIPUL BATUKBHAI","JAKASANIYA YASHKUMAR KANTILAL","JASANI BHARGAV JAYSUKHBHAI","JESADIYA DIPKUMAR HASMUKHBHAI","JETHVA JAYKUMAR MAHESHBHAI","JOGI ANKUL ASHOKBHAI","JOSHI DIVYARAJ CHANDRAMANI","KACHCHHI ELESH PARESHBHAI","KACHHADIYA YATRI RAJESHBHAI","KAPURIYA HIMANSHU BHARATBHAI","KARELIYA KISHANBHAI LIMBABHAI","KASUNDRA BANSI NARENDRABHAI","KATHIRIYA YASH NARSHIBHAI","KERALIYA DARSH HITESHBHAI","KHAMBHAYATA PRERNA HARESHBHAI","KHOLIYA HARSH PRADEEPBHAI","KHUNT VARSHIL MAHENDRABHAI","KOLADIYA PUNJAN PRAFULBHAI","KOTHIYA MEET DHANSUKHBHAI","MEHTA VARUN KETANBHAI","MEPANI VRINDABEN VASANTBHAI","MORI KULDIP JAGDISHBHAI","ODEDRA ARJUN MUNJABHAI","PARGADU MANISHA CHAMPASHIBHAI","PARMAR VAIBHAV GOVINDBHAI","PIPARIYA JAY JAYSUKHBHAI","RADADIYA BANSI JIVANBHAI","RAMANI SMITKUMAR JITESHKUMAR","RAMAVAT DIV RAMADEV","SABHADIYA JEET BHUPATBHAI","VAGADIYA MANOJ PUNJABHAI","VAISHNAV NEEVA DENISHKUMAR","VASANI HENIL JAGDISHBHAI","VIRANI JAY PRAVINBHAI","ZALAVADIYA VIVEK DINESHBHAI","ANDANI RAHIL ASHOKBHAI","GOLETAR MALAY SURESHBHAI"]
    k=5
    for i,j in zip(ab,new):
        i=ttk.Checkbutton(second_frame,cursor="plus", text =i, variable=j,onvalue = 1,bootstyle=SUCCESS)
        i.grid(row=k,column=10,sticky=W,pady=2)
        k=k+1
    ttk.Button(root, text ="save",command=check, style='warning.Outline.TButton').pack(padx=0,pady=1)
    ttk.Button(root, text ="close", command =root.destroy,style='warning.Outline.TButton').pack(padx=0,pady=0)
    root.mainloop()
######Class A attandance End################################################################################
######Class B attandance Start ################################################################################
def attandance_B():
    import mysql.connector
    import tkinter.messagebox as tmsg
    import ttkbootstrap as ttk
    root=ttk.Window()
    root.title("Class B Attandance")
    root.iconbitmap("images.ico")
    root.config(bg="light gray")
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH, expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame)
    number=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65']
    var1=ttk.IntVar(second_frame)
    var2=ttk.IntVar(second_frame)
    var3=ttk.IntVar(second_frame)
    var4=ttk.IntVar(second_frame)
    var5=ttk.IntVar(second_frame)
    var6=ttk.IntVar(second_frame)
    var7=ttk.IntVar(second_frame)
    var8=ttk.IntVar(second_frame)
    var9=ttk.IntVar(second_frame)
    var10=ttk.IntVar(second_frame)
    var11=ttk.IntVar(second_frame)
    var12=ttk.IntVar(second_frame)
    var13=ttk.IntVar(second_frame)
    var14=ttk.IntVar(second_frame)
    var15=ttk.IntVar(second_frame)
    var16=ttk.IntVar(second_frame)
    var17=ttk.IntVar(second_frame)
    var18=ttk.IntVar(second_frame)
    var19=ttk.IntVar(second_frame)
    var20=ttk.IntVar(second_frame)
    var21=ttk.IntVar(second_frame)
    var22=ttk.IntVar(second_frame)
    var23=ttk.IntVar(second_frame)
    var24=ttk.IntVar(second_frame)
    var25=ttk.IntVar(second_frame)
    var26=ttk.IntVar(second_frame)
    var27=ttk.IntVar(second_frame)
    var28=ttk.IntVar(second_frame)
    var29=ttk.IntVar(second_frame)
    var30=ttk.IntVar(second_frame)
    var31=ttk.IntVar(second_frame)
    var32=ttk.IntVar(second_frame)
    var33=ttk.IntVar(second_frame)
    var34=ttk.IntVar(second_frame)
    var35=ttk.IntVar(second_frame)
    var36=ttk.IntVar(second_frame)
    var37=ttk.IntVar(second_frame)
    var38=ttk.IntVar(second_frame)
    var39=ttk.IntVar(second_frame)
    var40=ttk.IntVar(second_frame)
    var41=ttk.IntVar(second_frame)
    var42=ttk.IntVar(second_frame)
    var43=ttk.IntVar(second_frame)
    var44=ttk.IntVar(second_frame)
    var45=ttk.IntVar(second_frame)
    var46=ttk.IntVar(second_frame)
    var47=ttk.IntVar(second_frame)
    var48=ttk.IntVar(second_frame)
    var49=ttk.IntVar(second_frame)
    var50=ttk.IntVar(second_frame)
    var51=ttk.IntVar(second_frame)
    var52=ttk.IntVar(second_frame)
    var53=ttk.IntVar(second_frame)
    var54=ttk.IntVar(second_frame)
    var55=ttk.IntVar(second_frame)
    var56=ttk.IntVar(second_frame)
    var57=ttk.IntVar(second_frame)
    var58=ttk.IntVar(second_frame)
    var59=ttk.IntVar(second_frame)
    var60=ttk.IntVar(second_frame)
    var61=ttk.IntVar(second_frame)
    var62=ttk.IntVar(second_frame)
    var63=ttk.IntVar(second_frame)
    var64=ttk.IntVar(second_frame)
    var65=ttk.IntVar(second_frame)
    new=[var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21,var22,var23,var24,var25,var26,var27,var28,var29,var30,var31,var32,var33,var34,var35,var36,var37,var38,var39,var40,var41,var42,var43,var44,var45,var46,var47,var48,var49,var50,var51,var52,var53,var54,var55,var56,var57,var58,var59,var60,var61,var62,var63,var64,var65]
    for i in new:
        i=i.set(1)
    def check():
        import os
        connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
        mycursor=connection.cursor()
        mycursor = connection.cursor()
        query9= "SELECT DISTINCT date FROM class_b ORDER BY date ASC"
        mycursor.execute(query9)
        row9 = mycursor.fetchall()
        date=[]

        for i in row9:
            v=i[0]
            date.append(v)
        for i in date:
            if(b==i):
                tmsg.showinfo("attandance","attandance has been taken already")
                os._exit(0)
            else:
                print("")
        for i,j,k in zip(new,ab,number):
            if(i.get()==1):
                connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
                mycursor=connection.cursor()
                mycursor.execute("INSERT INTO class_b VALUES (%s, %s,%s,%s)", (k, j,"present",b))
                connection.commit()
            else:
                connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
                mycursor=connection.cursor()  
                mycursor.execute("INSERT INTO class_b VALUES (%s, %s,%s,%s)", (k, j,"absent",b))          
                connection.commit()
        tmsg.showinfo("attandance","Saved Successfully")
    ab=Label(second_frame,text="Unclick To Absent Student",justify=CENTER,padx=14,font="verdana  15 bold")
    ab.grid(row=1,column=10,pady=10)
    ab=["BALDHA JEET RANCHHODBHAI","BARACH PAAWAN PIYUSHBHAI","BHATT JANVI SANDIPBHAI","BHENSADADIYA ESHA RAKESHBHAI","BHUT MEET DILIPBHAI","BHUVA JAYRAJ RAJUBHAI","CHAUHAN HARSH RAMESHBHAI","CHAUHAN RIDDHI CHANDULAL","CHAVDA MITESH DINESHBHAI","CHHAYANI VIRAJ BHARATBHAI","CHUDASAMA ABHAY PRAVINBHAI","DABHI HARPALBHAI RANJITBHAI","DADHANIYA MYUSI MANOJBHAI","DALAL KHUSHI YATINKUMAR","DASLANIYA DHRUVIL VIPULBHAI","DAVADA KRISHNA HITESHBHAI","DER SAHILKUMAR JITUBHAI","DHRANGI ASHISHKUMAR SHANKARBHAI","FALDU KESHVI RAJENDRAKUMAR","FATANIYA KEYUR HITESHBHAI","GADHIYA AFSIN NAUSHAD","GOHEL KRISH BHARATBHAI","GOR JEELKUMAR VIRENDRAKUMAR","GOSWAMI VINITPURI RAMESHPURI","GUNDIGARA ADITYA ROHITBHAI","HALAI AKSHAY NANJI","HIRANI SIDDHI NARANBHAI","JADAV KHUSHI NILESHBHAI","JADAV VIPUL BATUKBHAI","JAKASANIYA YASHKUMAR KANTILAL","JASANI BHARGAV JAYSUKHBHAI","JESADIYA DIPKUMAR HASMUKHBHAI","JETHVA JAYKUMAR MAHESHBHAI","JOGI ANKUL ASHOKBHAI","JOSHI DIVYARAJ CHANDRAMANI","KACHCHHI ELESH PARESHBHAI","KACHHADIYA YATRI RAJESHBHAI","KAPURIYA HIMANSHU BHARATBHAI","KARELIYA KISHANBHAI LIMBABHAI","KASUNDRA BANSI NARENDRABHAI","KATHIRIYA YASH NARSHIBHAI","KERALIYA DARSH HITESHBHAI","KHAMBHAYATA PRERNA HARESHBHAI","KHOLIYA HARSH PRADEEPBHAI","KHUNT VARSHIL MAHENDRABHAI","KOLADIYA PUNJAN PRAFULBHAI","KOTHIYA MEET DHANSUKHBHAI","MEHTA VARUN KETANBHAI","MEPANI VRINDABEN VASANTBHAI","MORI KULDIP JAGDISHBHAI","ODEDRA ARJUN MUNJABHAI","PARGADU MANISHA CHAMPASHIBHAI","PARMAR VAIBHAV GOVINDBHAI","PIPARIYA JAY JAYSUKHBHAI","RADADIYA BANSI JIVANBHAI","RAMANI SMITKUMAR JITESHKUMAR","RAMAVAT DIV RAMADEV","SABHADIYA JEET BHUPATBHAI","VAGADIYA MANOJ PUNJABHAI","VAISHNAV NEEVA DENISHKUMAR","VASANI HENIL JAGDISHBHAI","VIRANI JAY PRAVINBHAI","ZALAVADIYA VIVEK DINESHBHAI","ANDANI RAHIL ASHOKBHAI","GOLETAR MALAY SURESHBHAI"]
    k=5
    for i,j in zip(ab,new):
        i=ttk.Checkbutton(second_frame,cursor="plus", text =i, variable=j,onvalue = 1,bootstyle=SUCCESS)
        i.grid(row=k,column=10,sticky=W,pady=2)
        k=k+1
    ttk.Button(root, text ="save",command=check, style='warning.Outline.TButton').pack(padx=0,pady=1)
    ttk.Button(root, text ="close", command =root.destroy,style='warning.Outline.TButton').pack(padx=0,pady=0)
    root.mainloop()
######Class B attandance End#########################################################################
######Class C attandance Start ######################################################################
def attandance_C():
    import mysql.connector
    import tkinter.messagebox as tmsg
    import ttkbootstrap as ttk
    root=ttk.Window()
    root.title("Class C Attandance")
    root.iconbitmap("images.ico")
    root.config(bg="light gray")
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH, expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame)
    number=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65']
    var1=ttk.IntVar(second_frame)
    var2=ttk.IntVar(second_frame)
    var3=ttk.IntVar(second_frame)
    var4=ttk.IntVar(second_frame)
    var5=ttk.IntVar(second_frame)
    var6=ttk.IntVar(second_frame)
    var7=ttk.IntVar(second_frame)
    var8=ttk.IntVar(second_frame)
    var9=ttk.IntVar(second_frame)
    var10=ttk.IntVar(second_frame)
    var11=ttk.IntVar(second_frame)
    var12=ttk.IntVar(second_frame)
    var13=ttk.IntVar(second_frame)
    var14=ttk.IntVar(second_frame)
    var15=ttk.IntVar(second_frame)
    var16=ttk.IntVar(second_frame)
    var17=ttk.IntVar(second_frame)
    var18=ttk.IntVar(second_frame)
    var19=ttk.IntVar(second_frame)
    var20=ttk.IntVar(second_frame)
    var21=ttk.IntVar(second_frame)
    var22=ttk.IntVar(second_frame)
    var23=ttk.IntVar(second_frame)
    var24=ttk.IntVar(second_frame)
    var25=ttk.IntVar(second_frame)
    var26=ttk.IntVar(second_frame)
    var27=ttk.IntVar(second_frame)
    var28=ttk.IntVar(second_frame)
    var29=ttk.IntVar(second_frame)
    var30=ttk.IntVar(second_frame)
    var31=ttk.IntVar(second_frame)
    var32=ttk.IntVar(second_frame)
    var33=ttk.IntVar(second_frame)
    var34=ttk.IntVar(second_frame)
    var35=ttk.IntVar(second_frame)
    var36=ttk.IntVar(second_frame)
    var37=ttk.IntVar(second_frame)
    var38=ttk.IntVar(second_frame)
    var39=ttk.IntVar(second_frame)
    var40=ttk.IntVar(second_frame)
    var41=ttk.IntVar(second_frame)
    var42=ttk.IntVar(second_frame)
    var43=ttk.IntVar(second_frame)
    var44=ttk.IntVar(second_frame)
    var45=ttk.IntVar(second_frame)
    var46=ttk.IntVar(second_frame)
    var47=ttk.IntVar(second_frame)
    var48=ttk.IntVar(second_frame)
    var49=ttk.IntVar(second_frame)
    var50=ttk.IntVar(second_frame)
    var51=ttk.IntVar(second_frame)
    var52=ttk.IntVar(second_frame)
    var53=ttk.IntVar(second_frame)
    var54=ttk.IntVar(second_frame)
    var55=ttk.IntVar(second_frame)
    var56=ttk.IntVar(second_frame)
    var57=ttk.IntVar(second_frame)
    var58=ttk.IntVar(second_frame)
    var59=ttk.IntVar(second_frame)
    var60=ttk.IntVar(second_frame)
    var61=ttk.IntVar(second_frame)
    var62=ttk.IntVar(second_frame)
    var63=ttk.IntVar(second_frame)
    var64=ttk.IntVar(second_frame)
    var65=ttk.IntVar(second_frame)
    new=[var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21,var22,var23,var24,var25,var26,var27,var28,var29,var30,var31,var32,var33,var34,var35,var36,var37,var38,var39,var40,var41,var42,var43,var44,var45,var46,var47,var48,var49,var50,var51,var52,var53,var54,var55,var56,var57,var58,var59,var60,var61,var62,var63,var64,var65]
    for i in new:
        i=i.set(1)
    def check():
        import os
        connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
        mycursor=connection.cursor()
        mycursor = connection.cursor()
        query9= "SELECT DISTINCT date FROM class_c ORDER BY date ASC"
        mycursor.execute(query9)
        row9 = mycursor.fetchall()
        date=[]

        for i in row9:
            v=i[0]
            date.append(v)
        for i in date:
            if(b==i):
                tmsg.showinfo("attandance","attandance has been taken already")
                os._exit(0)
            else:
                print("")
        for i,j,k in zip(new,ab,number):
            if(i.get()==1):
                connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
                mycursor=connection.cursor()
                mycursor.execute("INSERT INTO class_c VALUES (%s, %s,%s,%s)", (k, j,"present",b))
                connection.commit()
            else:
                connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
                mycursor=connection.cursor()  
                mycursor.execute("INSERT INTO class_c VALUES (%s, %s,%s,%s)", (k, j,"absent",b))          
                connection.commit()
        tmsg.showinfo("attandance","Saved Successfully")
    ab=Label(second_frame,text="Unclick To Absent Student",justify=CENTER,padx=14,font="verdana  15 bold")
    ab.grid(row=1,column=10,pady=10)
    ab=["BALDHA JEET RANCHHODBHAI","BARACH PAAWAN PIYUSHBHAI","BHATT JANVI SANDIPBHAI","BHENSADADIYA ESHA RAKESHBHAI","BHUT MEET DILIPBHAI","BHUVA JAYRAJ RAJUBHAI","CHAUHAN HARSH RAMESHBHAI","CHAUHAN RIDDHI CHANDULAL","CHAVDA MITESH DINESHBHAI","CHHAYANI VIRAJ BHARATBHAI","CHUDASAMA ABHAY PRAVINBHAI","DABHI HARPALBHAI RANJITBHAI","DADHANIYA MYUSI MANOJBHAI","DALAL KHUSHI YATINKUMAR","DASLANIYA DHRUVIL VIPULBHAI","DAVADA KRISHNA HITESHBHAI","DER SAHILKUMAR JITUBHAI","DHRANGI ASHISHKUMAR SHANKARBHAI","FALDU KESHVI RAJENDRAKUMAR","FATANIYA KEYUR HITESHBHAI","GADHIYA AFSIN NAUSHAD","GOHEL KRISH BHARATBHAI","GOR JEELKUMAR VIRENDRAKUMAR","GOSWAMI VINITPURI RAMESHPURI","GUNDIGARA ADITYA ROHITBHAI","HALAI AKSHAY NANJI","HIRANI SIDDHI NARANBHAI","JADAV KHUSHI NILESHBHAI","JADAV VIPUL BATUKBHAI","JAKASANIYA YASHKUMAR KANTILAL","JASANI BHARGAV JAYSUKHBHAI","JESADIYA DIPKUMAR HASMUKHBHAI","JETHVA JAYKUMAR MAHESHBHAI","JOGI ANKUL ASHOKBHAI","JOSHI DIVYARAJ CHANDRAMANI","KACHCHHI ELESH PARESHBHAI","KACHHADIYA YATRI RAJESHBHAI","KAPURIYA HIMANSHU BHARATBHAI","KARELIYA KISHANBHAI LIMBABHAI","KASUNDRA BANSI NARENDRABHAI","KATHIRIYA YASH NARSHIBHAI","KERALIYA DARSH HITESHBHAI","KHAMBHAYATA PRERNA HARESHBHAI","KHOLIYA HARSH PRADEEPBHAI","KHUNT VARSHIL MAHENDRABHAI","KOLADIYA PUNJAN PRAFULBHAI","KOTHIYA MEET DHANSUKHBHAI","MEHTA VARUN KETANBHAI","MEPANI VRINDABEN VASANTBHAI","MORI KULDIP JAGDISHBHAI","ODEDRA ARJUN MUNJABHAI","PARGADU MANISHA CHAMPASHIBHAI","PARMAR VAIBHAV GOVINDBHAI","PIPARIYA JAY JAYSUKHBHAI","RADADIYA BANSI JIVANBHAI","RAMANI SMITKUMAR JITESHKUMAR","RAMAVAT DIV RAMADEV","SABHADIYA JEET BHUPATBHAI","VAGADIYA MANOJ PUNJABHAI","VAISHNAV NEEVA DENISHKUMAR","VASANI HENIL JAGDISHBHAI","VIRANI JAY PRAVINBHAI","ZALAVADIYA VIVEK DINESHBHAI","ANDANI RAHIL ASHOKBHAI","GOLETAR MALAY SURESHBHAI"]
    k=5
    for i,j in zip(ab,new):
        i=ttk.Checkbutton(second_frame,cursor="plus", text =i, variable=j,onvalue = 1,bootstyle=SUCCESS)
        i.grid(row=k,column=10,sticky=W,pady=2)
        k=k+1
    ttk.Button(root, text ="save",command=check, style='warning.Outline.TButton').pack(padx=0,pady=1)
    ttk.Button(root, text ="close", command =root.destroy,style='warning.Outline.TButton').pack(padx=0,pady=0)
    root.mainloop()
######Class C attandance End###################################################################################################
######Class D attandance Start ################################################################################################
def attandance_D():
    import mysql.connector
    import tkinter.messagebox as tmsg
    import ttkbootstrap as ttk
    root=ttk.Window()
    root.title("Class D Attandance")
    root.iconbitmap("images.ico")
    root.config(bg="light gray")
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH, expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame)
    number=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65']
    var1=ttk.IntVar(second_frame)
    var2=ttk.IntVar(second_frame)
    var3=ttk.IntVar(second_frame)
    var4=ttk.IntVar(second_frame)
    var5=ttk.IntVar(second_frame)
    var6=ttk.IntVar(second_frame)
    var7=ttk.IntVar(second_frame)
    var8=ttk.IntVar(second_frame)
    var9=ttk.IntVar(second_frame)
    var10=ttk.IntVar(second_frame)
    var11=ttk.IntVar(second_frame)
    var12=ttk.IntVar(second_frame)
    var13=ttk.IntVar(second_frame)
    var14=ttk.IntVar(second_frame)
    var15=ttk.IntVar(second_frame)
    var16=ttk.IntVar(second_frame)
    var17=ttk.IntVar(second_frame)
    var18=ttk.IntVar(second_frame)
    var19=ttk.IntVar(second_frame)
    var20=ttk.IntVar(second_frame)
    var21=ttk.IntVar(second_frame)
    var22=ttk.IntVar(second_frame)
    var23=ttk.IntVar(second_frame)
    var24=ttk.IntVar(second_frame)
    var25=ttk.IntVar(second_frame)
    var26=ttk.IntVar(second_frame)
    var27=ttk.IntVar(second_frame)
    var28=ttk.IntVar(second_frame)
    var29=ttk.IntVar(second_frame)
    var30=ttk.IntVar(second_frame)
    var31=ttk.IntVar(second_frame)
    var32=ttk.IntVar(second_frame)
    var33=ttk.IntVar(second_frame)
    var34=ttk.IntVar(second_frame)
    var35=ttk.IntVar(second_frame)
    var36=ttk.IntVar(second_frame)
    var37=ttk.IntVar(second_frame)
    var38=ttk.IntVar(second_frame)
    var39=ttk.IntVar(second_frame)
    var40=ttk.IntVar(second_frame)
    var41=ttk.IntVar(second_frame)
    var42=ttk.IntVar(second_frame)
    var43=ttk.IntVar(second_frame)
    var44=ttk.IntVar(second_frame)
    var45=ttk.IntVar(second_frame)
    var46=ttk.IntVar(second_frame)
    var47=ttk.IntVar(second_frame)
    var48=ttk.IntVar(second_frame)
    var49=ttk.IntVar(second_frame)
    var50=ttk.IntVar(second_frame)
    var51=ttk.IntVar(second_frame)
    var52=ttk.IntVar(second_frame)
    var53=ttk.IntVar(second_frame)
    var54=ttk.IntVar(second_frame)
    var55=ttk.IntVar(second_frame)
    var56=ttk.IntVar(second_frame)
    var57=ttk.IntVar(second_frame)
    var58=ttk.IntVar(second_frame)
    var59=ttk.IntVar(second_frame)
    var60=ttk.IntVar(second_frame)
    var61=ttk.IntVar(second_frame)
    var62=ttk.IntVar(second_frame)
    var63=ttk.IntVar(second_frame)
    var64=ttk.IntVar(second_frame)
    var65=ttk.IntVar(second_frame)
    new=[var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21,var22,var23,var24,var25,var26,var27,var28,var29,var30,var31,var32,var33,var34,var35,var36,var37,var38,var39,var40,var41,var42,var43,var44,var45,var46,var47,var48,var49,var50,var51,var52,var53,var54,var55,var56,var57,var58,var59,var60,var61,var62,var63,var64,var65]
    for i in new:
        i=i.set(1)
    def check():
        import os
        connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
        mycursor=connection.cursor()
        mycursor = connection.cursor()
        query9= "SELECT DISTINCT date FROM class_d ORDER BY date ASC"
        mycursor.execute(query9)
        row9 = mycursor.fetchall()
        date=[]

        for i in row9:
            v=i[0]
            date.append(v)
        for i in date:
            if(b==i):
                tmsg.showinfo("attandance","attandance has been taken already")
                os._exit(0)
            else:
                print("")
        for i,j,k in zip(new,ab,number):
            if(i.get()==1):
                connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
                mycursor=connection.cursor()
                mycursor.execute("INSERT INTO class_d VALUES (%s, %s,%s,%s)", (k, j,"present",b))
                connection.commit()
            else:
                connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
                mycursor=connection.cursor()  
                mycursor.execute("INSERT INTO class_d VALUES (%s, %s,%s,%s)", (k, j,"absent",b))          
                connection.commit()
        tmsg.showinfo("attandance","Saved Successfully")
    ab=Label(second_frame,text="Unclick To Absent Student",justify=CENTER,padx=14,font="verdana  15 bold")
    ab.grid(row=1,column=10,pady=10)
    ab=["BALDHA JEET RANCHHODBHAI","BARACH PAAWAN PIYUSHBHAI","BHATT JANVI SANDIPBHAI","BHENSADADIYA ESHA RAKESHBHAI","BHUT MEET DILIPBHAI","BHUVA JAYRAJ RAJUBHAI","CHAUHAN HARSH RAMESHBHAI","CHAUHAN RIDDHI CHANDULAL","CHAVDA MITESH DINESHBHAI","CHHAYANI VIRAJ BHARATBHAI","CHUDASAMA ABHAY PRAVINBHAI","DABHI HARPALBHAI RANJITBHAI","DADHANIYA MYUSI MANOJBHAI","DALAL KHUSHI YATINKUMAR","DASLANIYA DHRUVIL VIPULBHAI","DAVADA KRISHNA HITESHBHAI","DER SAHILKUMAR JITUBHAI","DHRANGI ASHISHKUMAR SHANKARBHAI","FALDU KESHVI RAJENDRAKUMAR","FATANIYA KEYUR HITESHBHAI","GADHIYA AFSIN NAUSHAD","GOHEL KRISH BHARATBHAI","GOR JEELKUMAR VIRENDRAKUMAR","GOSWAMI VINITPURI RAMESHPURI","GUNDIGARA ADITYA ROHITBHAI","HALAI AKSHAY NANJI","HIRANI SIDDHI NARANBHAI","JADAV KHUSHI NILESHBHAI","JADAV VIPUL BATUKBHAI","JAKASANIYA YASHKUMAR KANTILAL","JASANI BHARGAV JAYSUKHBHAI","JESADIYA DIPKUMAR HASMUKHBHAI","JETHVA JAYKUMAR MAHESHBHAI","JOGI ANKUL ASHOKBHAI","JOSHI DIVYARAJ CHANDRAMANI","KACHCHHI ELESH PARESHBHAI","KACHHADIYA YATRI RAJESHBHAI","KAPURIYA HIMANSHU BHARATBHAI","KARELIYA KISHANBHAI LIMBABHAI","KASUNDRA BANSI NARENDRABHAI","KATHIRIYA YASH NARSHIBHAI","KERALIYA DARSH HITESHBHAI","KHAMBHAYATA PRERNA HARESHBHAI","KHOLIYA HARSH PRADEEPBHAI","KHUNT VARSHIL MAHENDRABHAI","KOLADIYA PUNJAN PRAFULBHAI","KOTHIYA MEET DHANSUKHBHAI","MEHTA VARUN KETANBHAI","MEPANI VRINDABEN VASANTBHAI","MORI KULDIP JAGDISHBHAI","ODEDRA ARJUN MUNJABHAI","PARGADU MANISHA CHAMPASHIBHAI","PARMAR VAIBHAV GOVINDBHAI","PIPARIYA JAY JAYSUKHBHAI","RADADIYA BANSI JIVANBHAI","RAMANI SMITKUMAR JITESHKUMAR","RAMAVAT DIV RAMADEV","SABHADIYA JEET BHUPATBHAI","VAGADIYA MANOJ PUNJABHAI","VAISHNAV NEEVA DENISHKUMAR","VASANI HENIL JAGDISHBHAI","VIRANI JAY PRAVINBHAI","ZALAVADIYA VIVEK DINESHBHAI","ANDANI RAHIL ASHOKBHAI","GOLETAR MALAY SURESHBHAI"]
    k=5
    for i,j in zip(ab,new):
        i=ttk.Checkbutton(second_frame,cursor="plus", text =i, variable=j,onvalue = 1,bootstyle=SUCCESS)
        i.grid(row=k,column=10,sticky=W,pady=2)
        k=k+1
    ttk.Button(root, text ="save",command=check, style='warning.Outline.TButton').pack(padx=0,pady=1)
    ttk.Button(root, text ="close", command =root.destroy,style='warning.Outline.TButton').pack(padx=0,pady=0)
    root.mainloop()
######Class D attandance End##########################################################################################
######Class A show attandance Start###################################################################################       
def show_attandance_A():     
    from tkinter import ttk
    import mysql.connector
    import tkinter.messagebox as tmsg
    root = Tk() 
    root.geometry("500x300")
    root.title("Attandance Sheet Of Class A")
    root.iconbitmap("images.ico")
    root.config(bg="light gray")
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH, expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame)
    connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
    mycursor=connection.cursor()
      # mycursor.execute('insert into vipul values("j ","k"); ')
    mycursor.execute(f"select * from class_a where date='{b}' ")
    r=mycursor.fetchall()
    num=3
    ab1=ttk.Label(second_frame,text="Roll Number",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab1.grid(row=1,column=0,padx=0,pady=0)
    ab2=ttk.Label(second_frame,text="Name",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab2.grid(row=1,column=1,padx=10,pady=10)
    ab3=ttk.Label(second_frame,text="Status",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab3.grid(row=1,column=2,padx=0,pady=0)
    ab4=ttk.Label(second_frame,text="Date",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab4.grid(row=1,column=3,padx=10,pady=0)
    for i in r:
        if(i[2]=="present"):
            Roll_Number=ttk.Label(second_frame,text=i[0],font="time 12 bold",style='warning.Inverse.TLabel',background="")
            Roll_Number.grid(row=num,column=0,padx=0,pady=0)
            Student_Name=ttk.Label(second_frame,text=i[1],font="time 12 bold",style='warning.Inverse.TLabel',background="")
            Student_Name.grid(row=num,column=1,padx=10,pady=10)
            Status=ttk.Label(second_frame,text=i[2],font="time 12 bold",style='warning.Inverse.TLabel',background="")
            Status.grid(row=num,column=2,padx=0,pady=0)
            Status=ttk.Label(second_frame,text=i[3],font="time 12 bold",style='warning.Inverse.TLabel',background="")
            Status.grid(row=num,column=3,padx=10,pady=0)
            num=num+1
        else:
            Roll_Number=ttk.Label(second_frame,text=i[0],font="time 12 bold",style='warning.Inverse.TLabel',background="red")
            Roll_Number.grid(row=num,column=0,padx=0,pady=0)
            Student_Name=ttk.Label(second_frame,text=i[1],font="time 12 bold",style='warning.Inverse.TLabel',background="red")
            Student_Name.grid(row=num,column=1,padx=10,pady=10)
            Status=ttk.Label(second_frame,text=i[2],font="time 12 bold",style='warning.Inverse.TLabel',background="red")
            Status.grid(row=num,column=2,padx=0,pady=0)
            Status=ttk.Label(second_frame,text=i[3],font="time 12 bold",style='warning.Inverse.TLabel',background="red")
            Status.grid(row=num,column=3,padx=10,pady=0)
            num=num+1

    if(num==3):
        tmsg.showinfo("error","Data not found")
    else:
        tmsg.showinfo("attandance",f"total {num-3} student in Class A")
    connection.commit() 
    root.mainloop()
######Class A show attandance End###################################################################################
######Class B show attandance Start#################################################################################
def show_attandance_B():     
    from tkinter import ttk
    import mysql.connector
    import tkinter.messagebox as tmsg
    root = Tk() 
    root.geometry("500x300")
    root.title("Attandance Sheet Of Class B")
    root.iconbitmap("images.ico")
    root.config(bg="light gray")
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH, expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame)
    connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
    mycursor=connection.cursor()
      # mycursor.execute('insert into vipul values("j ","k"); ')
    mycursor.execute(f"select * from class_b where date='{b}' ")
    r=mycursor.fetchall()
    num=3
    ab1=ttk.Label(second_frame,text="Roll Number",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab1.grid(row=1,column=0,padx=0,pady=0)
    ab2=ttk.Label(second_frame,text="Name",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab2.grid(row=1,column=1,padx=10,pady=10)
    ab3=ttk.Label(second_frame,text="Status",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab3.grid(row=1,column=2,padx=0,pady=0)
    ab4=ttk.Label(second_frame,text="Date",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab4.grid(row=1,column=3,padx=10,pady=0)
    for i in r:
        if(i[2]=="present"):
            Roll_Number=ttk.Label(second_frame,text=i[0],font="time 12 bold",style='warning.Inverse.TLabel',background="")
            Roll_Number.grid(row=num,column=0,padx=0,pady=0)
            Student_Name=ttk.Label(second_frame,text=i[1],font="time 12 bold",style='warning.Inverse.TLabel',background="")
            Student_Name.grid(row=num,column=1,padx=10,pady=10)
            Status=ttk.Label(second_frame,text=i[2],font="time 12 bold",style='warning.Inverse.TLabel',background="")
            Status.grid(row=num,column=2,padx=0,pady=0)
            Status=ttk.Label(second_frame,text=i[3],font="time 12 bold",style='warning.Inverse.TLabel',background="")
            Status.grid(row=num,column=3,padx=10,pady=0)
            num=num+1
        else:
            Roll_Number=ttk.Label(second_frame,text=i[0],font="time 12 bold",style='warning.Inverse.TLabel',background="red")
            Roll_Number.grid(row=num,column=0,padx=0,pady=0)
            Student_Name=ttk.Label(second_frame,text=i[1],font="time 12 bold",style='warning.Inverse.TLabel',background="red")
            Student_Name.grid(row=num,column=1,padx=10,pady=10)
            Status=ttk.Label(second_frame,text=i[2],font="time 12 bold",style='warning.Inverse.TLabel',background="red")
            Status.grid(row=num,column=2,padx=0,pady=0)
            Status=ttk.Label(second_frame,text=i[3],font="time 12 bold",style='warning.Inverse.TLabel',background="red")
            Status.grid(row=num,column=3,padx=10,pady=0)
            num=num+1
    if(num==3):
        tmsg.showinfo("error","Data not found")
    else:
        tmsg.showinfo("attandance",f"total {num-3} student in Class B")                
    connection.commit() 
    root.mainloop()
######Class B show attandance End###################################################################################
######Class C show attandance Start#################################################################################
def show_attandance_C():     
    from tkinter import ttk
    import mysql.connector
    import tkinter.messagebox as tmsg
    root = Tk() 
    root.geometry("500x300")
    root.title("Attandance Sheet Of Class C")
    root.iconbitmap("images.ico")
    root.config(bg="light gray")
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH, expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame)
    connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
    mycursor=connection.cursor()
      # mycursor.execute('insert into vipul values("j ","k"); ')
    mycursor.execute(f"select * from class_c where date='{b}' ")
    r=mycursor.fetchall()
    num=3
    ab1=ttk.Label(second_frame,text="Roll Number",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab1.grid(row=1,column=0,padx=0,pady=0)
    ab2=ttk.Label(second_frame,text="Name",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab2.grid(row=1,column=1,padx=10,pady=10)
    ab3=ttk.Label(second_frame,text="Status",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab3.grid(row=1,column=2,padx=0,pady=0)
    ab4=ttk.Label(second_frame,text="Date",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab4.grid(row=1,column=3,padx=10,pady=0)
    for i in r:
        if(i[2]=="present"):
            Roll_Number=ttk.Label(second_frame,text=i[0],font="time 12 bold",style='warning.Inverse.TLabel',background="")
            Roll_Number.grid(row=num,column=0,padx=0,pady=0)
            Student_Name=ttk.Label(second_frame,text=i[1],font="time 12 bold",style='warning.Inverse.TLabel',background="")
            Student_Name.grid(row=num,column=1,padx=10,pady=10)
            Status=ttk.Label(second_frame,text=i[2],font="time 12 bold",style='warning.Inverse.TLabel',background="")
            Status.grid(row=num,column=2,padx=0,pady=0)
            Status=ttk.Label(second_frame,text=i[3],font="time 12 bold",style='warning.Inverse.TLabel',background="")
            Status.grid(row=num,column=3,padx=10,pady=0)
            num=num+1
        else:
            Roll_Number=ttk.Label(second_frame,text=i[0],font="time 12 bold",style='warning.Inverse.TLabel',background="red")
            Roll_Number.grid(row=num,column=0,padx=0,pady=0)
            Student_Name=ttk.Label(second_frame,text=i[1],font="time 12 bold",style='warning.Inverse.TLabel',background="red")
            Student_Name.grid(row=num,column=1,padx=10,pady=10)
            Status=ttk.Label(second_frame,text=i[2],font="time 12 bold",style='warning.Inverse.TLabel',background="red")
            Status.grid(row=num,column=2,padx=0,pady=0)
            Status=ttk.Label(second_frame,text=i[3],font="time 12 bold",style='warning.Inverse.TLabel',background="red")
            Status.grid(row=num,column=3,padx=10,pady=0)
            num=num+1
    if(num==3):
        tmsg.showinfo("error","Data not found")
    else:
        tmsg.showinfo("attandance",f"total {num-3} student in Class C")
    connection.commit() 
    root.mainloop()
######Class C show attandance End#################################################################################
######Class D show attandance Start#################################################################################       
def show_attandance_D():     
    from tkinter import ttk
    import mysql.connector
    import tkinter.messagebox as tmsg
    root = Tk() 
    root.geometry("500x300")
    root.title("Attandance Sheet Of Class D")
    root.iconbitmap("images.ico")
    root.config(bg="light gray")
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH, expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame)
    connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
    mycursor=connection.cursor()
      # mycursor.execute('insert into vipul values("j ","k"); ')
    mycursor.execute(f"select * from class_d where date='{b}' ")
    r=mycursor.fetchall()
    num=3
    ab1=ttk.Label(second_frame,text="Roll Number",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab1.grid(row=1,column=0,padx=0,pady=0)
    ab2=ttk.Label(second_frame,text="Name",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab2.grid(row=1,column=1,padx=10,pady=10)
    ab3=ttk.Label(second_frame,text="Status",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab3.grid(row=1,column=2,padx=0,pady=0)
    ab4=ttk.Label(second_frame,text="Date",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab4.grid(row=1,column=3,padx=10,pady=0)
    for i in r:
        if(i[2]=="present"):
            Roll_Number=ttk.Label(second_frame,text=i[0],font="time 12 bold",style='warning.Inverse.TLabel',background="")
            Roll_Number.grid(row=num,column=0,padx=0,pady=0)
            Student_Name=ttk.Label(second_frame,text=i[1],font="time 12 bold",style='warning.Inverse.TLabel',background="")
            Student_Name.grid(row=num,column=1,padx=10,pady=10)
            Status=ttk.Label(second_frame,text=i[2],font="time 12 bold",style='warning.Inverse.TLabel',background="")
            Status.grid(row=num,column=2,padx=0,pady=0)
            Status=ttk.Label(second_frame,text=i[3],font="time 12 bold",style='warning.Inverse.TLabel',background="")
            Status.grid(row=num,column=3,padx=10,pady=0)
            num=num+1
        else:
            Roll_Number=ttk.Label(second_frame,text=i[0],font="time 12 bold",style='warning.Inverse.TLabel',background="red")
            Roll_Number.grid(row=num,column=0,padx=0,pady=0)
            Student_Name=ttk.Label(second_frame,text=i[1],font="time 12 bold",style='warning.Inverse.TLabel',background="red")
            Student_Name.grid(row=num,column=1,padx=10,pady=10)
            Status=ttk.Label(second_frame,text=i[2],font="time 12 bold",style='warning.Inverse.TLabel',background="red")
            Status.grid(row=num,column=2,padx=0,pady=0)
            Status=ttk.Label(second_frame,text=i[3],font="time 12 bold",style='warning.Inverse.TLabel',background="red")
            Status.grid(row=num,column=3,padx=10,pady=0)
            num=num+1
    if(num==3):
        tmsg.showinfo("error","Data not found")
    else:
        tmsg.showinfo("attandance",f"total {num-3} student in Class D")
    connection.commit() 
    root.mainloop() 
######Class D show attandance End#################################################################################
######For Present Start###########################################################################################        
def show_present_A():
    from tkinter import ttk
    import mysql.connector
    import tkinter.messagebox as tmsg
    root = Tk() 
    root.geometry("500x300")
    root.title("Total Present In Class A")
    root.iconbitmap("images.ico")
    root.config(bg="light gray")
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH, expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame)
    connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
    mycursor=connection.cursor()
    mycursor.execute(f"select * from class_a where Status='present' and date='{b}' ")
    r=mycursor.fetchall()
    num=3
    ab1=ttk.Label(second_frame,text="Roll Number",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab1.grid(row=1,column=0,padx=0,pady=0)
    ab2=ttk.Label(second_frame,text="Name",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab2.grid(row=1,column=1,padx=10,pady=10)
    ab3=ttk.Label(second_frame,text="Status",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab3.grid(row=1,column=2,padx=0,pady=0)
    ab4=ttk.Label(second_frame,text="Date",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab4.grid(row=1,column=3,padx=10,pady=0)
    for i in r:
        Roll_Number=Label(second_frame,text=i[0],font="time 12 bold",fg="blue")
        Roll_Number.grid(row=num,column=0,padx=0,pady=0)
        Student_Name=Label(second_frame,text=i[1],font="time 12 bold",fg="blue")
        Student_Name.grid(row=num,column=1,padx=10,pady=10)
        Status=Label(second_frame,text=i[2],font="time 12 bold",fg="blue")
        Status.grid(row=num,column=2,padx=0,pady=0)
        Status=Label(second_frame,text=i[3],font="time 12 bold",fg="blue")
        Status.grid(row=num,column=3,padx=10,pady=0)
        num=num+1
    if(num==3):
        tmsg.showinfo("error","Data not found")
    else:
        tmsg.showinfo("attandance",f"total {num-3} present in Class A")
    connection.commit() 
    root.mainloop()
def show_present_B():
    from tkinter import ttk
    import mysql.connector
    import tkinter.messagebox as tmsg
    root = Tk() 
    root.geometry("500x300")
    root.title("Total Present In Class B")
    root.iconbitmap("images.ico")
    root.config(bg="light gray")
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH, expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame)
    connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
    mycursor=connection.cursor()
    mycursor.execute(f"select * from class_b where Status='present' and date='{b}' ")
    r=mycursor.fetchall()
    num=3
    ab1=ttk.Label(second_frame,text="Roll Number",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab1.grid(row=1,column=0,padx=0,pady=0)
    ab2=ttk.Label(second_frame,text="Name",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab2.grid(row=1,column=1,padx=10,pady=10)
    ab3=ttk.Label(second_frame,text="Status",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab3.grid(row=1,column=2,padx=0,pady=0)
    ab4=ttk.Label(second_frame,text="Date",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab4.grid(row=1,column=3,padx=10,pady=0)
    for i in r:
        Roll_Number=Label(second_frame,text=i[0],font="time 12 bold",fg="blue")
        Roll_Number.grid(row=num,column=0,padx=0,pady=0)
        Student_Name=Label(second_frame,text=i[1],font="time 12 bold",fg="blue")
        Student_Name.grid(row=num,column=1,padx=10,pady=10)
        Status=Label(second_frame,text=i[2],font="time 12 bold",fg="blue")
        Status.grid(row=num,column=2,padx=0,pady=0)
        Status=Label(second_frame,text=i[3],font="time 12 bold",fg="blue")
        Status.grid(row=num,column=3,padx=10,pady=0)
        num=num+1
    if(num==3):
        tmsg.showinfo("error","Data not found")
    else:
        tmsg.showinfo("attandance",f"total {num-3} present in Class B")                
    connection.commit() 
    root.mainloop()
def show_present_C():
    from tkinter import ttk
    import mysql.connector
    import tkinter.messagebox as tmsg
    root = Tk() 
    root.geometry("500x300")
    root.title("Total Present In Class C")
    root.iconbitmap("images.ico")
    root.config(bg="light gray")
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH, expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame)
    connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
    mycursor=connection.cursor()
    mycursor.execute(f"select * from class_c where Status='present' and date='{b}' ")
    r=mycursor.fetchall()
    num=3
    ab1=ttk.Label(second_frame,text="Roll Number",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab1.grid(row=1,column=0,padx=0,pady=0)
    ab2=ttk.Label(second_frame,text="Name",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab2.grid(row=1,column=1,padx=10,pady=10)
    ab3=ttk.Label(second_frame,text="Status",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab3.grid(row=1,column=2,padx=0,pady=0)
    ab4=ttk.Label(second_frame,text="Date",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab4.grid(row=1,column=3,padx=10,pady=0)
    for i in r:
        Roll_Number=Label(second_frame,text=i[0],font="time 12 bold",fg="blue")
        Roll_Number.grid(row=num,column=0,padx=0,pady=0)
        Student_Name=Label(second_frame,text=i[1],font="time 12 bold",fg="blue")
        Student_Name.grid(row=num,column=1,padx=10,pady=10)
        Status=Label(second_frame,text=i[2],font="time 12 bold",fg="blue")
        Status.grid(row=num,column=2,padx=0,pady=0)
        Status=Label(second_frame,text=i[3],font="time 12 bold",fg="blue")
        Status.grid(row=num,column=3,padx=10,pady=0)
        num=num+1
    if(num==3):
        tmsg.showinfo("error","Data not found")
    else:
        tmsg.showinfo("attandance",f"total {num-3} present in Class C")
    connection.commit() 
    root.mainloop()
def show_present_D():
    from tkinter import ttk
    import mysql.connector
    import tkinter.messagebox as tmsg
    root = Tk() 
    root.geometry("500x300")
    root.title("Total Present In Class D")
    root.iconbitmap("images.ico")
    root.config(bg="light gray")
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH, expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame)
    connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
    mycursor=connection.cursor()
    mycursor.execute(f"select * from class_d where Status='present' and date='{b}' ")
    r=mycursor.fetchall()
    num=3
    ab1=ttk.Label(second_frame,text="Roll Number",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab1.grid(row=1,column=0,padx=0,pady=0)
    ab2=ttk.Label(second_frame,text="Name",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab2.grid(row=1,column=1,padx=10,pady=10)
    ab3=ttk.Label(second_frame,text="Status",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab3.grid(row=1,column=2,padx=0,pady=0)
    ab4=ttk.Label(second_frame,text="Date",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab4.grid(row=1,column=3,padx=10,pady=0)
    for i in r:
        Roll_Number=Label(second_frame,text=i[0],font="time 12 bold",fg="blue")
        Roll_Number.grid(row=num,column=0,padx=0,pady=0)
        Student_Name=Label(second_frame,text=i[1],font="time 12 bold",fg="blue")
        Student_Name.grid(row=num,column=1,padx=10,pady=10)
        Status=Label(second_frame,text=i[2],font="time 12 bold",fg="blue")
        Status.grid(row=num,column=2,padx=0,pady=0)
        Status=Label(second_frame,text=i[3],font="time 12 bold",fg="blue")
        Status.grid(row=num,column=3,padx=10,pady=0)
        num=num+1
    if(num==3):
        tmsg.showinfo("error","Data not found")
    else:
        tmsg.showinfo("attandance",f"total {num-3} present in Class D")
    connection.commit() 
    root.mainloop()
######For Present End###########################################################################################
######For absent Start########################################################################################## 
def show_absent_A():
    from tkinter import ttk
    import mysql.connector
    import tkinter.messagebox as tmsg
    root = Tk() 
    root.geometry("500x300")
    root.title("Total Absent In Class A")
    root.iconbitmap("images.ico")
    root.config(bg="light gray")
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH, expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame)
    connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
    mycursor=connection.cursor()
    mycursor.execute(f"select * from class_a where Status='absent' and date='{b}' ")
    r=mycursor.fetchall()
    num=3
    ab1=ttk.Label(second_frame,text="Roll Number",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab1.grid(row=1,column=0,padx=0,pady=0)
    ab2=ttk.Label(second_frame,text="Name",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab2.grid(row=1,column=1,padx=10,pady=10)
    ab3=ttk.Label(second_frame,text="Status",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab3.grid(row=1,column=2,padx=0,pady=0)
    ab4=ttk.Label(second_frame,text="Date",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab4.grid(row=1,column=3,padx=10,pady=0)
    for i in r:
        Roll_Number=Label(second_frame,text=i[0],font="time 12 bold",fg="blue")
        Roll_Number.grid(row=num,column=0,padx=0,pady=0)
        Student_Name=Label(second_frame,text=i[1],font="time 12 bold",fg="blue")
        Student_Name.grid(row=num,column=1,padx=10,pady=10)
        Status=Label(second_frame,text=i[2],font="time 12 bold",fg="blue")
        Status.grid(row=num,column=2,padx=0,pady=0)
        Status=Label(second_frame,text=i[3],font="time 12 bold",fg="blue")
        Status.grid(row=num,column=3,padx=10,pady=0)
        num=num+1
    if(num==3):
        tmsg.showinfo("error","Data not found")
    else:
        tmsg.showinfo("attandance",f"total {num-3} absent in Class A")
    connection.commit() 
    root.mainloop()
def show_absent_B():
    from tkinter import ttk
    import mysql.connector
    import tkinter.messagebox as tmsg
    root = Tk() 
    root.geometry("500x300")
    root.title("Total Absent In Class B")
    root.iconbitmap("images.ico")
    root.config(bg="light gray")
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH, expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame)
    connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
    mycursor=connection.cursor()
    mycursor.execute(f"select * from class_b where Status='absent' and date='{b}' ")
    r=mycursor.fetchall()
    num=3
    ab1=ttk.Label(second_frame,text="Roll Number",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab1.grid(row=1,column=0,padx=0,pady=0)
    ab2=ttk.Label(second_frame,text="Name",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab2.grid(row=1,column=1,padx=10,pady=10)
    ab3=ttk.Label(second_frame,text="Status",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab3.grid(row=1,column=2,padx=0,pady=0)
    ab4=ttk.Label(second_frame,text="Date",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab4.grid(row=1,column=3,padx=10,pady=0)
    for i in r:
        print(i[0]=="")
            # tmsg.showinfo("Error","data not found")
        Roll_Number=Label(second_frame,text=i[0],font="time 12 bold",fg="blue")
        Roll_Number.grid(row=num,column=0,padx=0,pady=0)
        Student_Name=Label(second_frame,text=i[1],font="time 12 bold",fg="blue")
        Student_Name.grid(row=num,column=1,padx=10,pady=10)
        Status=Label(second_frame,text=i[2],font="time 12 bold",fg="blue")
        Status.grid(row=num,column=2,padx=0,pady=0)
        Status=Label(second_frame,text=i[3],font="time 12 bold",fg="blue")
        Status.grid(row=num,column=3,padx=10,pady=0)
        num=num+1
    if(num==3):
        tmsg.showinfo("error","Data not found")
    else:
        tmsg.showinfo("attandance",f"total {num-3} absent in Class B")
    connection.commit() 
    root.mainloop()
def show_absent_C():
    from tkinter import ttk
    import mysql.connector
    import tkinter.messagebox as tmsg
    root = Tk() 
    root.geometry("500x300")
    root.title("Total Absent In Class C")
    root.iconbitmap("images.ico")
    root.config(bg="light gray")
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH, expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame)
    connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
    mycursor=connection.cursor()
    mycursor.execute(f"select * from class_c where Status='absent' and date='{b}' ")
    r=mycursor.fetchall()
    num=3
    ab1=ttk.Label(second_frame,text="Roll Number",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab1.grid(row=1,column=0,padx=0,pady=0)
    ab2=ttk.Label(second_frame,text="Name",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab2.grid(row=1,column=1,padx=10,pady=10)
    ab3=ttk.Label(second_frame,text="Status",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab3.grid(row=1,column=2,padx=0,pady=0)
    ab4=ttk.Label(second_frame,text="Date",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab4.grid(row=1,column=3,padx=10,pady=0)
    for i in r:
        Roll_Number=Label(second_frame,text=i[0],font="time 12 bold",fg="blue")
        Roll_Number.grid(row=num,column=0,padx=0,pady=0)
        Student_Name=Label(second_frame,text=i[1],font="time 12 bold",fg="blue")
        Student_Name.grid(row=num,column=1,padx=10,pady=10)
        Status=Label(second_frame,text=i[2],font="time 12 bold",fg="blue")
        Status.grid(row=num,column=2,padx=0,pady=0)
        Status=Label(second_frame,text=i[3],font="time 12 bold",fg="blue")
        Status.grid(row=num,column=3,padx=10,pady=0)
        num=num+1
    if(num==3):
        tmsg.showinfo("error","Data not found")
    else:
        tmsg.showinfo("attandance",f"total {num-3} absent in Class C")
    connection.commit() 
    root.mainloop()
def show_absent_D():
    from tkinter import ttk
    import mysql.connector
    import tkinter.messagebox as tmsg
    root = Tk() 
    root.geometry("500x300")
    root.title("Total Absent In Class D")
    root.iconbitmap("images.ico")
    root.config(bg="light gray")
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH, expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame)
    connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
    mycursor=connection.cursor()
    mycursor.execute(f"select * from class_d where Status='absent' and date='{b}' ")
    r=mycursor.fetchall()
    num=3
    ab1=ttk.Label(second_frame,text="Roll Number",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab1.grid(row=1,column=0,padx=0,pady=0)
    ab2=ttk.Label(second_frame,text="Name",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab2.grid(row=1,column=1,padx=10,pady=10)
    ab3=ttk.Label(second_frame,text="Status",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab3.grid(row=1,column=2,padx=0,pady=0)
    ab4=ttk.Label(second_frame,text="Date",font="time 15 bold",style='warning.Inverse.TLabel',background="yellow")
    ab4.grid(row=1,column=3,padx=10,pady=0)
    for i in r:
        Roll_Number=Label(second_frame,text=i[0],font="time 12 bold",fg="blue")
        Roll_Number.grid(row=num,column=0,padx=0,pady=0)
        Student_Name=Label(second_frame,text=i[1],font="time 12 bold",fg="blue")
        Student_Name.grid(row=num,column=1,padx=10,pady=10)
        Status=Label(second_frame,text=i[2],font="time 12 bold",fg="blue")
        Status.grid(row=num,column=2,padx=0,pady=0)
        Status=Label(second_frame,text=i[3],font="time 12 bold",fg="blue")
        Status.grid(row=num,column=3,padx=10,pady=0)
        num=num+1
    if(num==3):
        tmsg.showinfo("error","Data not found")
    else:
        tmsg.showinfo("attandance",f"total {num-3} absent in Class D")
    connection.commit() 
    root.mainloop()
######For absent End#############################################################################################    
######For matplotlib bar Start###################################################################################
def analysis_A():
    import tkinter as tk
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
    import mysql.connector
    
    connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
    mycursor=connection.cursor()
    mycursor = connection.cursor()
    query = "SELECT DISTINCT date FROM class_a ORDER BY date ASC"
    mycursor.execute(query)
    row = mycursor.fetchall()
    x=[]
    for i in row:
        b=i[0]
        x.append(b)
    y1=[]
    for i in x:
        query1 = f"SELECT count(Status)  FROM class_a where date='{i}' and Status='present' "
        mycursor.execute(query1)
        row1= [item[0] for item in mycursor.fetchall()]
        y1.append(row1)
    y=[]
    for i in y1:
        c=i[0]
        y.append(c) 
    root=tk.Tk()
    # root.geometry("600x600")
    root.title("Class A Bargraph")
    root.iconbitmap("images.ico")
    root.config(bg="light gray")
    fig,ax=plt.subplots()
    frame=tk.Frame(root)
    # lable=tk.Label(text="Class A")
    # lable.config(font=("Courier",32))
    # lable.pack()
    
    plt.ylabel("Date",fontsize=20)
    plt.xlabel("Present Rate",fontsize=20)
        
    canvas =FigureCanvasTkAgg(fig,master=root)
    canvas.get_tk_widget().pack()
    toolbar=NavigationToolbar2Tk(canvas,frame,pack_toolbar=False)
    toolbar.pack()
    ax.barh(x,y)
    for i in ax.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5,str(round((i.get_width()), 2)),fontsize = 10, fontweight ='bold',color ='grey')
                
    # plt.show()
    frame.pack()
    root.mainloop()
def analysis_B():
    import tkinter as tk
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
    import mysql.connector
    
    connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
    mycursor=connection.cursor()
    mycursor = connection.cursor()
    query = "SELECT DISTINCT date FROM class_b ORDER BY date ASC"
    mycursor.execute(query)
    row = mycursor.fetchall()
    x=[]
    for i in row:
        b=i[0]
        x.append(b)
    y1=[]
    for i in x:
        query1 = f"SELECT count(Status)  FROM class_b where date='{i}' and Status='present' "
        mycursor.execute(query1)
        row1= [item[0] for item in mycursor.fetchall()]
        y1.append(row1)
    y=[]
    for i in y1:
        c=i[0]
        y.append(c) 
    root=tk.Tk()
    # root.geometry("600x600")
    root.title("Class B Bargraph")
    root.iconbitmap("images.ico")
    root.config(bg="light gray")
    fig,ax=plt.subplots()
    frame=tk.Frame(root)
    # lable=tk.Label(text="Class A")
    # lable.config(font=("Courier",32))
    # lable.pack()
    
    plt.ylabel("Date",fontsize=20)
    plt.xlabel("Present Rate",fontsize=20)
        
    canvas =FigureCanvasTkAgg(fig,master=root)
    canvas.get_tk_widget().pack()
    toolbar=NavigationToolbar2Tk(canvas,frame,pack_toolbar=False)
    toolbar.pack()
    ax.barh(x,y)
    for i in ax.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5,str(round((i.get_width()), 2)),fontsize = 10, fontweight ='bold',color ='grey')
                
    # plt.show()
    frame.pack()
    root.mainloop()
def analysis_C():
    import tkinter as tk
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
    import mysql.connector
    
    connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
    mycursor=connection.cursor()
    mycursor = connection.cursor()
    query = "SELECT DISTINCT date FROM class_c ORDER BY date ASC"
    mycursor.execute(query)
    row = mycursor.fetchall()
    x=[]
    for i in row:
        b=i[0]
        x.append(b)
    y1=[]
    for i in x:
        query1 = f"SELECT count(Status)  FROM class_c where date='{i}' and Status='present' "
        mycursor.execute(query1)
        row1= [item[0] for item in mycursor.fetchall()]
        y1.append(row1)
    y=[]
    for i in y1:
        c=i[0]
        y.append(c) 
    root=tk.Tk()
    # root.geometry("600x600")
    root.title("Class C Bargraph")
    root.iconbitmap("images.ico")
    root.config(bg="light gray")
    fig,ax=plt.subplots()
    frame=tk.Frame(root)
    # lable=tk.Label(text="Class A")
    # lable.config(font=("Courier",32))
    # lable.pack()
    
    plt.ylabel("Date",fontsize=20)
    plt.xlabel("Present Rate",fontsize=20)
        
    canvas =FigureCanvasTkAgg(fig,master=root)
    canvas.get_tk_widget().pack()
    toolbar=NavigationToolbar2Tk(canvas,frame,pack_toolbar=False)
    toolbar.pack()
    ax.barh(x,y)
    for i in ax.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5,str(round((i.get_width()), 2)),fontsize = 10, fontweight ='bold',color ='grey')
                
    # plt.show()
    frame.pack()
    root.mainloop()
def analysis_D():
    import tkinter as tk
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
    import mysql.connector
    
    connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
    mycursor=connection.cursor()
    mycursor = connection.cursor()
    query = "SELECT DISTINCT date FROM class_d ORDER BY date ASC"
    mycursor.execute(query)
    row = mycursor.fetchall()
    x=[]
    for i in row:
        b=i[0]
        x.append(b)
    y1=[]
    for i in x:
        query1 = f"SELECT count(Status)  FROM class_d where date='{i}' and Status='present' "
        mycursor.execute(query1)
        row1= [item[0] for item in mycursor.fetchall()]
        y1.append(row1)
    y=[]
    for i in y1:
        c=i[0]
        y.append(c) 
    root=tk.Tk()
    # root.geometry("600x600")
    root.title("Class D Bargraph")
    root.iconbitmap("images.ico")
    root.config(bg="light gray")
    fig,ax=plt.subplots()
    frame=tk.Frame(root)
    # lable=tk.Label(text="Class A")
    # lable.config(font=("Courier",32))
    # lable.pack()
    
    plt.ylabel("Date",fontsize=20)
    plt.xlabel("Present Rate",fontsize=20)
        
    canvas =FigureCanvasTkAgg(fig,master=root)
    canvas.get_tk_widget().pack()
    toolbar=NavigationToolbar2Tk(canvas,frame,pack_toolbar=False)
    toolbar.pack()
    ax.barh(x,y)
    for i in ax.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5,str(round((i.get_width()), 2)),fontsize = 10, fontweight ='bold',color ='grey')
                
    # plt.show()
    frame.pack()
    root.mainloop()
######For matplotlib bar End###################################################################################
######For download CSV Start###################################################################################

# def csv_A():    
#     global b
#     import pandas as pd
#     import mysql.connector
#     import tkinter.messagebox as tmsg
#     db=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
#     cursor=db.cursor()
#     cursor = db.cursor()
#     query = f"SELECT Roll_Number,Student_Name,Status,date from class_a where date='{b}' "
#     cursor.execute(query)
#     row = cursor.fetchall()
#     w=[]
#     x=[]
#     y=[]
#     z=[]
#     for i in row:
#         a=i[0]
#         w.append(a)
#         b=i[1]
#         x.append(b)
#         c=i[2]
#         y.append(c)
#         d=i[3]
#         z.append(d)
#     dictionary={'Roll_Number':w, 'Student_Name':x, 'Status':y, 'date': z}
#     df=pd.DataFrame(dictionary)
#     df_csv=df.to_csv(f"attendance_of_class_A_{b}.csv")
#     tmsg.showinfo("Download","Download Successfully")
# def csv_B():    
#     global b
#     print(b)
#     import pandas as pd
#     import mysql.connector
#     import tkinter.messagebox as tmsg
#     db=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
#     cursor=db.cursor()
#     cursor = db.cursor()
#     query = f"SELECT Roll_Number,Student_Name,Status,date from class_b where date='{b}' "
#     cursor.execute(query)
#     row = cursor.fetchall()
#     w=[]
#     x=[]
#     y=[]
#     z=[]
#     for i in row:
#         a=i[0]
#         w.append(a)
#         b=i[1]
#         x.append(b)
#         c=i[2]
#         y.append(c)
#         d=i[3]
#         z.append(d)
#     dictionary={'Roll_Number':w, 'Student_Name':x, 'Status':y, 'date': z}
#     df=pd.DataFrame(dictionary)
#     df_csv=df.to_csv(f"attendance_of_class_B_{b}.csv")
#     tmsg.showinfo("Download","Download Successfully")
# def csv_C():    
#     global b
#     import pandas as pd
#     import mysql.connector
#     import tkinter.messagebox as tmsg
#     db=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
#     cursor=db.cursor()
#     cursor = db.cursor()
#     query = f"SELECT Roll_Number,Student_Name,Status,date from class_c where date='{b}' "
#     cursor.execute(query)
#     row = cursor.fetchall()
#     w=[]
#     x=[]
#     y=[]
#     z=[]
#     for i in row:
#         a=i[0]
#         w.append(a)
#         b=i[1]
#         x.append(b)
#         c=i[2]
#         y.append(c)
#         d=i[3]
#         z.append(d)
#     dictionary={'Roll_Number':w, 'Student_Name':x, 'Status':y, 'date': z}
#     df=pd.DataFrame(dictionary)
#     df_csv=df.to_csv(f"attendance_of_class_C_{b}.csv")
#     tmsg.showinfo("Download","Download Successfully")
# def csv_D():    
#     global b
#     import pandas as pd
#     import mysql.connector
#     import tkinter.messagebox as tmsg
#     db=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
#     cursor=db.cursor()
#     cursor = db.cursor()
#     query = f"SELECT Roll_Number,Student_Name,Status,date from class_d where date='{b}' "
#     cursor.execute(query)
#     row = cursor.fetchall()
#     w=[]
#     x=[]
#     y=[]
#     z=[]
#     for i in row:
#         a=i[0]
#         w.append(a)
#         b=i[1]
#         x.append(b)
#         c=i[2]
#         y.append(c)
#         d=i[3]
#         z.append(d)
#     dictionary={'Roll_Number':w, 'Student_Name':x, 'Status':y, 'date': z}
#     df=pd.DataFrame(dictionary)
#     df_csv=df.to_csv(f"attendance_of_class_D_{b}.csv")
#     tmsg.showinfo("Download","Download Successfully")


def csv_A():
    global b    
    new=b 
    import pandas as pd
    import mysql.connector
    import tkinter.messagebox as tmsg
    db=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
    cursor=db.cursor()
    cursor = db.cursor()
    query = f"SELECT Roll_Number,Student_Name,Status,date from class_a where date='{new}' "
    cursor.execute(query)
    row = cursor.fetchall()
    w=[]
    x=[]
    y=[]
    z=[]
    for i in row:
        a=i[0]
        w.append(a)
        b=i[1]
        x.append(b)
        c=i[2]
        y.append(c)
        d=i[3]
        z.append(d)
    dictionary={'Roll_Number':w, 'Student_Name':x, 'Status':y, 'date': z}
    df=pd.DataFrame(dictionary)
    df_csv=df.to_csv(f"attendance_of_class_A_{new}.csv")
    tmsg.showinfo("Download","Download CSV Of Class-A  Successfully")
def csv_B():  
    global b    
    new=b   
    import pandas as pd
    import mysql.connector
    import tkinter.messagebox as tmsg
    db=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
    cursor=db.cursor()
    cursor = db.cursor()
    query = f"SELECT Roll_Number,Student_Name,Status,date from class_a where date='{new}' "
    cursor.execute(query)
    row = cursor.fetchall()
    w=[]
    x=[]
    y=[]
    z=[]
    for i in row:
        a=i[0]
        w.append(a)
        b=i[1]
        x.append(b)
        c=i[2]
        y.append(c)
        d=i[3]
        z.append(d)
    dictionary={'Roll_Number':w, 'Student_Name':x, 'Status':y, 'date': z}
    df=pd.DataFrame(dictionary)
    df_csv=df.to_csv(f"attendance_of_class_B_{new}.csv")
    tmsg.showinfo("Download","Download CSV Of Class-B  Successfully")
def csv_C():  
    global b    
    new=b   
    import pandas as pd
    import mysql.connector
    import tkinter.messagebox as tmsg
    db=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
    cursor=db.cursor()
    cursor = db.cursor()
    query = f"SELECT Roll_Number,Student_Name,Status,date from class_a where date='{new}' "
    cursor.execute(query)
    row = cursor.fetchall()
    w=[]
    x=[]
    y=[]
    z=[]
    for i in row:
        a=i[0]
        w.append(a)
        b=i[1]
        x.append(b)
        c=i[2]
        y.append(c)
        d=i[3]
        z.append(d)
    dictionary={'Roll_Number':w, 'Student_Name':x, 'Status':y, 'date': z}
    df=pd.DataFrame(dictionary)
    df_csv=df.to_csv(f"attendance_of_class_C_{new}.csv")
    tmsg.showinfo("Download","Download CSV Of Class-C  Successfully")
def csv_D(): 
    global b    
    new=b    
    import pandas as pd
    import mysql.connector
    import tkinter.messagebox as tmsg
    db=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
    cursor=db.cursor()
    cursor = db.cursor()
    query = f"SELECT Roll_Number,Student_Name,Status,date from class_a where date='{new}' "
    cursor.execute(query)
    row = cursor.fetchall()
    w=[]
    x=[]
    y=[]
    z=[]
    for i in row:
        a=i[0]
        w.append(a)
        b=i[1]
        x.append(b)
        c=i[2]
        y.append(c)
        d=i[3]
        z.append(d)
    dictionary={'Roll_Number':w, 'Student_Name':x, 'Status':y, 'date': z}
    df=pd.DataFrame(dictionary)
    df_csv=df.to_csv(f"attendance_of_class_D_{new}.csv")
    tmsg.showinfo("Download","Download CSV Of Class-D  Successfully")


# def csv_B(): 
#     global b   
#     import pandas as pd
#     import mysql.connector
#     import tkinter.messagebox as tmsg
#     db=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
#     cursor=db.cursor()
#     cursor = db.cursor()
#     query = f"SELECT Roll_Number,Student_Name,Status,date from class_b where date='{b}' "
#     cursor.execute(query)
#     row = cursor.fetchall()
#     w=[]
#     x=[]
#     y=[]
#     z=[]
#     for i in row:
#         a=i[0]
#         w.append(a)
#         b=i[1]
#         x.append(b)
#         c=i[2]
#         y.append(c)
#         d=i[3]
#         z.append(d)
#     dictionary={'Roll_Number':w, 'Student_Name':x, 'Status':y, 'date': z}
#     df=pd.DataFrame(dictionary)
#     df_csv=df.to_csv(f"attendance_of_class_B_{b}.csv")
#     tmsg.showinfo("Download","Download Successfully")
# def csv_C(): 
#     global b   
#     import pandas as pd
#     import mysql.connector
#     import tkinter.messagebox as tmsg
#     db=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
#     cursor=db.cursor()
#     cursor = db.cursor()
#     query = f"SELECT Roll_Number,Student_Name,Status,date from class_c where date='{b}' "
#     cursor.execute(query)
#     row = cursor.fetchall()
#     w=[]
#     x=[]
#     y=[]
#     z=[]
#     for i in row:
#         a=i[0]
#         w.append(a)
#         b=i[1]
#         x.append(b)
#         c=i[2]
#         y.append(c)
#         d=i[3]
#         z.append(d)
#     dictionary={'Roll_Number':w, 'Student_Name':x, 'Status':y, 'date': z}
#     df=pd.DataFrame(dictionary)
#     df_csv=df.to_csv(f"attendance_of_class_C_{b}.csv")
#     tmsg.showinfo("Download","Download Successfully")
# def csv_D():
#     global b    
#     import pandas as pd
#     import mysql.connector
#     import tkinter.messagebox as tmsg
#     db=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
#     cursor=db.cursor()
#     cursor = db.cursor()
#     query = f"SELECT Roll_Number,Student_Name,Status,date from class_d where date='{b}' "
#     cursor.execute(query)
#     row = cursor.fetchall()
#     w=[]
#     x=[]
#     y=[]
#     z=[]
#     for i in row:
#         a=i[0]
#         w.append(a)
#         b=i[1]
#         x.append(b)
#         c=i[2]
#         y.append(c)
#         d=i[3]
#         z.append(d)
#     dictionary={'Roll_Number':w, 'Student_Name':x, 'Status':y, 'date': z}
#     df=pd.DataFrame(dictionary)
#     df_csv=df.to_csv(f"attendance_of_class_D_{b}.csv")
#     tmsg.showinfo("Download","Download Successfully")
######For download CSV End###################################################################################
Label(root,text="RK University",justify=CENTER,font="lucida 19 bold",relief="raised",border=10).pack()
Label(root,text="Tamba Road,Rajkot",justify=CENTER,font="lucida 11").pack()
Label(root,text="Subject: Dynamic Attandance Python Project",justify=CENTER,font="lucida 11 bold").pack(pady=10)

Label(root,text="Guided By Snehal Sathwara",justify=CENTER,font="lucida 11 bold").pack(pady=10)
Label(root,text="Created By Jadav Vipul & Dadhaniya Myusi",justify=CENTER,font="lucida 11 bold").pack(pady=10)

######For menus start########################################################################################
mainmenu=Menu(root)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="Class-A",command=attandance_A)
m1.add_command(label="Class-B",command=attandance_B)
m1.add_command(label="Class-C",command=attandance_C)
m1.add_command(label="Class-D",command=attandance_D)
mainmenu.add_cascade(label="Pending Attandance",menu=m1)
m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="Class-A",command=show_attandance_A)
m2.add_command(label="Class-B",command=show_attandance_B)
m2.add_command(label="Class-C",command=show_attandance_C)
m2.add_command(label="Class-D",command=show_attandance_D)
mainmenu.add_cascade(label="Attandance",menu=m2)
m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="Class-A",command=show_present_A)
m3.add_command(label="Class-B",command=show_present_B)
m3.add_command(label="Class-C",command=show_present_C)
m3.add_command(label="Class-D",command=show_present_D)
mainmenu.add_cascade(label="Present",menu=m3)
m4=Menu(mainmenu,tearoff=0)
m4.add_command(label="Class-A",command=show_absent_A)
m4.add_command(label="Class-B",command=show_absent_B)
m4.add_command(label="Class-C",command=show_absent_C)
m4.add_command(label="Class-D",command=show_absent_D)
mainmenu.add_cascade(label="Absent",menu=m4)
m5=Menu(mainmenu,tearoff=0)
m5.add_command(label="Class-A",command=analysis_A)
m5.add_command(label="Class-B",command=analysis_B)
m5.add_command(label="Class-C",command=analysis_C)
m5.add_command(label="Class-D",command=analysis_D)
mainmenu.add_cascade(label="Analysis",menu=m5)
m6=Menu(mainmenu,tearoff=0)
m6.add_command(label="Class-A",command=csv_A)
m6.add_command(label="Class-B",command=csv_B)
m6.add_command(label="Class-C",command=csv_C)
m6.add_command(label="Class-D",command=csv_D)
mainmenu.add_cascade(label="Download CSV",menu=m6)

m7=Menu(mainmenu,tearoff=0)
m7.add_command(label="Goto Date",command=date)
mainmenu.add_cascade(label="Date",menu=m7)

root.config(menu=mainmenu)
root.mainloop()
######For menus End########################################################################################