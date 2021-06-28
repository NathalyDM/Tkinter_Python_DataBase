#imports
from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import random
import time
import datetime
# Hacer una base de datos y usuarios
with sqlite3.connect('quit.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEX NOT NULL);')
db.commit()
db.close()

#Clase principal
def cerrarventana():
    root.destroy()

def abrirventana2():
    root2=Tk()
    root2.title('Negocios')
    root2.geometry('1350x750+0+0')
    root2.config(bg="Lime Green")

    Tops=Frame(root2, width=1350, height=100, bd=14, relief="raise")
    Tops.pack(side=TOP)

    f1=Frame(root2, width=900, height=650, bd=8, relief="raise")
    f1.pack(side=LEFT)
    f2=Frame(root2, width=440, height=650, bd=8, relief="raise")
    f2.pack(side=RIGHT)

    ft2=Frame(f2, width=440, height=250, bd=12, relief="raise")
    ft2.pack(side=TOP)
    fb2=Frame(f2, width=440, height=450, bd=16, relief="raise")
    fb2.pack(side=BOTTOM)

    f1a=Frame(f1, width=900, height=330, bd=8, relief="raise")
    f1a.pack(side=TOP)
    f2a=Frame(f1, width=900, height=320, bd=6, relief="raise")
    f2a.pack(side=BOTTOM)

    f1aa=Frame(f1a, width=400, height=330, bd=16, relief="raise")
    f1aa.pack(side=LEFT)
    f1ab=Frame(f1a, width=400, height=330, bd=16, relief="raise")
    f1ab.pack(side=RIGHT)

    f2aa=Frame(f2a, width=450, height=330, bd=14, relief="raise")
    f2aa.pack(side=LEFT)
    f2ab=Frame(f2a, width=450, height=330, bd=14, relief="raise")
    f2ab.pack(side=RIGHT)

    Tops.configure(background="Dark Orange")
    f1.configure(background="Lime Green")
    f2.configure(background="Lime Green")
    lblinfo= Label(Tops, font=("arial",50,"bold"), text="       Sistema de Administración Jugería        ", bd=10)
    lblinfo.grid(row=0,column=0)

    def salida():
        salida= ms.askyesno("Saliendo del sistema", "¿Quieres salir del programa?")
        if salida>0:
         root2.destroy()

    def reset():
        date.set(time.strftime("%d/%m/%Y"))
        PaidTax.set("")
        SubTotal.set("")
        Totalcost.set("")
        Costotorta.set("")
        Costodrink.set("")
        Serviciocargo.set("")
        txtrecibido.delete("1.0",END)

        txtMango.configure(state= DISABLED)
        txtpiña.configure(state= DISABLED)
        txtfresa.configure(state= DISABLED)
        txtpapaya.configure(state= DISABLED)
        txtplatano.configure(state= DISABLED)
        txtkiwi.configure(state= DISABLED)
        txtsurtido.configure(state= DISABLED)
        txtespecial.configure(state= DISABLED)
        txtchoco.configure(state= DISABLED)
        txtpie.configure(state= DISABLED)
        txthamb.configure(state= DISABLED)
        txtsand.configure(state= DISABLED)
        txtbolog.configure(state= DISABLED)
        txtpiña.configure(state= DISABLED)
        txtfruta.configure(state= DISABLED)
        txtfruta.configure(state= DISABLED)
        txtmenu.configure(state= DISABLED)

        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)


        E_Mango.set("0")
        E_piña.set("0")
        E_fresa.set("0")
        E_papaya.set("0")
        E_platano.set("0")
        E_kiwi.set("0")
        E_surtido.set("0")
        E_especial.set("0")
        E_choco.set("0")
        E_pie.set("0")
        E_hamb.set("0")
        E_sand.set("0")
        E_bolog.set("0")
        E_piñas.set("0")
        E_fruta.set("0")
        E_menu.set("0")



    def piña():
        if(var2.get()==1):
            txtpiña.configure(state=NORMAL)
        elif var2.get()==0:
            txtpiña.configure(state=DISABLED)
            E_piña.set("0")
    def fresa():
        if(var3.get()==1):
            txtfresa.configure(state=NORMAL)
        elif var3.get()==0:
            txtfresa.configure(state=DISABLED)
            E_fresa.set("0")
    def papaya():
        if(var4.get()==1):
            txtpapaya.configure(state=NORMAL)
        elif var4.get()==0:
            txtpapaya.configure(state=DISABLED)
            E_papaya.set("0")
    def platano():
        if(var5.get()==1):
            txtplatano.configure(state=NORMAL)
        elif var5.get()==0:
            txtplatano.configure(state=DISABLED)
            E_platano.set("0")
    def kiwi():
        if(var6.get()==1):
            txtkiwi.configure(state=NORMAL)
        elif var6.get()==0:
            txtkiwi.configure(state=DISABLED)
            E_kiwi.set("0")
    def surtido():
        if(var7.get()==1):
            txtsurtido.configure(state=NORMAL)
        elif var7.get()==0:
            txtsurtido.configure(state=DISABLED)
            E_surtido.set("0")
    def especial():
        if(var8.get()==1):
            txtespecial.configure(state=NORMAL)
        elif var8.get()==0:
            txtespecial.configure(state=DISABLED)
            E_especial.set("0")
    def choco():
        if(var9.get()==1):
            txtchoco.configure(state=NORMAL)
        elif var9.get()==0:
            txtchoco.configure(state=DISABLED)
            E_choco.set("0")
    def pie():
        if(var10.get()==1):
            txtpie.configure(state=NORMAL)
        elif var10.get()==0:
            txtpie.configure(state=DISABLED)
            E_pie.set("0")
    def hamb():
        if(var11.get()==1):
            txthamb.configure(state=NORMAL)
        elif var11.get()==0:
            txthamb.configure(state=DISABLED)
            E_hamb.set("0")
    def sand():
        if(var12.get()==1):
            txtsand.configure(state=NORMAL)
        elif var12.get()==0:
            txtsand.configure(state=DISABLED)
            E_sand.set("0")
    def bolog():
        if(var13.get()==1):
            txtbolog.configure(state=NORMAL)
        elif var13.get()==0:
            txtbolog.configure(state=DISABLED)
            E_bolog.set("0")
    def piñas():
        if(var14.get()==1):
            txtpiñas.configure(state=NORMAL)
        elif var14.get()==0:
            txtpiñas.configure(state=DISABLED)
            E_piñas.set("0")
    def fruta():
        if(var15.get()==1):
            txtfruta.configure(state=NORMAL)
        elif var15.get()==0:
            txtfruta.configure(state=DISABLED)
            E_fruta.set("0")
    def menu():
        if(var16.get()==1):
            txtmenu.configure(state=NORMAL)
        elif var16.get()==0:
            txtmenu.configure(state=DISABLED)
            E_menu.set("0")
    def mango():
        if var1.get()==1:
            txtMango.configure(state=NORMAL)
        elif var1.get()==0:
            txtMango.configure(state=DISABLED)
            E_Mango.set("0")



    def COSTOITEM():
        item1=int(E_Mango.get())
        item2=int(E_piña.get())
        item3=int(E_fresa.get())
        item4=int(E_papaya.get())
        item5=int(E_platano.get())
        item6=int(E_kiwi.get())
        item7=int(E_surtido.get())
        item8=int(E_especial.get())
        item9=int(E_choco.get())
        item10=int(E_pie.get())
        item11=int(E_hamb.get())
        item12=int(E_sand.get())
        item13=int(E_bolog.get())
        item14=int(E_piñas.get())
        item15=int(E_fruta.get())
        item16=int(E_menu.get())

        preciodebebidas=(item1*6)+(item2*6)+(item3*6)+(item4*7)+(item5*8)+(item6*8)+(item7*9)+(item8*9)
        precioape=(item9*5)+(item10*5)+(item11*6)+(item12*6)+(item13*10)+(item14*6)+(item15*8)+(item16*8)

        cbeb="s/.",str("%.2f"%(preciodebebidas))
        cape="s/.",str("%.2f"%(precioape))
        Costotorta.set(cape)
        Costodrink.set(cbeb)
        CS="s/.",str("%.2f"%(4.59))
        Serviciocargo.set(CS)

        SubTotalitems="s/.",str("%.2f"%(precioape+preciodebebidas))
        SubTotal.set(SubTotalitems)

        Tax="s/.",str("%.2f"%((precioape+preciodebebidas)*0.18))
        PaidTax.set(Tax)
        TT=((preciodebebidas+preciodebebidas)*0.18)
        TCost=(preciodebebidas+precioape+TT)
        Totalcost.set(TCost)

    def RECIBO():
        txtrecibido.delete("1.0",END)
        x=random.randint(1000000,99999999)
        randomRef=str(x)
        Recibo_Ref.set("URL"+randomRef)

        txtrecibido.insert(END,"Recibo RUC:\t\t\t"+Recibo_Ref.get()+"\t\t"+date.get()+"\n")
        txtrecibido.insert(END,"ITEMS:\t\t\t\t\t"+"Costo de items \n\n")
        txtrecibido.insert(END,"Jugo de Mango:\t\t\t\t"+E_Mango.get()+"\n")
        txtrecibido.insert(END,"Jugo de Piña:\t\t\t\t"+E_piña.get()+"\n")
        txtrecibido.insert(END,"Jugo de Fresa:\t\t\t\t"+E_fresa.get()+"\n")
        txtrecibido.insert(END,"Jugo de Papaya:\t\t\t\t"+E_papaya.get()+"\n")
        txtrecibido.insert(END,"Jugo de Plátano:\t\t\t\t"+E_platano.get()+"\n")
        txtrecibido.insert(END,"Jugo de Kiwi:\t\t\t\t"+E_kiwi.get()+"\n")
        txtrecibido.insert(END,"Surtido:\t\t\t\t"+E_surtido.get()+"\n")
        txtrecibido.insert(END,"Especial:\t\t\t\t"+E_especial.get()+"\n")
        txtrecibido.insert(END,"Pastel de chocolate:\t\t\t\t"+E_choco.get()+"\n")
        txtrecibido.insert(END,"Pie de manzana/durazno:\t\t\t\t"+E_pie.get()+"\n")
        txtrecibido.insert(END,"Hamburguesa:\t\t\t\t"+E_hamb.get()+"\n")
        txtrecibido.insert(END,"Sandwich de pollo:\t\t\t\t"+E_sand.get()+"\n")
        txtrecibido.insert(END,"Bolognesa:\t\t\t\t"+E_bolog.get()+"\n")
        txtrecibido.insert(END,"Pie acaramelado de Piña:\t\t\t\t"+E_piñas+"\n")
        txtrecibido.insert(END,"Ensalada de fruta:\t\t\t\t"+E_fruta.get()+"\n")
        txtrecibido.insert(END,"Menu del dia:\t\t\t\t"+E_menu()+"\n")
        txtrecibido.insert(END,"Costos de bebidas:\t\t"+Costodrink.get()+ "\tIGV:\t\t"+PaidTax.get()+"\n")
        txtrecibido.insert(END,"Costos de aperitivos:\t\t"+Costotorta.get()+ "\tSub Total:\t\t"+SubTotal.get()+"\n")
        txtrecibido.insert(END,"Cargo por servicios:\t\t"+Serviciocargo.get()+ "\tCosto Total:\t\t"+Totalcost.get()+"\n")
    date=StringVar()
    PaidTax=StringVar()
    SubTotal=StringVar()
    Totalcost=StringVar()
    Costotorta=StringVar()
    Costodrink=StringVar()
    Serviciocargo=StringVar()
    Recibo_Ref=StringVar()

    E_Mango=StringVar()
    E_piña=StringVar()
    E_fresa=StringVar()
    E_papaya=StringVar()
    E_platano=StringVar()
    E_kiwi=StringVar()
    E_surtido=StringVar()
    E_especial=StringVar()
    E_choco=StringVar()
    E_pie=StringVar()
    E_hamb=StringVar()
    E_sand=StringVar()
    E_bolog=StringVar()
    E_piñas=StringVar()
    E_fruta=StringVar()
    E_menu=StringVar()

    var1=IntVar()
    var2=IntVar()
    var3=IntVar()
    var4=IntVar()
    var5=IntVar()
    var6=IntVar()
    var7=IntVar()
    var8=IntVar()
    var9=IntVar()
    var10=IntVar()
    var11=IntVar()
    var12=IntVar()
    var13=IntVar()
    var14=IntVar()
    var15=IntVar()
    var16=IntVar()

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)

    E_Mango.set("0")
    E_piña.set("0")
    E_fresa.set("0")
    E_papaya.set("0")
    E_platano.set("0")
    E_kiwi.set("0")
    E_surtido.set("0")
    E_especial.set("0")
    E_choco.set("0")
    E_pie.set("0")
    E_hamb.set("0")
    E_sand.set("0")
    E_bolog.set("0")
    E_piñas.set("0")
    E_fruta.set("0")
    E_menu.set("0")


    Mango=Checkbutton(f1aa, text="Jugo de Mango    \t", variable=var1, onvalue=1, offvalue=0, font=("arial",18,"bold"), command=mango).grid(row=0, column=0)
    Piña=Checkbutton(f1aa, text="Jugo de Piña    \t", variable=var2, onvalue=1, offvalue=0, font=("arial",18,"bold"), command=piña).grid(row=1, column=0)
    Fresa=Checkbutton(f1aa, text="Jugo de Fresa    \t", variable=var3, onvalue=1, offvalue=0, font=("arial",18,"bold"), command=fresa).grid(row=2, column=0)
    Papaya=Checkbutton(f1aa, text="Jugo de Papaya   \t", variable=var4, onvalue=1, offvalue=0, font=("arial",18,"bold"), command=papaya).grid(row=3, column=0)
    Platano=Checkbutton(f1aa, text="Jugo de Plátano  \t", variable=var5, onvalue=1, offvalue=0, font=("arial",18,"bold"), command=platano).grid(row=4, column=0)
    Kiwi=Checkbutton(f1aa, text="Jugo de Kiwi    \t", variable=var6, onvalue=1, offvalue=0, font=("arial",18,"bold"),command=kiwi).grid(row=5, column=0)
    Surtido=Checkbutton(f1aa, text="Jugo Surtido    \t", variable=var7, onvalue=1, offvalue=0, font=("arial",18,"bold"),command=surtido).grid(row=6, column=0)
    Especial=Checkbutton(f1aa, text="Jugo Special    \t", variable=var8, onvalue=1, offvalue=0, font=("arial",18,"bold"),command=especial).grid(row=7, column=0)

    tchoco=Checkbutton(f1ab, text="Pastel de chocolate \t", variable=var9, onvalue=1, offvalue=0, font=("arial",18,"bold"),command=choco).grid(row=0, column=0)
    tpie=Checkbutton(f1ab, text="Pie de manzana o platano\t", variable=var10, onvalue=1, offvalue=0, font=("arial",18,"bold"),command=pie).grid(row=1, column=0)
    hamb=Checkbutton(f1ab, text="Hamburguesa con papas \t", variable=var11, onvalue=1, offvalue=0, font=("arial",18,"bold"),command=hamb).grid(row=2, column=0)
    sand=Checkbutton(f1ab, text="Sandwich de pollo \t", variable=var12, onvalue=1, offvalue=0, font=("arial",18,"bold"),command=sand).grid(row=3, column=0)
    bolognesa=Checkbutton(f1ab, text="Fideos a la bolognesa \t", variable=var13, onvalue=1, offvalue=0, font=("arial",18,"bold"),command=bolog).grid(row=4, column=0)
    piñas=Checkbutton(f1ab, text="Pie de piña acaramelada \t", variable=var14, onvalue=1, offvalue=0, font=("arial",18,"bold"),command=piñas).grid(row=5, column=0)
    fruta=Checkbutton(f1ab, text="Ensalada de frutas\t", variable=var15, onvalue=1, offvalue=0, font=("arial",18,"bold"),command=fruta).grid(row=6, column=0)
    menu=Checkbutton(f1ab, text="Menú del día/desayuno\t", variable=var16, onvalue=1, offvalue=0, font=("arial",18,"bold"),command=menu).grid(row=7, column=0)


    txtMango=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left", textvariable=E_Mango,state= DISABLED)
    txtMango.grid(row=0, column=1)
    txtpiña=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left", textvariable=E_piña,state= DISABLED)
    txtpiña.grid(row=1, column=1)
    txtfresa=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",  textvariable=E_fresa,state= DISABLED)
    txtfresa.grid(row=2, column=1)
    txtpapaya=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left", textvariable=E_papaya,state= DISABLED)
    txtpapaya.grid(row=3, column=1)
    txtplatano=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left", textvariable=E_platano,state= DISABLED)
    txtplatano.grid(row=4, column=1)
    txtkiwi=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left", textvariable=E_kiwi,state= DISABLED)
    txtkiwi.grid(row=5, column=1)
    txtsurtido=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left", textvariable=E_surtido,state= DISABLED)
    txtsurtido.grid(row=6, column=1)
    txtespecial=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left", textvariable=E_especial,state= DISABLED)
    txtespecial.grid(row=7, column=1)

    txtchoco=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left", textvariable=E_choco,state= DISABLED)
    txtchoco.grid(row=0, column=1)
    txtpie=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_pie, state= DISABLED)
    txtpie.grid(row=1, column=1)
    txthamb=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_hamb, state= DISABLED)
    txthamb.grid(row=2, column=1)
    txtsand=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_sand,state= DISABLED)
    txtsand.grid(row=3, column=1)
    txtbolog=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_bolog,state= DISABLED)
    txtbolog.grid(row=4, column=1)
    txtpiñas=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_piñas,state= DISABLED)
    txtpiñas.grid(row=5, column=1)
    txtfruta=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_fruta,state= DISABLED)
    txtfruta.grid(row=6, column=1)
    txtmenu=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_menu,state= DISABLED)
    txtmenu.grid(row=7, column=1)


    lblreceipt= Label(ft2,font=("arial",12,"bold"),text="Recibido", bd=2, justify="left",textvariable=Recibo_Ref).grid(row=0, column=0, sticky=W)
    txtrecibido= Text(ft2,font=("arial",12,"bold"),bd=8,width=40, height=20)
    txtrecibido.grid(row=1,column=0)
