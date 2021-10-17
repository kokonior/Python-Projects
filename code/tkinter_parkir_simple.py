# Python 3.7.x
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime

class Parkir():
    def __init__(self):
        self.root = Tk()
        self.datas = []
        self.root.title("Tiket Parkir by Kelompok 6")
        self.root.geometry("664x400+450+250")
        self.root.resizable(width=False, height=False)
        self.createHome()
        self.root.mainloop()

    def createHome(self):
        Label(self.root, text="Aplikasi Parkir Kelompok 6", font=('Comic Sans MS', 15)).place(x = 25,y = 10)
        #row 1
        Label(self.root, text="Cari NoPol", font=('Comic Sans MS', 10)).place(x=17, y=60)
        self.nopol = StringVar()
        Entry(self.root, textvariable=self.nopol).place(x=110, y=62)
        Button(self.root, text="Cari", font=('Comic Sans MS', 7), width=3, height=1, command=self.searchData).place(x=250, y=60)
        #row 2
        Label(self.root, text="No Plat Polisi", font=('Comic Sans MS', 10)).place(x=17, y=100)
        self.noplat = StringVar()
        Entry(self.root, textvariable=self.noplat).place(x=110, y=102)
        #row 3
        Label(self.root, text="Waktu Masuk", font=('Comic Sans MS', 10)).place(x=17, y=130)
        self.masuk = StringVar()
        Entry(self.root, textvariable=self.masuk).place(x=110, y=132)
        self.masuk.trace("w", self.updateMasuk)
        #row 4
        Label(self.root, text="Waktu Keluar", font=('Comic Sans MS', 10)).place(x=17, y=160)
        self.keluar = StringVar()
        Entry(self.root, textvariable=self.keluar).place(x=110, y=162)
        self.keluar.trace("w", self.updateKeluar)
        #row 4
        Label(self.root, text="Biaya", font=('Comic Sans MS', 10)).place(x=17, y=190)
        self.biaya = IntVar()
        Entry(self.root, textvariable=self.biaya).place(x=110, y=192)
        Button(self.root, text="Button", font=('Comic Sans MS', 7), width=5, height=1, command=self.insertDataTreeview1).place(x=250, y=190)
        #biaya per jam 2000
        Label(self.root, text="Biaya Per Jam", font=('Comic Sans MS', 20), fg="red").place(x=350, y=68)
        Label(self.root, text="Rp. 2.000", font=('Comic Sans MS', 35), fg="red").place(x=350, y=105)
        #---------------- treeview section -----------------#
        #label
        Label(self.root, text="List Pelanggan Urut Terakhir Keluar", font=('Comic Sans MS', 10), fg="blue").place(x=17, y=240)
        Label(self.root, text="List Pelanggan Banyak Bayar", font=('Comic Sans MS', 10), fg="blue").place(x=347, y=240)
        self.DataTreeview1()
        self.DataTreeview2()

    def DataTreeview1(self):
        self.treev = ttk.Treeview(selectmode ='browse', height=3) 
        self.treev.place(x=19,y=270) 
        verscrlbar = ttk.Scrollbar(
                self.root,  
                orient ="vertical",  
                command = self.treev.yview
            ) 
        verscrlbar.place(x=312, y=287)
        self.treev.configure(xscrollcommand = verscrlbar.set) 
        self.treev["columns"] = ("1", "2", "3", "4") 
        self.treev['show'] = 'headings'
        self.treev.column("1", width = 80, anchor ='c') 
        self.treev.column("2", width = 70, anchor ='se') 
        self.treev.column("3", width = 70, anchor ='se') 
        self.treev.column("4", width = 70, anchor ='se') 
        self.treev.heading("1", text ="No Plat Polisi") 
        self.treev.heading("2", text ="Masuk") 
        self.treev.heading("3", text ="Keluar")
        self.treev.heading("4", text ="Biaya") 
 
    def DataTreeview2(self):
        self.treev2 = ttk.Treeview(selectmode ='browse', height=3) 
        self.treev2.place(x=350,y=270) 
        verscrlbar = ttk.Scrollbar(
                self.root,  
                orient ="vertical",  
                command = self.treev2.yview
            ) 
        verscrlbar.place(x=643, y=287)
        self.treev2.configure(xscrollcommand = verscrlbar.set) 
        self.treev2["columns"] = ("1", "2", "3", "4") 
        self.treev2['show'] = 'headings'
        self.treev2.column("1", width = 80, anchor ='c') 
        self.treev2.column("2", width = 70, anchor ='se') 
        self.treev2.column("3", width = 70, anchor ='se') 
        self.treev2.column("4", width = 70, anchor ='se') 
        self.treev2.heading("1", text ="No Plat Polisi") 
        self.treev2.heading("2", text ="Masuk") 
        self.treev2.heading("3", text ="Keluar")
        self.treev2.heading("4", text ="Biaya")

    def insertDataTreeview1(self):
        self.datas.append(
            {
                'noplat': str(self.noplat.get()),
                'masuk': str(self.masuk.get()),
                'keluar': str(self.keluar.get()),
                'biaya': self.biaya.get()
            }
        )
        self.treev.insert("", 0, 
             values = (str(self.noplat.get()), str(self.masuk.get()), str(self.keluar.get()), self.biaya.get())) 
        self.clearDataTreeview2()
        self.insertDataTreeview2()

    def insertDataTreeview2(self):
        self.datas.sort(key=self.bSort)
        for x in self.datas:
            self.treev2.insert("", 0,
                values = (x['noplat'], x['masuk'], x['keluar'], x['biaya']))

    def clearDataTreeview2(self):
        try:
            for i in self.treev2.get_children():
                self.treev2.delete(i)
        except:
            print("error")
    
    def searchData(self):
        found = 0
        text = ""
        for z in self.datas:
            if str(z['noplat']).lower().strip() == str(self.nopol.get()).lower().strip():
                text += "No. {} | No Plat : {} | Jam Masuk : {} | Jam Keluar : {} | Biaya : Rp. {}".format(str(found + 1), str(z['noplat']), str(z['masuk']), str(z['keluar']), str(z['biaya']))+"\n"
                found += 1
        if found > 0:
            messagebox.showinfo("Hasil Pencarian : "+str(self.nopol.get()), message=text)
        else:
            messagebox.showerror("Tidak ditemukan", "Hasil pencarian : {} tidak ditemukan.".format(str(self.nopol.get())))

    def updateMasuk(self, *args):
        if(len(str(self.masuk.get()))) >= 8:
            if len(str(self.keluar.get())) >= 8:
                biaya = self.hitungParkir(self.masuk.get(), self.keluar.get())
                self.biaya.set(biaya)
                print(biaya)
        else:
            self.biaya.set("input jam masuk/keluar")

    def updateKeluar(self, *args):
        if(len(str(self.keluar.get()))) >= 8:
            if len(str(self.masuk.get())) >= 8:
                biaya = self.hitungParkir(self.masuk.get(), self.keluar.get())
                self.biaya.set(biaya)
                print(biaya)
        else:
            self.biaya.set("input jam masuk/keluar")

    def hitungParkir(self, masuk, keluar):
        jam_masuk = str(masuk)
        jam_keluar = str(keluar)
        get_hour = (datetime.strptime(jam_keluar, "%H:%M:%S") - datetime.strptime(jam_masuk, "%H:%M:%S")).seconds
        if (get_hour//3600) > 0 and (get_hour//60)%60 < 50:
            return get_hour//3600 * 2000 
        elif ((get_hour//60)%60) > 50: # lebih dari 50 menit terhitung 60 menit
            return ((get_hour//3600) + 1) * 2000
        else:
            return 2000

    def bSort(self, e):
        return e['biaya']

Parkir()
