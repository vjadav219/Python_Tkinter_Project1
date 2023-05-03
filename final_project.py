from tkinter import *
from tkcalendar import Calendar
root = Tk() 
root.geometry("500x300")
root.title("by vipul")
root.iconbitmap("images.ico")
root.config(bg="light gray")

####for select date Start###################################################################################
def date(): 
    def getCustomDate():
        global b
        print(cal.get_date())
        b=cal.get_date()
        return b
####for select date End###################################################################################
    
    def goto():
        
        # from tkinter import *
        from tkinter import ttk
        import mysql.connector
        import tkinter.messagebox as tmsg

        root = Tk() 
        root.geometry("500x500")
        root.title("By Vipul")
        root.iconbitmap("images.ico")
        root.config(bg="light gray")

########Class A attandance Start #######################################################################
        def attandance_A():
            from tkinter import ttk
            import mysql.connector
            import tkinter as tk 
            import tkinter.messagebox as tmsg
            root = Tk() 
            root.geometry("500x500")
            root.title("By Vipul")
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

            var1=tk.IntVar(second_frame)
            var2=tk.IntVar(second_frame)
            var3=tk.IntVar(second_frame)
            var4=tk.IntVar(second_frame)
            var5=tk.IntVar(second_frame)
            var6=tk.IntVar(second_frame)
            var7=tk.IntVar(second_frame)
            var8=tk.IntVar(second_frame)
            var9=tk.IntVar(second_frame)
            var10=tk.IntVar(second_frame)
            var11=tk.IntVar(second_frame)
            var12=tk.IntVar(second_frame)
            var13=tk.IntVar(second_frame)
            var14=tk.IntVar(second_frame)
            var15=tk.IntVar(second_frame)
            var16=tk.IntVar(second_frame)
            var17=tk.IntVar(second_frame)
            var18=tk.IntVar(second_frame)
            var19=tk.IntVar(second_frame)
            var20=tk.IntVar(second_frame)
            var21=tk.IntVar(second_frame)
            var22=tk.IntVar(second_frame)
            var23=tk.IntVar(second_frame)
            var24=tk.IntVar(second_frame)
            var25=tk.IntVar(second_frame)
            var26=tk.IntVar(second_frame)
            var27=tk.IntVar(second_frame)
            var28=tk.IntVar(second_frame)
            var29=tk.IntVar(second_frame)
            var30=tk.IntVar(second_frame)
            var31=tk.IntVar(second_frame)
            var32=tk.IntVar(second_frame)
            var33=tk.IntVar(second_frame)
            var34=tk.IntVar(second_frame)
            var35=tk.IntVar(second_frame)
            var36=tk.IntVar(second_frame)
            var37=tk.IntVar(second_frame)
            var38=tk.IntVar(second_frame)
            var39=tk.IntVar(second_frame)
            var40=tk.IntVar(second_frame)
            var41=tk.IntVar(second_frame)
            var42=tk.IntVar(second_frame)
            var43=tk.IntVar(second_frame)
            var44=tk.IntVar(second_frame)
            var45=tk.IntVar(second_frame)
            var46=tk.IntVar(second_frame)
            var47=tk.IntVar(second_frame)
            var48=tk.IntVar(second_frame)
            var49=tk.IntVar(second_frame)
            var50=tk.IntVar(second_frame)
            var51=tk.IntVar(second_frame)
            var52=tk.IntVar(second_frame)
            var53=tk.IntVar(second_frame)
            var54=tk.IntVar(second_frame)
            var55=tk.IntVar(second_frame)
            var56=tk.IntVar(second_frame)
            var57=tk.IntVar(second_frame)
            var58=tk.IntVar(second_frame)
            var59=tk.IntVar(second_frame)
            var60=tk.IntVar(second_frame)
            var61=tk.IntVar(second_frame)
            var62=tk.IntVar(second_frame)
            var63=tk.IntVar(second_frame)
            var64=tk.IntVar(second_frame)
            var65=tk.IntVar(second_frame)
            new=[var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21,var22,var23,var24,var25,var26,var27,var28,var29,var30,var31,var32,var33,var34,var35,var36,var37,var38,var39,var40,var41,var42,var43,var44,var45,var46,var47,var48,var49,var50,var51,var52,var53,var54,var55,var56,var57,var58,var59,var60,var61,var62,var63,var64,var65]
            for i in new:
                i=i.set(1)
            def check():
                for i,j,k in zip(new,ab,number):
                    # print(i.get())
                    if(i.get()==1):
                        print(f"{k} is present")
                        connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
                        mycursor=connection.cursor()
                        # mycursor.execute('insert into vipul values("j ","k"); ')
                        mycursor.execute("INSERT INTO class_a VALUES (%s, %s,%s,%s)", (k, j,"present",b))
                        connection.commit()
                    else:
                        print(f"{k} is absent")
                        connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
                        mycursor=connection.cursor()
                        # mycursor.execute('insert into vipul values("j" ,"k"); ')  
                        mycursor.execute("INSERT INTO class_a VALUES (%s, %s,%s,%s)", (k, j,"absent",b))          
                        connection.commit()
                tmsg.showinfo("attandance","Saved Successfully")

            Label(second_frame,text="Click To Present Student",justify=CENTER,padx=14,font="verdana  15 bold").pack()
            ab=["BALDHA JEET RANCHHODBHA","BARACH PAAWAN PIYUSHBHA","BHATT JANVI SANDIPBHA","BHENSADADIYA ESHA RAKESHBHA","BHUT MEET DILIPBHA","BHUVA JAYRAJ RAJUBHA","CHAUHAN HARSH RAMESHBHA","CHAUHAN RIDDHI CHANDULA","CHAVDA MITESH DINESHBHAI","CHHAYANI VIRAJ BHARATBHAI","CHUDASAMA ABHAY PRAVINBHAI","DABHI HARPALBHAI RANJITBHAI","DADHANIYA MYUSI MANOJBHAI","DALAL KHUSHI YATINKUMAR","DASLANIYA DHRUVIL VIPULBHAI","DAVADA KRISHNA HITESHBHAI","DER SAHILKUMAR JITUBHAI","DHRANGI ASHISHKUMAR SHANKARBHAI","FALDU KESHVI RAJENDRAKUMAR","FATANIYA KEYUR HITESHBHAI","GADHIYA AFSIN NAUSHAD","GOHEL KRISH BHARATBHAI","GOR JEELKUMAR VIRENDRAKUMAR","GOSWAMI VINITPURI RAMESHPURI","GUNDIGARA ADITYA ROHITBHAI","HALAI AKSHAY NANJI","HIRANI SIDDHI NARANBHAI","JADAV KHUSHI NILESHBHAI","JADAV VIPUL BATUKBHAI","JAKASANIYA YASHKUMAR KANTILAL","JASANI BHARGAV JAYSUKHBHAI","JESADIYA DIPKUMAR HASMUKHBHAI","JETHVA JAYKUMAR MAHESHBHAI","JOGI ANKUL ASHOKBHAI","JOSHI DIVYARAJ CHANDRAMANI","KACHCHHI ELESH PARESHBHAI","KACHHADIYA YATRI RAJESHBHAI","KAPURIYA HIMANSHU BHARATBHAI","KARELIYA KISHANBHAI LIMBABHAI","KASUNDRA BANSI NARENDRABHAI","KATHIRIYA YASH NARSHIBHAI","KERALIYA DARSH HITESHBHAI","KHAMBHAYATA PRERNA HARESHBHAI","KHOLIYA HARSH PRADEEPBHAI","KHUNT VARSHIL MAHENDRABHAI","KOLADIYA PUNJAN PRAFULBHAI","KOTHIYA MEET DHANSUKHBHAI","MEHTA VARUN KETANBHAI","MEPANI VRINDABEN VASANTBHAI","MORI KULDIP JAGDISHBHAI","ODEDRA ARJUN MUNJABHAI","PARGADU MANISHA CHAMPASHIBHAI","PARMAR VAIBHAV GOVINDBHAI","PIPARIYA JAY JAYSUKHBHAI","RADADIYA BANSI JIVANBHAI","RAMANI SMITKUMAR JITESHKUMAR","RAMAVAT DIV RAMADEV","SABHADIYA JEET BHUPATBHAI","VAGADIYA MANOJ PUNJABHAI","VAISHNAV NEEVA DENISHKUMAR","VASANI HENIL JAGDISHBHAI","VIRANI JAY PRAVINBHAI","ZALAVADIYA VIVEK DINESHBHAI","ANDANI RAHIL ASHOKBHAI","GOLETAR MALAY SURESHBHAI"]
            for i,j in zip(ab,new):
                Checkbutton(second_frame, text =i, variable=j,onvalue = 1, offvalue = 0).pack()
            Button(root, text ="save",command=check).pack()
            Button(root, text ="close", command =root.destroy).pack()
            root.mainloop()
