
#ALİ YETKİN IRMAK
#Proje: klasör oluşturmak ve dosya kopyalamak
#Tarih: 31.07.2023 

import tkinter as tk
from tkinter import ttk
import os
from tkinter import filedialog as fd
import shutil
import calendar
from datetime import date

selected_year = None
selected_month = None
days_in_month = None

interface = tk.Tk()
interface.geometry("500x250")

months = ["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]

output_text = tk.Text(interface, width=60, height=5)
output_text.place(x=5,y=130)

def get_data_from_file(file_path):
    array = []
    with open(file_path, "r") as f:
        array = f.read().splitlines()
    return array

file_path = fd.askopenfilename(
  title="Departmanlar listesini seçin"
  )
depArr=get_data_from_file(file_path)

def on_submit():
    global selected_year, selected_month, days_in_month

    selected_year = int(year_var.get())
    selected_month = month_combobox.current() + 1  
    if selected_month == 2 and calendar.isleap(selected_year):
        days_in_month = 29
    else:
        days_in_month = calendar.monthrange(selected_year, selected_month)[1]

def create_widgets():
    global month_combobox  

    year_label = ttk.Label(interface, text="Yıl seç:")
    year_label.place(x=10,y=30)

    year_combobox = ttk.Combobox(interface, textvariable=year_var, state="readonly",values=list(range(current_year, 2050 + 1)))
    year_combobox.place(x=100,y=35)
    year_combobox.set(current_year) 

    month_label = ttk.Label(interface, text="Ay seç:")
    month_label.place(x=10,y=60)

    month_combobox = ttk.Combobox(interface,state="readonly", values=months)
    month_combobox.place(x=100,y=65)
    month_combobox.set(months[current_month - 1])

    dep_label = ttk.Label(interface,text="Departman seç:")
    dep_label.place(x=10,y=90)

    dep_combobox = ttk.Combobox(interface,state="readonly", textvariable=dep_var ,values=depArr)
    dep_combobox.place(x=100,y=90)
    dep_combobox.set(depArr[0])

current_year = date.today().year
current_month = date.today().month

dep_var=tk.StringVar()
year_var = tk.StringVar()

create_widgets()

def select_folder():
  
    global directory1
    directory1 = fd.askdirectory(
      title="Departmanların oluşacağı klasör"
    )
    if not directory1:
      output_text.config(state=tk.NORMAL)
      output_text.delete(1.0, tk.END)
      output_text.insert(tk.END,f"Departman klasörlerini oluşturmak için konum seçmediniz")
      output_text.config(state=tk.DISABLED)
      return
    create_dep_folders()

def create_dep_folders():
  
  on_submit()
  path=directory1

  for i in depArr:
    if not os.path.exists(os.path.join(path, i)):
      os.mkdir(os.path.join(path, i))
  
  on_submit()
  output_text.config(state=tk.NORMAL)
  output_text.delete(1.0, tk.END)
  output_text.insert(tk.END,f"Departman klasörleri {path} konumuna oluşturuldu")
  output_text.config(state=tk.DISABLED)

def select_file():
  
  on_submit()
  
  filenames = fd.askopenfilenames(
    title="Kopyalanacak dosyaları seçin"
  )
  output_text.config(state=tk.NORMAL)
  output_text.delete(1.0, tk.END) 
  output_text.insert(tk.END,f"Dosyalar kopyalandı")
  output_text.config(state=tk.DISABLED)

  if filenames:
    despath=fd.askdirectory(
      title="Departmanların bulunduğu klasörü seçin"
    )
    if not despath:
      output_text.config(state=tk.NORMAL)
      output_text.delete(1.0, tk.END)
      output_text.insert(tk.END,f"Dosyaları kopyalamak için hedef konum seçmediniz")
      output_text.config(state=tk.DISABLED)
      return
    if os.path.exists(os.path.join(despath,dep_var.get())):
      for filename in filenames:
        tstr=dep_var.get()
        ddpath=os.path.join(despath,tstr)
        ssy=os.path.join(ddpath,(str(selected_year)+"_"+str(selected_month)))
        if not os.path.exists(os.path.join(ddpath,ssy)):
          os.mkdir(os.path.join(ddpath,ssy))
        ga=str(selected_year)+"_"+str(selected_month)
        dddpath=os.path.join(ddpath,ga)
        for j in range (1,days_in_month+1):
          gun1=ga+"_"+str(j)
          fpath=os.path.join(dddpath,gun1)
          if not os.path.exists(fpath):
            os.mkdir(fpath)
          gun=os.path.join(dddpath,gun1)
          shutil.copy(filename,gun)
          gun1=ga
      output_text.config(state=tk.NORMAL)
      output_text.delete(1.0, tk.END)
      output_text.insert(tk.END,f"Seçilen dosyalar {ssy} konumuna kopyalandı")
      output_text.config(state=tk.DISABLED)
    else:
      output_text.config(state=tk.NORMAL)
      output_text.delete(1.0, tk.END)
      output_text.insert(tk.END,f"Departman klasörleri seçtiğiniz konumda değil")
      output_text.config(state=tk.DISABLED)
  output_text.config(state=tk.NORMAL)
  output_text.delete(1.0, tk.END)
  output_text.insert(tk.END,f"Kopyalanacak dosya seçmediniz")
  output_text.config(state=tk.DISABLED)
btn1 = tk.Button(text="Departman klasörlerini şuraya aç",command=select_folder)
btn1.place(x=10,y=5)
btn2 = tk.Button(text="Dosya seç ve seçilen tarihe kopyala",command=select_file)
btn2.place(x=260,y=90)


interface.mainloop()