#----------------------
    btnTotal=Button(fb2, padx=16,pady=1,bd=4,fg="black",font=("arial",14,"bold"), width=4, text="Total",command=COSTOITEM).grid(row=0, column=0)
    btnRecibo=Button(fb2, padx=16,pady=1,bd=4,fg="black",font=("arial",14,"bold"), width=4, text="Recibo",command=RECIBO).grid(row=0, column=1)
    btnReset=Button(fb2, padx=16,pady=1,bd=4,fg="black",font=("arial",14,"bold"), width=4, text="Nuevo",command=reset).grid(row=0, column=2)
    btnExit=Button(fb2, padx=16,pady=1,bd=4,fg="black",font=("arial",14,"bold"), width=4, text="Salir", command=salida).grid(row=0, column=3)

    lblcostofru=Label(f2aa, font=("arial",16,"bold"),text="Costo Frugos", bd=8).grid(row=0, column=0, sticky=W)
    lblcostofru=Entry(f2aa,font=("arial",16,"bold"),bd=8, justify="left",textvariable=Costodrink).grid(row=0, column=1, sticky=W)

    lblcostoape=Label(f2aa, font=("arial",16,"bold"),text="Costo Aperitivos", bd=8).grid(row=1, column=0, sticky=W)
    lblcostoape=Entry(f2aa,font=("arial",16,"bold"),bd=8,justify="left",textvariable=Costotorta).grid(row=1, column=1, sticky=W)

    lblcostoser=Label(f2aa, font=("arial",16,"bold"),text="Cargo servicio", bd=8).grid(row=2, column=0, sticky=W)
    lblcostoser=Entry(f2aa,font=("arial",16,"bold"),bd=8,justify="left",textvariable=Serviciocargo).grid(row=2, column=1, sticky=W)