########Class A attandance End################################################################################
########Class B attandance Start ################################################################################
        def attandance_B():
            from tkinter import ttk
            import mysql.connector
            import tkinter as tk 
            import tkinter.messagebox as tmsg

            root = Tk() 
            root.geometry("500x500")
            root.title("By Vipul")
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

            var1=tk.IntVar(second_frame)
            var2=tk.IntVar(second_frame)
            var3=tk.IntVar(second_frame)
            var4=tk.IntVar(second_frame)
            var5=tk.IntVar(second_frame)
            var6=tk.IntVar(second_frame)
            var7=tk.IntVar(second_frame)
            var8=tk.IntVar(second_frame)
            var9=tk.IntVar(second_frame)
            var10=tk.IntVar(second_frame)
            var11=tk.IntVar(second_frame)
            var12=tk.IntVar(second_frame)
            var13=tk.IntVar(second_frame)
            var14=tk.IntVar(second_frame)
            var15=tk.IntVar(second_frame)
            var16=tk.IntVar(second_frame)
            var17=tk.IntVar(second_frame)
            var18=tk.IntVar(second_frame)
            var19=tk.IntVar(second_frame)
            var20=tk.IntVar(second_frame)
            var21=tk.IntVar(second_frame)
            var22=tk.IntVar(second_frame)
            var23=tk.IntVar(second_frame)
            var24=tk.IntVar(second_frame)
            var25=tk.IntVar(second_frame)
            var26=tk.IntVar(second_frame)
            var27=tk.IntVar(second_frame)
            var28=tk.IntVar(second_frame)
            var29=tk.IntVar(second_frame)
            var30=tk.IntVar(second_frame)
            var31=tk.IntVar(second_frame)
            var32=tk.IntVar(second_frame)
            var33=tk.IntVar(second_frame)
            var34=tk.IntVar(second_frame)
            var35=tk.IntVar(second_frame)
            var36=tk.IntVar(second_frame)
            var37=tk.IntVar(second_frame)
            var38=tk.IntVar(second_frame)
            var39=tk.IntVar(second_frame)
            var40=tk.IntVar(second_frame)
            var41=tk.IntVar(second_frame)
            var42=tk.IntVar(second_frame)
            var43=tk.IntVar(second_frame)
            var44=tk.IntVar(second_frame)
            var45=tk.IntVar(second_frame)
            var46=tk.IntVar(second_frame)
            var47=tk.IntVar(second_frame)
            var48=tk.IntVar(second_frame)
            var49=tk.IntVar(second_frame)
            var50=tk.IntVar(second_frame)
            var51=tk.IntVar(second_frame)
            var52=tk.IntVar(second_frame)
            var53=tk.IntVar(second_frame)
            var54=tk.IntVar(second_frame)
            var55=tk.IntVar(second_frame)
            var56=tk.IntVar(second_frame)
            var57=tk.IntVar(second_frame)
            var58=tk.IntVar(second_frame)
            var59=tk.IntVar(second_frame)
            var60=tk.IntVar(second_frame)
            var61=tk.IntVar(second_frame)
            var62=tk.IntVar(second_frame)
            var63=tk.IntVar(second_frame)
            var64=tk.IntVar(second_frame)
            var65=tk.IntVar(second_frame)
            new=[var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21,var22,var23,var24,var25,var26,var27,var28,var29,var30,var31,var32,var33,var34,var35,var36,var37,var38,var39,var40,var41,var42,var43,var44,var45,var46,var47,var48,var49,var50,var51,var52,var53,var54,var55,var56,var57,var58,var59,var60,var61,var62,var63,var64,var65]
            for i in new:
                i=i.set(1)
            def check():
                for i,j,k in zip(new,ab,number):
                    # print(i.get())
                    if(i.get()==1):
                        # print(f"{k} is present")
                        connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
                        mycursor=connection.cursor()
                        # mycursor.execute('insert into vipul values("j ","k"); ')
                        mycursor.execute("INSERT INTO class_b VALUES (%s, %s,%s,%s)", (k, j,"present",b))
                        connection.commit()

                    else:
                        # print(f"{k} is absent")
                        connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
                        mycursor=connection.cursor()
                        # mycursor.execute('insert into vipul values("j" ,"k"); ')  
                        mycursor.execute("INSERT INTO class_b VALUES (%s, %s,%s,%s)", (k, j,"absent",b))          
                        connection.commit()
                tmsg.showinfo("attandance","Saved Successfully")
            Label(second_frame,text="Click To Present Student",justify=CENTER,padx=14,font="verdana  15 bold").pack()
            ab=["BALDHA JEET RANCHHODBHA","BARACH PAAWAN PIYUSHBHA","BHATT JANVI SANDIPBHA","BHENSADADIYA ESHA RAKESHBHA","BHUT MEET DILIPBHA","BHUVA JAYRAJ RAJUBHA","CHAUHAN HARSH RAMESHBHA","CHAUHAN RIDDHI CHANDULA","CHAVDA MITESH DINESHBHAI","CHHAYANI VIRAJ BHARATBHAI","CHUDASAMA ABHAY PRAVINBHAI","DABHI HARPALBHAI RANJITBHAI","DADHANIYA MYUSI MANOJBHAI","DALAL KHUSHI YATINKUMAR","DASLANIYA DHRUVIL VIPULBHAI","DAVADA KRISHNA HITESHBHAI","DER SAHILKUMAR JITUBHAI","DHRANGI ASHISHKUMAR SHANKARBHAI","FALDU KESHVI RAJENDRAKUMAR","FATANIYA KEYUR HITESHBHAI","GADHIYA AFSIN NAUSHAD","GOHEL KRISH BHARATBHAI","GOR JEELKUMAR VIRENDRAKUMAR","GOSWAMI VINITPURI RAMESHPURI","GUNDIGARA ADITYA ROHITBHAI","HALAI AKSHAY NANJI","HIRANI SIDDHI NARANBHAI","JADAV KHUSHI NILESHBHAI","JADAV VIPUL BATUKBHAI","JAKASANIYA YASHKUMAR KANTILAL","JASANI BHARGAV JAYSUKHBHAI","JESADIYA DIPKUMAR HASMUKHBHAI","JETHVA JAYKUMAR MAHESHBHAI","JOGI ANKUL ASHOKBHAI","JOSHI DIVYARAJ CHANDRAMANI","KACHCHHI ELESH PARESHBHAI","KACHHADIYA YATRI RAJESHBHAI","KAPURIYA HIMANSHU BHARATBHAI","KARELIYA KISHANBHAI LIMBABHAI","KASUNDRA BANSI NARENDRABHAI","KATHIRIYA YASH NARSHIBHAI","KERALIYA DARSH HITESHBHAI","KHAMBHAYATA PRERNA HARESHBHAI","KHOLIYA HARSH PRADEEPBHAI","KHUNT VARSHIL MAHENDRABHAI","KOLADIYA PUNJAN PRAFULBHAI","KOTHIYA MEET DHANSUKHBHAI","MEHTA VARUN KETANBHAI","MEPANI VRINDABEN VASANTBHAI","MORI KULDIP JAGDISHBHAI","ODEDRA ARJUN MUNJABHAI","PARGADU MANISHA CHAMPASHIBHAI","PARMAR VAIBHAV GOVINDBHAI","PIPARIYA JAY JAYSUKHBHAI","RADADIYA BANSI JIVANBHAI","RAMANI SMITKUMAR JITESHKUMAR","RAMAVAT DIV RAMADEV","SABHADIYA JEET BHUPATBHAI","VAGADIYA MANOJ PUNJABHAI","VAISHNAV NEEVA DENISHKUMAR","VASANI HENIL JAGDISHBHAI","VIRANI JAY PRAVINBHAI","ZALAVADIYA VIVEK DINESHBHAI","ANDANI RAHIL ASHOKBHAI","GOLETAR MALAY SURESHBHAI"]
            for i,j in zip(ab,new):
                Checkbutton(second_frame, text =i, variable=j,onvalue = 1, offvalue = 0).pack()
            Button(root, text ="save",command=check).pack()
            Button(root, text ="close", command =root.destroy).pack()
            root.mainloop()
