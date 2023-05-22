import tkinter as tk

root = tk.Tk()
root.config(height=350,width=670)
root.title("Ders İçi Kimlik Sistemi")
ilceler = ["ALPU", "BEYLİKOVA", "ÇİFTELER", "GÜNYÜZÜ", "HAN", "İNÖNÜ", "MAHMUDİYE", "MİHALGAZİ", "MİHALIÇÇIK", "ODUNPAZARI","SARICAKAYA", "SEYİTGAZİ", "SİVRİHİSAR", "TEPEBAŞI"]
cinsiyet = ["Kız","Erkek"]
sinif = ["9","10","11","12"]
lbl1 = tk.Label(text="İsim:", font="Arial 16 bold",bg="Gray",width=8)
lbl2 = tk.Label(text="Soyisim:", font="Arial 16 bold",bg="Gray",width=8)
lbl3 = tk.Label(text="Kimlik No:", font="Arial 16 bold",bg="Gray",width=8)
lbl4 = tk.Label(text="İlçe:", font="Arial 16 bold",bg="Gray",width=8)
lbl5 = tk.Label(text="Okul:", font="Arial 16 bold",bg="Gray",width=8)
lbl6 = tk.Label(text="Cinsiyet:", font="Arial 16 bold",bg="Gray",width=8)
lbl7 = tk.Label(text="Sınıf:", font="Arial 16 bold",bg="Gray",width=8)

def KAYDET():
    list1.insert(1, txt1.get())
    list1.insert(2, txt2.get())
    list1.insert(3, txt3.get())
    list1.insert(4, value1.get())
    list1.insert(5, txt4.get())
    list1.insert(6, value2.get())
    list1.insert(7, value3.get())
def TEMIZLE():
    list1.delete(first=0,last=8)

value1 = tk.StringVar(root)
value1.set("İlçe Seçiniz")
value2 = tk.StringVar(root)
value2.set("Cinsiyet Seçiniz")
value3 = tk.StringVar(root)
value3.set("Sınıf Seçiniz")

ops1 = tk.OptionMenu(root, value1, *ilceler)
ops2 = tk.OptionMenu(root, value2, *cinsiyet)
ops3 = tk.OptionMenu(root, value3, *sinif)

list1 = tk.Listbox()

txt1 = tk.Entry()
txt1.config(width=20)
txt2 = tk.Entry()
txt2.config(width=20)
txt3 = tk.Entry()
txt3.config(width=20)
txt4 = tk.Entry()
txt4.config(width=20)

btn1 = tk.Button(text="KAYDET", command=KAYDET, bg="Blue")
btn2 = tk.Button(text="TEMİZLE", command=TEMIZLE, bg="Red")

lbl1.place(x=10,y=10)
lbl2.place(x=10,y=40)
lbl3.place(x=10,y=70)
lbl4.place(x=10,y=100)
lbl5.place(x=300,y=10)
lbl6.place(x=300,y=40)
lbl7.place(x=300,y=70)

txt1.place(x=150,y=17)
txt2.place(x=150,y=47)
txt3.place(x=150,y=77)
txt4.place(x=440,y=17)

ops1.place(x=150,y=100)
ops2.place(x=440,y=40)
ops3.place(x=440,y=70)

btn1.place(x=400,y=110)
btn2.place(x=470,y=110)

list1.place(x=10,y=150)

root.mainloop()