#________Información
    lblcostoigv=Label(f2ab, font=("arial",16,"bold"),text="IGV", bd=8).grid(row=0, column=0, sticky=W)
    lblcostoigv=Entry(f2ab,font=("arial",16,"bold"),bd=8, justify="left", textvariable=PaidTax).grid(row=0, column=1, sticky=W)

    lblcostosub=Label(f2ab, font=("arial",16,"bold"),text="Sub Total", bd=8).grid(row=1, column=0, sticky=W)
    lblcostosub=Entry(f2ab,font=("arial",16,"bold"),bd=8,justify="left",textvariable=SubTotal).grid(row=1, column=1, sticky=W)

    lblcostot=Label(f2ab, font=("arial",16,"bold"),text="Total", bd=8).grid(row=2, column=0, sticky=W)
    lblcostot=Entry(f2ab,font=("arial",16,"bold"),bd=8,justify="left",textvariable=Totalcost).grid(row=2, column=1, sticky=W)



    root2.mainloop()


class main:
    def __init__(self,master):
    	# Window
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()

    #Función login
    def login(self):
    	#Establecer conección
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #_____encontrando usuario
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] =  "Bienvenida \n" + self.username.get()
            self.head['pady'] = 150
            cerrarventana()
            abrirventana2()

        else:
            ms.showerror('Uy','Nombre de usuario no encontrado.')

    def new_user(self):
    	#Establecer conección
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Encontrar usuario
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.username.get())])
        if c.fetchall():
            ms.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Crear nueva cuenta
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()

        #Ventana para empacar metodos
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Crear Cuenta'
        self.crf.pack()

    # Widgets
    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',font = ('',35),pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10)
        Label(self.logf,text = 'Usuario: ',font = ('',18),pady=10,padx=10, ).grid(sticky = W,),
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('',18),pady=10,padx=10).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('',13),padx=10,pady=10,command=self.login).grid()
        Button(self.logf,text = ' Crear cuenta ',bd = 3 ,font = ('',13),padx=10,pady=10,command=self.cr).grid(row=2,column=1)
        self.logf.pack()

        self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = 'Usuario: ',font = ('',18),pady=10,padx=10).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',font = ('',18),pady=10,padx=10).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.crf,text = 'Crear cuenta',bd = 3 ,font = ('',13),padx=10,pady=10,command=self.new_user).grid()
        Button(self.crf,text = 'Ir a Login',bd = 3 ,font = ('',13),padx=10,pady=10,command=self.log).grid(row=2,column=1)



if __name__ == '__main__':
    root = Tk()
    root.title('Login Form')
    root.geometry('350x300+300+300')
    root.config(bg="#DAF7A6")
    root.wm_iconbitmap("C:\Trabajo\persona.ico.ico")
    main(root)
    root.mainloop()