########Class B attandance End#########################################################################
########Class C attandance Start ######################################################################
        def attandance_C():
            from tkinter import ttk
            import mysql.connector
            import tkinter as tk 
            import tkinter.messagebox as tmsg

            root = Tk() 
            root.geometry("500x500")
            root.title("By Vipul")
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
            var1=tk.IntVar(second_frame)
            var2=tk.IntVar(second_frame)
            var3=tk.IntVar(second_frame)
            var4=tk.IntVar(second_frame)
            var5=tk.IntVar(second_frame)
            var6=tk.IntVar(second_frame)
            var7=tk.IntVar(second_frame)
            var8=tk.IntVar(second_frame)
            var9=tk.IntVar(second_frame)
            var10=tk.IntVar(second_frame)
            var11=tk.IntVar(second_frame)
            var12=tk.IntVar(second_frame)
            var13=tk.IntVar(second_frame)
            var14=tk.IntVar(second_frame)
            var15=tk.IntVar(second_frame)
            var16=tk.IntVar(second_frame)
            var17=tk.IntVar(second_frame)
            var18=tk.IntVar(second_frame)
            var19=tk.IntVar(second_frame)
            var20=tk.IntVar(second_frame)
            var21=tk.IntVar(second_frame)
            var22=tk.IntVar(second_frame)
            var23=tk.IntVar(second_frame)
            var24=tk.IntVar(second_frame)
            var25=tk.IntVar(second_frame)
            var26=tk.IntVar(second_frame)
            var27=tk.IntVar(second_frame)
            var28=tk.IntVar(second_frame)
            var29=tk.IntVar(second_frame)
            var30=tk.IntVar(second_frame)
            var31=tk.IntVar(second_frame)
            var32=tk.IntVar(second_frame)
            var33=tk.IntVar(second_frame)
            var34=tk.IntVar(second_frame)
            var35=tk.IntVar(second_frame)
            var36=tk.IntVar(second_frame)
            var37=tk.IntVar(second_frame)
            var38=tk.IntVar(second_frame)
            var39=tk.IntVar(second_frame)
            var40=tk.IntVar(second_frame)
            var41=tk.IntVar(second_frame)
            var42=tk.IntVar(second_frame)
            var43=tk.IntVar(second_frame)
            var44=tk.IntVar(second_frame)
            var45=tk.IntVar(second_frame)
            var46=tk.IntVar(second_frame)
            var47=tk.IntVar(second_frame)
            var48=tk.IntVar(second_frame)
            var49=tk.IntVar(second_frame)
            var50=tk.IntVar(second_frame)
            var51=tk.IntVar(second_frame)
            var52=tk.IntVar(second_frame)
            var53=tk.IntVar(second_frame)
            var54=tk.IntVar(second_frame)
            var55=tk.IntVar(second_frame)
            var56=tk.IntVar(second_frame)
            var57=tk.IntVar(second_frame)
            var58=tk.IntVar(second_frame)
            var59=tk.IntVar(second_frame)
            var60=tk.IntVar(second_frame)
            var61=tk.IntVar(second_frame)
            var62=tk.IntVar(second_frame)
            var63=tk.IntVar(second_frame)
            var64=tk.IntVar(second_frame)
            var65=tk.IntVar(second_frame)
            new=[var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21,var22,var23,var24,var25,var26,var27,var28,var29,var30,var31,var32,var33,var34,var35,var36,var37,var38,var39,var40,var41,var42,var43,var44,var45,var46,var47,var48,var49,var50,var51,var52,var53,var54,var55,var56,var57,var58,var59,var60,var61,var62,var63,var64,var65]
            for i in new:
                i=i.set(1)
            def check():
                for i,j,k in zip(new,ab,number):
                    # print(i.get())
                    if(i.get()==1):
                        # print(f"{k} is present")
                        connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
                        mycursor=connection.cursor()
                        # mycursor.execute('insert into vipul values("j ","k"); ')
                        mycursor.execute("INSERT INTO class_c VALUES (%s, %s,%s,%s)", (k, j,"present",b))
                        connection.commit()

                    else:
                        # print(f"{k} is absent")
                        connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
                        mycursor=connection.cursor()
                        # mycursor.execute('insert into vipul values("j" ,"k"); ')  
                        mycursor.execute("INSERT INTO class_c VALUES (%s, %s,%s,%s)", (k, j,"absent",b))          
                        connection.commit()
                tmsg.showinfo("attandance","Saved Successfully")
            Label(second_frame,text="Click To Present Student",justify=CENTER,padx=14,font="verdana  15 bold").pack()
            ab=["BALDHA JEET RANCHHODBHA","BARACH PAAWAN PIYUSHBHA","BHATT JANVI SANDIPBHA","BHENSADADIYA ESHA RAKESHBHA","BHUT MEET DILIPBHA","BHUVA JAYRAJ RAJUBHA","CHAUHAN HARSH RAMESHBHA","CHAUHAN RIDDHI CHANDULA","CHAVDA MITESH DINESHBHAI","CHHAYANI VIRAJ BHARATBHAI","CHUDASAMA ABHAY PRAVINBHAI","DABHI HARPALBHAI RANJITBHAI","DADHANIYA MYUSI MANOJBHAI","DALAL KHUSHI YATINKUMAR","DASLANIYA DHRUVIL VIPULBHAI","DAVADA KRISHNA HITESHBHAI","DER SAHILKUMAR JITUBHAI","DHRANGI ASHISHKUMAR SHANKARBHAI","FALDU KESHVI RAJENDRAKUMAR","FATANIYA KEYUR HITESHBHAI","GADHIYA AFSIN NAUSHAD","GOHEL KRISH BHARATBHAI","GOR JEELKUMAR VIRENDRAKUMAR","GOSWAMI VINITPURI RAMESHPURI","GUNDIGARA ADITYA ROHITBHAI","HALAI AKSHAY NANJI","HIRANI SIDDHI NARANBHAI","JADAV KHUSHI NILESHBHAI","JADAV VIPUL BATUKBHAI","JAKASANIYA YASHKUMAR KANTILAL","JASANI BHARGAV JAYSUKHBHAI","JESADIYA DIPKUMAR HASMUKHBHAI","JETHVA JAYKUMAR MAHESHBHAI","JOGI ANKUL ASHOKBHAI","JOSHI DIVYARAJ CHANDRAMANI","KACHCHHI ELESH PARESHBHAI","KACHHADIYA YATRI RAJESHBHAI","KAPURIYA HIMANSHU BHARATBHAI","KARELIYA KISHANBHAI LIMBABHAI","KASUNDRA BANSI NARENDRABHAI","KATHIRIYA YASH NARSHIBHAI","KERALIYA DARSH HITESHBHAI","KHAMBHAYATA PRERNA HARESHBHAI","KHOLIYA HARSH PRADEEPBHAI","KHUNT VARSHIL MAHENDRABHAI","KOLADIYA PUNJAN PRAFULBHAI","KOTHIYA MEET DHANSUKHBHAI","MEHTA VARUN KETANBHAI","MEPANI VRINDABEN VASANTBHAI","MORI KULDIP JAGDISHBHAI","ODEDRA ARJUN MUNJABHAI","PARGADU MANISHA CHAMPASHIBHAI","PARMAR VAIBHAV GOVINDBHAI","PIPARIYA JAY JAYSUKHBHAI","RADADIYA BANSI JIVANBHAI","RAMANI SMITKUMAR JITESHKUMAR","RAMAVAT DIV RAMADEV","SABHADIYA JEET BHUPATBHAI","VAGADIYA MANOJ PUNJABHAI","VAISHNAV NEEVA DENISHKUMAR","VASANI HENIL JAGDISHBHAI","VIRANI JAY PRAVINBHAI","ZALAVADIYA VIVEK DINESHBHAI","ANDANI RAHIL ASHOKBHAI","GOLETAR MALAY SURESHBHAI"]
            for i,j in zip(ab,new):
                Checkbutton(second_frame, text =i, variable=j,onvalue = 1, offvalue = 0).pack()
            Button(root, text ="save",command=check).pack()
            Button(root, text ="close", command =root.destroy).pack()
            root.mainloop()
########Class C attandance End###################################################################################################
########Class D attandance Start ################################################################################################
        def attandance_D():
            from tkinter import ttk
            import mysql.connector
            import tkinter as tk 
            import tkinter.messagebox as tmsg

            root = Tk() 
            root.geometry("500x500")
            root.title("By Vipul")
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
            var1=tk.IntVar(second_frame)
            var2=tk.IntVar(second_frame)
            var3=tk.IntVar(second_frame)
            var4=tk.IntVar(second_frame)
            var5=tk.IntVar(second_frame)
            var6=tk.IntVar(second_frame)
            var7=tk.IntVar(second_frame)
            var8=tk.IntVar(second_frame)
            var9=tk.IntVar(second_frame)
            var10=tk.IntVar(second_frame)
            var11=tk.IntVar(second_frame)
            var12=tk.IntVar(second_frame)
            var13=tk.IntVar(second_frame)
            var14=tk.IntVar(second_frame)
            var15=tk.IntVar(second_frame)
            var16=tk.IntVar(second_frame)
            var17=tk.IntVar(second_frame)
            var18=tk.IntVar(second_frame)
            var19=tk.IntVar(second_frame)
            var20=tk.IntVar(second_frame)
            var21=tk.IntVar(second_frame)
            var22=tk.IntVar(second_frame)
            var23=tk.IntVar(second_frame)
            var24=tk.IntVar(second_frame)
            var25=tk.IntVar(second_frame)
            var26=tk.IntVar(second_frame)
            var27=tk.IntVar(second_frame)
            var28=tk.IntVar(second_frame)
            var29=tk.IntVar(second_frame)
            var30=tk.IntVar(second_frame)
            var31=tk.IntVar(second_frame)
            var32=tk.IntVar(second_frame)
            var33=tk.IntVar(second_frame)
            var34=tk.IntVar(second_frame)
            var35=tk.IntVar(second_frame)
            var36=tk.IntVar(second_frame)
            var37=tk.IntVar(second_frame)
            var38=tk.IntVar(second_frame)
            var39=tk.IntVar(second_frame)
            var40=tk.IntVar(second_frame)
            var41=tk.IntVar(second_frame)
            var42=tk.IntVar(second_frame)
            var43=tk.IntVar(second_frame)
            var44=tk.IntVar(second_frame)
            var45=tk.IntVar(second_frame)
            var46=tk.IntVar(second_frame)
            var47=tk.IntVar(second_frame)
            var48=tk.IntVar(second_frame)
            var49=tk.IntVar(second_frame)
            var50=tk.IntVar(second_frame)
            var51=tk.IntVar(second_frame)
            var52=tk.IntVar(second_frame)
            var53=tk.IntVar(second_frame)
            var54=tk.IntVar(second_frame)
            var55=tk.IntVar(second_frame)
            var56=tk.IntVar(second_frame)
            var57=tk.IntVar(second_frame)
            var58=tk.IntVar(second_frame)
            var59=tk.IntVar(second_frame)
            var60=tk.IntVar(second_frame)
            var61=tk.IntVar(second_frame)
            var62=tk.IntVar(second_frame)
            var63=tk.IntVar(second_frame)
            var64=tk.IntVar(second_frame)
            var65=tk.IntVar(second_frame)
            new=[var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21,var22,var23,var24,var25,var26,var27,var28,var29,var30,var31,var32,var33,var34,var35,var36,var37,var38,var39,var40,var41,var42,var43,var44,var45,var46,var47,var48,var49,var50,var51,var52,var53,var54,var55,var56,var57,var58,var59,var60,var61,var62,var63,var64,var65]
            for i in new:
                i=i.set(1)
            def check():
                for i,j,k in zip(new,ab,number):
                    # print(i.get())
                    if(i.get()==1):
                        # print(f"{k} is present")
                        connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
                        mycursor=connection.cursor()
                        # mycursor.execute('insert into vipul values("j ","k"); ')
                        mycursor.execute("INSERT INTO class_d VALUES (%s, %s,%s,%s)", (k, j,"present",b))
                        connection.commit()

                    else:
                        # print(f"{k} is absent")
                        connection=mysql.connector.connect(host="localhost",user="root",password="",database="python_final_project")
                        mycursor=connection.cursor()
                        # mycursor.execute('insert into vipul values("j" ,"k"); ')  
                        mycursor.execute("INSERT INTO class_d VALUES (%s, %s,%s,%s)", (k, j,"absent",b))          
                        connection.commit()
                tmsg.showinfo("attandance","Saved Successfully")
            Label(second_frame,text="Click To Present Student",justify=CENTER,padx=14,font="verdana  15 bold").pack()
            ab=["BALDHA JEET RANCHHODBHA","BARACH PAAWAN PIYUSHBHA","BHATT JANVI SANDIPBHA","BHENSADADIYA ESHA RAKESHBHA","BHUT MEET DILIPBHA","BHUVA JAYRAJ RAJUBHA","CHAUHAN HARSH RAMESHBHA","CHAUHAN RIDDHI CHANDULA","CHAVDA MITESH DINESHBHAI","CHHAYANI VIRAJ BHARATBHAI","CHUDASAMA ABHAY PRAVINBHAI","DABHI HARPALBHAI RANJITBHAI","DADHANIYA MYUSI MANOJBHAI","DALAL KHUSHI YATINKUMAR","DASLANIYA DHRUVIL VIPULBHAI","DAVADA KRISHNA HITESHBHAI","DER SAHILKUMAR JITUBHAI","DHRANGI ASHISHKUMAR SHANKARBHAI","FALDU KESHVI RAJENDRAKUMAR","FATANIYA KEYUR HITESHBHAI","GADHIYA AFSIN NAUSHAD","GOHEL KRISH BHARATBHAI","GOR JEELKUMAR VIRENDRAKUMAR","GOSWAMI VINITPURI RAMESHPURI","GUNDIGARA ADITYA ROHITBHAI","HALAI AKSHAY NANJI","HIRANI SIDDHI NARANBHAI","JADAV KHUSHI NILESHBHAI","JADAV VIPUL BATUKBHAI","JAKASANIYA YASHKUMAR KANTILAL","JASANI BHARGAV JAYSUKHBHAI","JESADIYA DIPKUMAR HASMUKHBHAI","JETHVA JAYKUMAR MAHESHBHAI","JOGI ANKUL ASHOKBHAI","JOSHI DIVYARAJ CHANDRAMANI","KACHCHHI ELESH PARESHBHAI","KACHHADIYA YATRI RAJESHBHAI","KAPURIYA HIMANSHU BHARATBHAI","KARELIYA KISHANBHAI LIMBABHAI","KASUNDRA BANSI NARENDRABHAI","KATHIRIYA YASH NARSHIBHAI","KERALIYA DARSH HITESHBHAI","KHAMBHAYATA PRERNA HARESHBHAI","KHOLIYA HARSH PRADEEPBHAI","KHUNT VARSHIL MAHENDRABHAI","KOLADIYA PUNJAN PRAFULBHAI","KOTHIYA MEET DHANSUKHBHAI","MEHTA VARUN KETANBHAI","MEPANI VRINDABEN VASANTBHAI","MORI KULDIP JAGDISHBHAI","ODEDRA ARJUN MUNJABHAI","PARGADU MANISHA CHAMPASHIBHAI","PARMAR VAIBHAV GOVINDBHAI","PIPARIYA JAY JAYSUKHBHAI","RADADIYA BANSI JIVANBHAI","RAMANI SMITKUMAR JITESHKUMAR","RAMAVAT DIV RAMADEV","SABHADIYA JEET BHUPATBHAI","VAGADIYA MANOJ PUNJABHAI","VAISHNAV NEEVA DENISHKUMAR","VASANI HENIL JAGDISHBHAI","VIRANI JAY PRAVINBHAI","ZALAVADIYA VIVEK DINESHBHAI","ANDANI RAHIL ASHOKBHAI","GOLETAR MALAY SURESHBHAI"]
            for i,j in zip(ab,new):
                Checkbutton(second_frame, text =i, variable=j,onvalue = 1, offvalue = 0).pack()
            Button(root, text ="save",command=check).pack()
            Button(root, text ="close", command =root.destroy).pack()
            root.mainloop()
########Class D attandance End##########################################################################################
########Class A show attandance Start###################################################################################       
        def show_attandance_A():     
            from tkinter import ttk
            import mysql.connector
            import tkinter.messagebox as tmsg
            root = Tk() 
            root.geometry("500x300")
            root.title("by vipul")
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
            num=2
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
            if(num==2):
                tmsg.showinfo("error","Data not found")
            else:
                tmsg.showinfo("attandance",f"total {num-2} student in Class A")
            connection.commit() 
            root.mainloop()
########Class A show attandance End###################################################################################
########Class B show attandance Start#################################################################################
        def show_attandance_B():     
            from tkinter import ttk
            import mysql.connector
            import tkinter.messagebox as tmsg
            root = Tk() 
            root.geometry("500x300")
            root.title("by vipul")
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
            num=2
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
            if(num==2):
                tmsg.showinfo("error","Data not found")
            else:
                tmsg.showinfo("attandance",f"total {num-2} student in Class B")                
            connection.commit() 
            root.mainloop()
########Class B show attandance End###################################################################################
########Class C show attandance Start#################################################################################
        def show_attandance_C():     
            from tkinter import ttk
            import mysql.connector
            import tkinter.messagebox as tmsg
            root = Tk() 
            root.geometry("500x300")
            root.title("by vipul")
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
            num=2
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
            if(num==2):
                tmsg.showinfo("error","Data not found")
            else:
                tmsg.showinfo("attandance",f"total {num-2} student in Class C")
            connection.commit() 
            root.mainloop()
########Class C show attandance End#################################################################################
########Class D show attandance Start#################################################################################       
        def show_attandance_D():     
            from tkinter import ttk
            import mysql.connector
            import tkinter.messagebox as tmsg
            root = Tk() 
            root.geometry("500x300")
            root.title("by vipul")
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
            num=2
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
            if(num==2):
                tmsg.showinfo("error","Data not found")
            else:
                tmsg.showinfo("attandance",f"total {num-2} student in Class D")
            connection.commit() 
            root.mainloop() 
########Class D show attandance End#################################################################################
########For Present Start###########################################################################################        
        def show_present_A():
            from tkinter import ttk
            import mysql.connector
            import tkinter.messagebox as tmsg
            root = Tk() 
            root.geometry("500x300")
            root.title("by vipul")
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
            num=2
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
            if(num==2):
                tmsg.showinfo("error","Data not found")
            else:
                tmsg.showinfo("attandance",f"total {num-2} present in Class A")
            connection.commit() 
            root.mainloop()

        def show_present_B():
            from tkinter import ttk
            import mysql.connector
            import tkinter.messagebox as tmsg
            root = Tk() 
            root.geometry("500x300")
            root.title("by vipul")
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
            num=2
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
            if(num==2):
                tmsg.showinfo("error","Data not found")
            else:
                tmsg.showinfo("attandance",f"total {num-2} present in Class B")                
            connection.commit() 
            root.mainloop()
        def show_present_C():
            from tkinter import ttk
            import mysql.connector
            import tkinter.messagebox as tmsg
            root = Tk() 
            root.geometry("500x300")
            root.title("by vipul")
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
            num=2
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
            if(num==2):
                tmsg.showinfo("error","Data not found")
            else:
                tmsg.showinfo("attandance",f"total {num-2} present in Class C")
            connection.commit() 
            root.mainloop()

        def show_present_D():
            from tkinter import ttk
            import mysql.connector
            import tkinter.messagebox as tmsg
            root = Tk() 
            root.geometry("500x300")
            root.title("by vipul")
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
            num=2
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
            if(num==2):
                tmsg.showinfo("error","Data not found")
            else:
                tmsg.showinfo("attandance",f"total {num-2} present in Class D")
            connection.commit() 
            root.mainloop()
########For Present End###########################################################################################
########For absent Start########################################################################################## 
        def show_absent_A():
            from tkinter import ttk
            import mysql.connector
            import tkinter.messagebox as tmsg
            root = Tk() 
            root.geometry("500x300")
            root.title("by vipul")
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
            num=2
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
            if(num==2):
                tmsg.showinfo("error","Data not found")
            else:
                tmsg.showinfo("attandance",f"total {num-2} absent in Class A")
            connection.commit() 
            root.mainloop()
        def show_absent_B():
            from tkinter import ttk
            import mysql.connector
            import tkinter.messagebox as tmsg
            root = Tk() 
            root.geometry("500x300")
            root.title("by vipul")
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
            num=2
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
            if(num==2):
                tmsg.showinfo("error","Data not found")
            else:
                tmsg.showinfo("attandance",f"total {num-2} absent in Class B")
            connection.commit() 
            root.mainloop()
        def show_absent_C():
            from tkinter import ttk
            import mysql.connector
            import tkinter.messagebox as tmsg
            root = Tk() 
            root.geometry("500x300")
            root.title("by vipul")
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
            num=2
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
            if(num==2):
                tmsg.showinfo("error","Data not found")
            else:
                tmsg.showinfo("attandance",f"total {num-2} absent in Class C")
            connection.commit() 
            root.mainloop()
        def show_absent_D():
            from tkinter import ttk
            import mysql.connector
            import tkinter.messagebox as tmsg
            root = Tk() 
            root.geometry("500x300")
            root.title("by vipul")
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
            num=2
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
            if(num==2):
                tmsg.showinfo("error","Data not found")
            else:
                tmsg.showinfo("attandance",f"total {num-2} absent in Class D")
            connection.commit() 
            root.mainloop()
########For absent End#############################################################################################    
########For matplotlib bar Start###################################################################################
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
            root.geometry("700x520")
            root.title("by vipul")
            root.iconbitmap("images.ico")
            root.config(bg="light gray")
            fig,ax=plt.subplots()
            
            frame=tk.Frame(root)
            lable=tk.Label(text="Class A")
            lable.config(font=("Courier",32))
            lable.pack()
            
            plt.xlabel("Date",fontsize=20)
            plt.ylabel("Present Rate",fontsize=20)
            
            canvas =FigureCanvasTkAgg(fig,master=root)
            canvas.get_tk_widget().pack()

            toolbar=NavigationToolbar2Tk(canvas,frame,pack_toolbar=False)
            toolbar.pack()
            ax.bar(x,y)
            
            for i in range(len(x)):
                plt.text(i,y[i],y[i],ha="center",va="bottom")
                        
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
            root.geometry("600x600")
            root.title("by vipul")
            root.iconbitmap("images.ico")
            root.config(bg="light gray")
            fig,ax=plt.subplots()
            
            frame=tk.Frame(root)
            lable=tk.Label(text="Class B")
            lable.config(font=("Courier",32))
            lable.pack()
            
            plt.xlabel("Date",fontsize=20)
            plt.ylabel("Present Rate",fontsize=20)
            
            canvas =FigureCanvasTkAgg(fig,master=root)
            canvas.get_tk_widget().pack()
            toolbar=NavigationToolbar2Tk(canvas,frame,pack_toolbar=False)
            toolbar.pack()
            ax.bar(x,y)
            
            for i in range(len(x)):
                plt.text(i,y[i],y[i],ha="center",va="bottom")
                        
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
            root.geometry("600x600")
            root.title("by vipul")
            root.iconbitmap("images.ico")
            root.config(bg="light gray")
            fig,ax=plt.subplots()
            
            frame=tk.Frame(root)
            lable=tk.Label(text="Class C")
            lable.config(font=("Courier",32))
            lable.pack()
            
            plt.xlabel("Date",fontsize=20)
            plt.ylabel("Present Rate",fontsize=20)
            
            canvas =FigureCanvasTkAgg(fig,master=root)
            canvas.get_tk_widget().pack()
            toolbar=NavigationToolbar2Tk(canvas,frame,pack_toolbar=False)
            toolbar.pack()
            ax.bar(x,y)
            
            for i in range(len(x)):
                plt.text(i,y[i],y[i],ha="center",va="bottom")
                        
            plt.show()
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
            root.geometry("600x600")
            root.title("by vipul")
            root.iconbitmap("images.ico")
            root.config(bg="light gray")
            fig,ax=plt.subplots()
            
            frame=tk.Frame(root)
            lable=tk.Label(text="Class D")
            lable.config(font=("Courier",32))
            lable.pack()
            
            plt.xlabel("Date",fontsize=20)
            plt.ylabel("Present Rate",fontsize=20)
            
            canvas =FigureCanvasTkAgg(fig,master=root)
            canvas.get_tk_widget().pack()
            toolbar=NavigationToolbar2Tk(canvas,frame,pack_toolbar=False)
            toolbar.pack()
            ax.bar(x,y)
            
            for i in range(len(x)):
                plt.text(i,y[i],y[i],ha="center",va="bottom")
                        
            plt.show()
            frame.pack()
            root.mainloop()
########For matplotlib bar End###################################################################################
########For download CSV Start###################################################################################
        new=b
        def csv_A():    
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
            df_csv=df.to_csv("attendance.csv")
            tmsg.showinfo("Download","Download Successfully")

        def csv_B():    
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
            df_csv=df.to_csv("attendance.csv")
            tmsg.showinfo("Download","Download Successfully")
        def csv_C():    
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
            df_csv=df.to_csv("attendance.csv")
            tmsg.showinfo("Download","Download Successfully")
        def csv_D():    
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
            df_csv=df.to_csv("attendance.csv")
            tmsg.showinfo("Download","Download Successfully")
########For download CSV End###################################################################################

        Label(root,text="RK University",justify=CENTER,font="lucida 19 bold").pack()
        Label(root,text="Tamba Road,Rajkot",justify=CENTER,font="lucida 11").pack()

########For menus start########################################################################################
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
        mainmenu.add_cascade(label="Show Attandance",menu=m2)

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
        mainmenu.add_cascade(label="download CSV",menu=m6)

        root.config(menu=mainmenu)
        root.mainloop()
########For menus End########################################################################################
    
    cal = Calendar(root,selectmode="day",firstweekday="monday",background="#0f8bff",foreground="black",disabledforeground="#a3bec7",bordercolor="grey",normalbackground="#d0f4ff",weekendbackground="#8ffeff",weekendforeground ="black",disabledbackground="99b3bc",date_pattern="dd-mm-yyyy")
    cal.pack(pady=10)
    getdate=Button(root, text="Select", bg="#00ffde", command=getCustomDate).pack()
    getdate1=Button(root, text="Go Next", bg="#00ffde", command=goto).pack()
    root.mainloop()

Button(root, text="Choose Date", bg="#00ffde", command=date).pack()
root.mainloop()