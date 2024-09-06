import tkinter as tk
import os
import sqlite3
import shutil
import json
import locale
import urllib.request
import tkinter.colorchooser as cc
import requests
import subprocess
import random
from tkinter import ttk
from tkinter import filedialog
from tkinter import Scrollbar
from urllib.request import urlopen
from urllib.error import URLError
from datetime import datetime
from PIL import Image
from PIL import ImageTk
from tkinter import END
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import os
import sqlite3



root = tk.Tk()
root.title('PyFloraPosuda')
root.configure(bg='#BAFFD2')
root.geometry('1100x700')
root.resizable(True, True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the coordinates to center the root window
window_width = 1100
window_height = 700
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the geometry of the root window
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

#1.slika
image_file = ''
image = tk.PhotoImage(file=image_file)
image_label = tk.Label(root, bg='#BAFFD2', image=image)
image_label.place(x=50, y=50)

#okvir za unos polja
frame = tk.Frame(root, width=400, height=650, bg='#BAFFD2')
frame.place(x=520, y=130)
 
login=tk.Label(frame, text='Prijava', bg='#BAFFD2', fg='black', font=('century', 26, 'bold'))
login.place(x=90, y=0)
#--------------------------VRIJEME----I POCETNI PROZOR-----------------------------------------------------------------------

locale.setlocale(locale.LC_ALL, 'hr_HR.UTF-8')

time_label = tk.Label(root, text="", font=('century', 12), bg='#4BF180')
def update_datetime():
    now = datetime.now()
    time_label.config(text=now.strftime("%A, %d.%m.%Y.\nSat:%H:%M"))
    root.after(1000, update_datetime)  #1 sec update
update_datetime()

def open_biljke():
    if user.get() == "Sara55" and PassWind.get() == "1234" or selected_choices.get=="BILJKE":
        image_label.place_forget()
        frame.place_forget()
        login.place_forget()
        UserName.place_forget()
        user.place_forget()
        UserPass.place_forget()
        PassWind.place_forget()
        button_prijava.place_forget()
        UserNew.place_forget()
        button_reg.place_forget()
        frame_dodaj_pot1.place_forget()
        naziv_biljke.place_forget()
        naziv_biljke_entry.place_forget()
        latinski_naziv.place_forget()
        latinski_naziv_entry.place_forget()
        frame_dodaj_pot2.place_forget()
        opis_frame.place_forget()
        opis_frame.place_forget()
        naslov_dodaj_biljku.place_forget()
        #sakrili smo prijavu i stranicu dodaj biljku

        frame_dodaj_pitar.place_forget()
        id_pitara.place_forget()
        naziv_pitara.place_forget()
        naziv_pitara_entry.place_forget()
        id__pitara_entry.place_forget()
        lokacija.place_forget()
        lokacija_entry.place_forget()
        posadjena_checkbox.place_forget()
        biljka_izbor.place_forget()
        pitar_dropdown.place_forget()
        frame_dodaj_pitar2.place_forget()
        naslov_dodaj_posudu.place_forget()
        show_graphs_button.place_forget()
        canvas_pitara.place_forget()
        frame_pitara.place_forget()
        scrollbar2.place_forget()
        frame2.place_forget()
        canvas_frame_pitara.place_forget()
#        store_button.place_forget()

        naslov_racun.place_forget()
        frame_racun.place_forget()
        name_label.place_forget()
        lastname_label.place_forget()
        username_label.place_forget()
        zipcode_label.place_forget()
        password_label.place_forget()
        city_label.place_forget()
        email_label.place_forget()

        name_entry.place_forget()
        lastname_entry.place_forget()
        username_entry.place_forget()
        password_entry.place_forget()
        city_entry.place_forget()
        email_entry.place_forget()
        button_datareg.place_forget()
        button_editdata.place_forget()

        naslov_prikaz_biljaka.place(x=500, y=15)
        naslov_prikaz_biljaka.lift()
        frame_biljaka.place(x=150, y=150, height=450, width=900)        
        canvas_biljaka.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        frame2.place(x=0, y=0)
        dropdown_menu.place(x=900, y=15)
        time_label.place(x=5, y=20)
        time_label.lift()
        refresh_canvas()
    else:
        messagebox.showerror("Error", "Invalid username or password.")

#user name
recUser=f'User name'
recenicaUser=tk.StringVar()
recenicaUser.set(recUser)
UserName=tk.Label(frame, textvariable=recenicaUser,bg='#BAFFD2', font=('century',12))
UserName.place(x=50,y=70)

user=tk.Entry(frame,width=25, fg='#00b300', border=2, bg='white', font=('century', 12,))
user.place(x=50, y=100)
user.insert(0, 'Input your user name')

#password
recPass=f'Password'
recenicaPass=tk.StringVar()
recenicaPass.set(recPass)
UserPass=tk.Label(frame, textvariable=recenicaPass, bg='#BAFFD2', font=('century',12))
UserPass.place(x=50,y=160)

PassWind = tk.Entry(frame, width=25, show="*", fg='#00b300', border=2, bg='white', font=('century', 12,))
PassWind.place(x=50, y=190)
PassWind.insert(0, 'Input your password')

#botun prijava na prvom prozoru
button_prijava=tk.Button(frame, text='PRIJAVI SE',command=open_biljke, width=32, height=2, border=1, relief='raised', bg='#4BF185')
button_prijava.place(x=50, y=240)

UserNew=tk.Label(frame, text='Novi korisnik?', bg='#BAFFD2', font=('century',11))
UserNew.place(x=50, y=300)
#registracija
button_reg=tk.Button(frame, text='REGISTRIRAJ SE', width=32, height=2, border=1,bg='#4BF185', relief='raised')
button_reg.place(x=50, y=330)

def clear_entry(event, widget, default_text):  #za brisanje teksta prilikom upisivana sifre i imena
    if widget.get() == default_text:
        widget.delete(0, tk.END)
        widget.config(fg='#000000')  # Change the text color to black

user.bind('<FocusIn>', lambda event: clear_entry(event, user, 'Input your user name'))
PassWind.bind('<FocusIn>', lambda event: clear_entry(event, PassWind, 'Input your password'))

frame2 = tk.Frame(root, width=1100, height=85, bg='#4BF180')
#------------------------------------------------BAZA--------------------------------------------------------------

conn= sqlite3.connect('BILJKEappinfo/MyFloraPosuda.db')
cursor = conn.cursor()

#cursor.execute('''DROP TABLE plants''')

cursor.execute('''CREATE TABLE IF NOT EXISTS pots (
                pot_id TEXT,  
                pot_name TEXT, 
                plant_name TEXT, 
                pot_location TEXT, 
                pot_photo TEXT, 
                plant_photo TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS plant_data (
                plant_id TEXT, 
                plant_humidity TEXT,
                plant_pH TEXT,
                plant_salinity TEXT, 
                plant_illumination TEXT,
                plant_room_temp TEXT, 
                timestamp_date TEXT, 
                timestamp_time TEXT)''')


cursor.execute("SELECT * FROM plant_data")
columns2 = cursor.fetchall()
for column in columns2:
          print(column)

cursor.execute('''CREATE TABLE IF NOT EXISTS plants (
                plant_id TEXT, 
                plant_name TEXT, 
                plant_name_lat TEXT,    
                plant_about TEXT,
                plant_photo TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS RandomValues (
                pot_id TEXT,
                humidity INTEGER,
                pH REAL, 
                salinity REAL,
                illumination INTEGER,
                room_temp INTEGER,
                datetime TEXT)''') 

# vrijednosti u brojevima
cursor.execute("SELECT * FROM RandomValues")
columns3 = cursor.fetchall()
for column in columns3:
          print(column)

conn.commit()
cursor.close()

 
#------------------------------------------------RAČUN U APLIKACIJI----------------------------------------------

def racun():
        image_label.place_forget()
        frame.place_forget()
        login.place_forget()
        UserName.place_forget()
        user.place_forget()
        UserPass.place_forget()
        PassWind.place_forget()
        button_prijava.place_forget()
        UserNew.place_forget()
        button_reg.place_forget()
        frame_dodaj_pot1.place_forget()
        naziv_biljke.place_forget()
        naziv_biljke_entry.place_forget()
        latinski_naziv.place_forget()
        latinski_naziv_entry.place_forget()
        frame_dodaj_pot2.place_forget()
        opis_frame.place_forget()
        opis_frame.place_forget()
        naslov_dodaj_biljku.place_forget()
        #sakrili smo prijavu i stranicu dodaj biljku

        frame_dodaj_pitar.place_forget()
        id_pitara.place_forget()
        naziv_pitara.place_forget()
        naziv_pitara_entry.place_forget()
        id__pitara_entry.place_forget()
        lokacija.place_forget()
        lokacija_entry.place_forget()
        posadjena_checkbox.place_forget()
        biljka_izbor.place_forget()
        pitar_dropdown.place_forget()
        frame_dodaj_pitar2.place_forget()
        naslov_dodaj_posudu.place_forget()
        
        show_graphs_button.place_forget()
        canvas_pitara.place_forget()
        frame_pitara.place_forget()
        scrollbar2.place_forget()
        frame2.place_forget()
        canvas_frame_pitara.place_forget()
#        store_button.place_forget() 

        naslov_prikaz_biljaka.place_forget()
        frame_biljaka.place_forget()        
        canvas_biljaka.pack_forget()
        frame2.place(x=0, y=0)
        dropdown_menu.place(x=900, y=15)
        time_label.place(x=5, y=20)
        time_label.lift()

        naslov_racun.place(x=400, y=15)
        frame_racun.place(x=180, y=100)
        name_label.place(x=220, y=120)
        lastname_label.place(x=520, y=120)
        username_label.place(x=220, y=200)
        zipcode_label.place(x=220, y=360)
        password_label.place(x=220, y=280)
        city_label.place(x=520, y=360)
        email_label.place(x=220, y=440)

        name_entry.place(x=220, y=150, width=230, height=32)
        lastname_entry.place(x=520, y=150, width=230, height=32)
        username_entry.place(x=220, y=230, width=530, height=32)
        password_entry.place(x=220, y=310, width=530, height=32)
        city_entry.place(x=520, y=390, width=230, height=32)
        email_entry.place(x=220, y=470, width=530, height=32)
        zipcode_entry.place(x=220, y=390, width=230, height=32)
        button_datareg.place(x=370, y=550, height=32)
        button_editdata.place(x=370, y=590, height=32)


naslov_racun = tk.Label(root, text='MOJ RAČUN', bg='#4BF180', fg='black', font=('century', 20, 'bold'))


# Create a database connection
conn = sqlite3.connect('BILJKEappinfo/MyFloraPosuda.db')
cursor = conn.cursor()

# Create a table to store the data if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS userdata (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT,
                    last_name TEXT,
                    username TEXT,
                    password TEXT,
                    zipcode TEXT,
                    city TEXT,
                    email TEXT
                )''')
conn.commit()

def disable_fields():
    name_entry.config(state='disabled')
    lastname_entry.config(state='disabled')
    username_entry.config(state='disabled')
    password_entry.config(state='disabled')
    zipcode_entry.config(state='disabled')
    city_entry.config(state='disabled')
    email_entry.config(state='disabled')

def enable_fields():
    name_entry.config(state='normal')
    lastname_entry.config(state='normal')
    username_entry.config(state='normal')
    password_entry.config(state='normal')
    zipcode_entry.config(state='normal')
    city_entry.config(state='normal')
    email_entry.config(state='normal')
    zipcode_entry.place(x=220, y=390, width=230, height=32)


def save_changes():
    # Get the values from the entry fields
    first_name = name_entry.get()
    last_name = lastname_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    zipcode = zipcode_entry.get()
    city = city_entry.get()
    email = email_entry.get()

    # Save the values to the database
    cursor.execute('''INSERT INTO userdata
                    (first_name, last_name, username, password, zipcode, city, email)
                    VALUES (?, ?, ?, ?, ?, ?, ?)''',
                    (first_name, last_name, username, password, zipcode, city, email))
    conn.commit()

    # Disable the fields after saving
    disable_fields()

def edit_data():
    enable_fields()
    button_editdata.config(state='disabled')

frame_racun = tk.Frame(root, width=610, height=550, bg='#4BF185')

name_label = tk.Label(root, text='First name', font=('century', 12), bg='#4BF180')

lastname_label = tk.Label(root, text='Last name', font=('century', 12),bg='#4BF180')

username_label = tk.Label(root, text='Username', font=('century', 12),bg='#4BF180')

password_label = tk.Label(root, text='Password', font=('century', 12),bg='#4BF180')

zipcode_label = tk.Label(root, text='Zipcode', font=('century', 12),bg='#4BF180')

city_label = tk.Label(root, text='City', font=('century', 12),bg='#4BF180')

email_label = tk.Label(root, text='Email address', font=('century', 12),bg='#4BF180')

name_entry = tk.Entry(root, font=('century', 12), justify='left')

lastname_entry = tk.Entry(root, font=('century', 12), justify='left')

username_entry = tk.Entry(root, font=('century', 12), justify='left')

password_entry = tk.Entry(root, font=('century', 12), justify='left')

zipcode_entry = tk.Entry(root, font=('century', 12), justify='left')

city_entry = tk.Entry(root, font=('century', 12), justify='left')

email_entry = tk.Entry(root, font=('century', 12), justify='left')


# Load the last entered values from the database, if available
cursor.execute('SELECT * FROM userdata ORDER BY id DESC LIMIT 1')
data = cursor.fetchone()

if data:
    name_entry.insert(0, data[1])
    lastname_entry.insert(0, data[2])
    username_entry.insert(0, data[3])
    password_entry.insert(0, data[4])
    zipcode_entry.insert(0, data[5])
    city_entry.insert(0, data[6])
    email_entry.insert(0, data[7])

button_datareg = tk.Button(root, text='SPREMI PROMJENE', width=32, height=2, border=1, relief='raised', bg='#fbe2aa', command=save_changes)

button_editdata = tk.Button(root, text='UREDI PODATKE', width=32, height=2, border=1, relief='raised', bg='#fbe2aa', command=edit_data)


disable_fields()


#*********************************************PRIKAZ BILJAKA***********************************************************

naslov_prikaz_biljaka=tk.Label(root, text='BILJKE', bg='#4BF180', fg='black', font=('century', 20, 'bold'))

frame_dodaj_pot1 = tk.Frame(root, width=430, height=500, bg='#4BF180')

naziv_biljke=tk.Label(frame_dodaj_pot1, text='NAZIV PITARA', bg='#4BF180', fg='black', font=('century', 11, 'bold'))

naziv_biljke_entry=tk.Entry(frame_dodaj_pot1, width=25, border=1, bg='white', font=('century', 12,))

latinski_naziv=tk.Label(frame_dodaj_pot1, text='LOKACIJA ', bg='#4BF180', fg='black', font=('century', 11, 'bold'))

latinski_naziv_entry=tk.Entry(frame_dodaj_pot1, width=25, border=1, bg='white', font=('century', 12,))

frame_dodaj_pot2 = tk.Frame(root, width=430, height=500, bg='#4BF180')

opis_frame=tk.Label(frame_dodaj_pot2, text='KARAKTERISTIKE', bg='#4BF180', fg='black', font=('century', 11, 'bold'))
opis_frame.place(x=40, y=240)
#za unos opisa biljke
opis_frame=tk.Text(frame_dodaj_pot2, bg='white', fg='black', font=('century', 11))

opis= opis_frame.get("1.0", "end-1c") #za prikaz teksta od 0 indeksa prve linije
#definiranje kako dodati sliku iz naseg fila sa racunala

#-----------------------------------------------------------------------------------------------------
def show_image_added():
    global file_path, resized_image_plant, label_image # Use the global file_path variable
    # Remove the "Dodaj sliku" button
    button_slika.place_forget()
    # Ask user to select an image file
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

# Load the selected image and display it
    image_Plant = Image.open(file_path)  #ZA OTVARANJE JPG TREBA IMAGE OPEN!!!!
    resized_image = image_Plant.resize((210, 210), Image.LANCZOS)
    resized_image_plant=ImageTk.PhotoImage(resized_image)
    label_image = tk.Label(frame_dodaj_pot2, image=resized_image_plant)
    label_image.image = resized_image_plant   #ZA UCITANJE SLIKE U LABEL
    label_image.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
   

image_add = tk.PhotoImage(file='Biljkeappinfo/biljkeplus.png')
button_slika=tk.Button(frame_dodaj_pot2, image=image_add, command=show_image_added, width=210, height=210, border=1, relief='raised', bg='#4BF180')
button_slika.place(relx=0.5, rely=0.25, anchor=tk.CENTER)



#***********************************definirali smo prozore za prikaz biljaka ***************************************
frame_biljaka = tk.Frame(root)
# create a canvas to hold the frame of canvases
canvas_biljaka = tk.Canvas(frame_biljaka, bg='#BAFFD2', highlightthickness=0)
#BAFFD2
# create a scrollbar for the canvas
scrollbar = tk.Scrollbar(frame_biljaka, orient="vertical", command=canvas_biljaka.yview)
# configure the canvas to work with the scrollbar
canvas_biljaka.configure(yscrollcommand=scrollbar.set)

# create a frame to hold the 2x2 canvases
canvas_frame_biljke = tk.Frame(canvas_biljaka, bg='#BAFFD2')
canvas_biljaka.create_window((0, 0), window=canvas_frame_biljke, anchor="nw")

# configure the canvas scroll region to encompass the 2x2 canvases
canvas_frame_biljke.update_idletasks()
canvas_biljaka.configure(scrollregion=canvas_biljaka.bbox("all"))

#---------------------brisanje biljke iz baze i prikaza----------------------------------------
def delete_plant(plant_id):
    conn = sqlite3.connect('BILJKEappinfo/MyFloraPosuda.db')
    cursor = conn.cursor()

    # Execute the SQL query to delete the plant with the given plant_id
    cursor.execute("DELETE FROM plants WHERE plant_id=?", (plant_id,))
    conn.commit()

    # Close the database connection
    cursor.close()
    conn.close()

    # Refresh the UI to reflect the updated plant list

    refresh_canvas()

def refresh_canvas():
    # Clear the existing canvases
    for child in canvas_frame_biljke.winfo_children():
        child.destroy()

    conn = sqlite3.connect('BILJKEappinfo/MyFloraPosuda.db')
    cursor = conn.cursor()
    cursor.execute("SELECT plant_id, plant_name, plant_name_lat, plant_about, plant_photo FROM plants")
    plants = cursor.fetchall()
    print(plants)
#that allows you to iterate over a sequence (such as a list or tuple) while also keeping track of the index of each element
    for i, plant in enumerate(plants):
        add_pot_canvas = tk.Canvas(canvas_frame_biljke, width=360, height=210, bg='#fff5cc')
        add_pot_canvas.grid(row=i // 2, column=i % 2, padx=10, pady=10)

    # Display plant data on the canvas
        plant_single_id = plant[0]
        plant_name = plant[1]
        plant_name_lat = plant[2]
        plant_about = plant[3]
    # Add code to display the plant data on the canvas
        plant_photo_path = plant[4]
        plant_photo = Image.open(plant_photo_path)
        plant_photo = plant_photo.resize((100, 100), resample=Image.LANCZOS)
        plant_photo_resized = ImageTk.PhotoImage(plant_photo)
        plant_photo_label=tk.Label(add_pot_canvas, image=plant_photo_resized)
        plant_photo_label.image=plant_photo_resized
        plant_photo_label.place(x=10, y=10)

        plant_id_written = tk.Label(add_pot_canvas, text=f'ID: {plant_single_id}', font=('century', 10, 'bold'), bg='#fff5cc')
        plant_id_written.place(x=5, y=120)  

        plant_name_written = tk.Label(add_pot_canvas, text=plant_name, font=('century', 12, 'bold'), bg='#fff5cc')
        plant_name_written.place(x=120, y=10)

        plant_name_lat_written = tk.Label(add_pot_canvas, text=f'{plant_name_lat}', font=('Segoe UI', 11, 'bold'), bg='#fff5cc')
        plant_name_lat_written.place(x=120, y=35)

        plant_about_written = tk.Text(add_pot_canvas, font=('century', 10), bd=0, highlightthickness=0, bg='#fff5cc')
        plant_about_written.insert('1.0', plant_about)
        plant_about_written.place(x=120, y=70, width=230, height=130)

        delete_button = tk.Button(add_pot_canvas, text='X', command=lambda id=plant_single_id: delete_plant(id), bg='#fff5cc')
        delete_button.place(x=340, y=10)

#----------------------------PRIKAZ DODATNOG CANVASA---------------------------------------------------------

    last_canvas = tk.Canvas(canvas_frame_biljke, width=360, height=210, bg='#fff5cc')
    last_canvas.grid(row=(len(plants) - 1) // 2, column=(len(plants) - 1) % 2, padx=10, pady=10)
    

    image_last_canvas = Image.open('BILJKEappinfo/biljkeplus.png')
    image_last_canvas = image_last_canvas.resize((220, 220), resample=Image.LANCZOS)
    image_last_canvas = ImageTk.PhotoImage(image_last_canvas)    

    # Add the image button to the last canvas
    image_button = tk.Button(last_canvas, image=image_last_canvas, bd=0, highlightthickness=0, bg='#fff5cc')
    image_button.image = image_last_canvas  # Keep a reference to the image
    image_button.place(x=80, y=10)
    image_button.bind("<Button-1>", lambda event: add_plant())

    # Configure the canvas scroll region to encompass all canvases
    canvas_frame_biljke.update_idletasks()
    canvas_biljaka.configure(scrollregion=canvas_biljaka.bbox("all"))

refresh_canvas()

    
#**********************************ZA DODAT NOVI PITAR************************************************

def add_new_pot():
    
    button_slika.place_forget()
    frame2.place(x=0, y=0)
    image_label.place_forget()
    frame.place_forget()
    login.place_forget()
    frame_dodaj_pot1.place_forget()
    naziv_biljke.place_forget()
    naziv_biljke_entry.place_forget()
    latinski_naziv.place_forget()
    latinski_naziv_entry.place_forget()
    frame_dodaj_pot2.place_forget()
    opis_frame.place_forget()
    opis_frame.place_forget()
    naslov_dodaj_biljku.place_forget()
    #sakrili smo prijavu i stranicu dodaj biljku
    naslov_prikaz_biljaka.place_forget()
    frame_biljaka.place_forget()        
    canvas_biljaka.pack_forget()
    scrollbar.pack_forget()

    canvas_pitara.place_forget()
    frame_pitara.place_forget()
    scrollbar2.place_forget()
    canvas_frame_pitara.place_forget()
    
    naslov_racun.place_forget()
    frame_racun.place_forget()
    name_label.place_forget()
    lastname_label.place_forget()
    username_label.place_forget()
    zipcode_label.place_forget()
    password_label.place_forget()
    city_label.place_forget()
    email_label.place_forget()

    name_entry.place_forget()
    lastname_entry.place_forget()
    username_entry.place_forget()
    password_entry.place_forget()
    city_entry.place_forget()
    email_entry.place_forget()
    button_datareg.place_forget()
    button_editdata.place_forget()
    
    show_graphs_button.place_forget()

    frame_dodaj_pitar.place(x=570, y=120)
    id_pitara.place(x=10, y=20)
    id__pitara_entry.place(x=180, y=25)
    naziv_pitara.place(x=10, y=80)
    naziv_pitara_entry.place(x=180, y=80, height=28)
    lokacija.place(x=10, y=140)
    lokacija_entry.place(x=180, y=140, height=28)
    posadjena_checkbox.place(x=10, y=210)
    biljka_izbor.place(x=10, y=260)
    pitar_dropdown.place(x=180, y=260, height=28)
    frame_dodaj_pitar2.place(x=90, y=120)
    naslov_dodaj_posudu.place(x=450, y=15)
    naslov_dodaj_posudu.lift()
    dropdown_menu.place(x=900, y=15)
    time_label.place(x=5, y=20)
    time_label.lift()
#-----------------------------------------------------------------------------------------------------
# spoji se na bazu
conn = sqlite3.connect('BILJKEappinfo/MyFloraPosuda.db')
cursor = conn.cursor()

# dohvati zadnji ID i dodajemo ga kao fiksni id za pitar
cursor.execute("SELECT MAX(pot_id) FROM pots")
last_pot_id = cursor.fetchone()[0]
if last_pot_id is None:
    last_pot_id = 0
else:
    last_pot_id = int(last_pot_id.split('-')[0]) 
# method will split the string at the '-' character and return a list of substrings:npr. ['005', 'plant'].
print(last_pot_id)
pot_id = '{:03d}-pot'.format(last_pot_id + 1)

naslov_dodaj_posudu = tk.Label(root, text='DODAJ POSUDU', bg='#4BF180', fg='black', font=('century', 20, 'bold'))

frame_dodaj_pitar = tk.Frame(root, width=430, height=500, bg='#4BF180')

id_pitara = tk.Label(frame_dodaj_pitar, text='ID PITARA', bg='#4BF180', fg='black', font=('century', 11, 'bold'))
id__pitara_entry = tk.Entry(frame_dodaj_pitar, disabledbackground='white', disabledforeground='grey', font=('century', 11, 'bold'))
# Convert last_pot_id + 1 to a string before concatenation
id__pitara_entry.insert(0, pot_id)

id__pitara_entry.config(state='disabled', width=25)

naziv_pitara_entry=tk.Entry(frame_dodaj_pitar, width=25, border=1, bg='white', font=('century', 12,))

naziv_pitara=tk.Label(frame_dodaj_pitar, text='NAZIV PITARA', bg='#4BF180', fg='black', font=('century', 11, 'bold'))

naziv_pitara_entry=tk.Entry(frame_dodaj_pitar, width=25, border=1, bg='white', font=('century', 12,))

lokacija=tk.Label(frame_dodaj_pitar, text='LOKACIJA', bg='#4BF180', fg='black', font=('century', 11, 'bold'))

lokacija_entry=tk.Entry(frame_dodaj_pitar, width=25, border=1, bg='white', font=('century', 12,))

posadjena_var = tk.BooleanVar()
posadjena_checkbox = tk.Checkbutton(frame_dodaj_pitar, text='POSAĐENA BILJKA', bg='#4BF180', fg='black',
                                    font=('century', 11, 'bold'), variable=posadjena_var)


#---------------------------------------------  IZBORNIK BILJKE-------------------------------------------

frame_dodaj_pitar2 = tk.Frame(root, width=430, height=500, bg='#4BF180')
conn = sqlite3.connect('BILJKEappinfo/MyFloraPosuda.db')
cursor = conn.cursor()

# Retrieve plant names from the database
cursor.execute("SELECT plant_name FROM plants")
plants = [''] + [row[0] for row in cursor.fetchall()]

# Variable to store the selected plant name
selected_plant = tk.StringVar()

biljka_izbor = tk.Label(frame_dodaj_pitar, text='BILJKA U POSUDI', bg='#4BF180', fg='black', font=('century', 11, 'bold'))

def get_selected_plant():
    plant_name = selected_plant.get()  # Get the selected plant name from the dropdown
    conn.commit()
    return plant_name 

# Dropdown for plant names
pitar_dropdown = tk.OptionMenu(frame_dodaj_pitar, selected_plant, *plants,)
pitar_dropdown.config(width=20, font=('century', 12))
pitar_dropdown
#dohvacanje cvijeta iz izbora


#----------------------------------------------------------------------------------------------------------------

def window_pots():
        image_label.place_forget()
        frame.place_forget()
        login.place_forget()
        UserName.place_forget()
        user.place_forget()
        UserPass.place_forget()
        PassWind.place_forget()
        button_prijava.place_forget()
        UserNew.place_forget()
        button_reg.place_forget()
        frame_dodaj_pot1.place_forget()
        naziv_biljke.place_forget()
        naziv_biljke_entry.place_forget()
        latinski_naziv.place_forget()
        latinski_naziv_entry.place_forget()
        frame_dodaj_pot2.place_forget()
        opis_frame.place_forget()
        opis_frame.place_forget()
        naslov_dodaj_biljku.place_forget()
        #sakrili smo prijavu i stranicu dodaj biljku

        frame_dodaj_pitar.place_forget()
        id_pitara.place_forget()
        id__pitara_entry.place_forget()
        naziv_pitara.place_forget()
        naziv_pitara_entry.place_forget()
        lokacija.place_forget()
        lokacija_entry.place_forget()
        posadjena_checkbox.place_forget()
        biljka_izbor.place_forget()
        pitar_dropdown.place_forget()
        frame_dodaj_pitar2.place_forget()
        button_slika.place_forget()

        naslov_prikaz_biljaka.place_forget()
        naslov_prikaz_biljaka.lift()

        naslov_racun.place_forget()
        frame_racun.place_forget()
        name_label.place_forget()
        lastname_label.place_forget()
        username_label.place_forget()
        zipcode_label.place_forget()
        password_label.place_forget()
        city_label.place_forget()
        email_label.place_forget()

        name_entry.place_forget()
        lastname_entry.place_forget()
        username_entry.place_forget()
        password_entry.place_forget()
        city_entry.place_forget()
        email_entry.place_forget()
        button_datareg.place_forget()
        button_editdata.place_forget()
        naslov_dodaj_posudu.place(x=400, y=20)
        frame_pitara.place(x=150, y=150, height=450, width=900)        
        canvas_pitara.pack(side="left", fill="both", expand=True)
        scrollbar2.pack(side="right", fill="y")
        frame2.place(x=0, y=0)
        show_graphs_button.place(x=950, y=110)

        dropdown_menu.place(x=900, y=15)
        time_label.place(x=5, y=20)
        time_label.lift()



frame_pitara = tk.Frame(root)
# create a canvas to hold the frame of canvases
canvas_pitara = tk.Canvas(frame_pitara, bg='#BAFFD2', highlightthickness=0)
#BAFFD2
# create a scrollbar for the canvas
scrollbar2 = tk.Scrollbar(frame_pitara, orient="vertical", command=canvas_pitara.yview)
# configure the canvas to work with the scrollbar
canvas_pitara.configure(yscrollcommand=scrollbar2.set)

# create a frame to hold the 2x2 canvases
canvas_frame_pitara = tk.Frame(canvas_pitara, bg='#BAFFD2')
canvas_pitara.create_window((0, 0), window=canvas_frame_pitara, anchor="nw")

# configure the canvas scroll region to encompass the 2x2 canvases
canvas_frame_pitara.update_idletasks()

canvas_pitara.configure(scrollregion=canvas_pitara.bbox("all"))


#---------------------------------BRISANJE PITARA/POTA---------------------------------------------------------------------------------
def delete_pot(pot_id):
    conn = sqlite3.connect('BILJKEappinfo/MyFloraPosuda.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM pots WHERE pot_id=?", (pot_id,))
    conn.commit()

    # Close the database connection
    cursor.close()
    conn.close()

    # Refresh the UI to reflect the updated plant list
    refresh_canvas_of_pots()

#--------------------------------------------------------------------------Prikaz pitara----------------------------------------
    
def refresh_canvas_of_pots():
    for child in canvas_frame_pitara.winfo_children():
        child.destroy()

    conn = sqlite3.connect('BILJKEappinfo/MyFloraPosuda.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pots")
    pots = cursor.fetchall()

    cursor.execute("SELECT plant_humidity, plant_pH, plant_salinity, plant_illumination, plant_room_temp FROM plant_data")
    saved_values = cursor.fetchone()

    for i, pot in enumerate(pots):
        add_pot_canvas = tk.Canvas(canvas_frame_pitara, width=360, height=210, bg='#fff5cc')
        add_pot_canvas.grid(row=i // 2, column=i % 2, padx=10, pady=10)

        pot_id = pot[0]
        pot_name = pot[1]
        plant_name= pot[2]
        pot_location = pot[3]
    # Add code to display the plant data on the canvas
        pot_photo_path = pot[4]
        pot_photo = Image.open(pot_photo_path)
        pot_photo = pot_photo.resize((120, 120), resample=Image.LANCZOS)
        pot_photo_show = ImageTk.PhotoImage(pot_photo)
        pot_photo_label=tk.Label(add_pot_canvas, image=pot_photo_show)
        pot_photo_label.image=pot_photo_show
        pot_photo_label.place(x=10, y=10)

        pot_id_written = tk.Label(add_pot_canvas, text=f'ID: {pot_id}', font=('century', 10, 'bold'), bg='#fff5cc')
        pot_id_written.place(x=5, y=140)  

        pot_name_written = tk.Label(add_pot_canvas, text=f'{pot_name}', font=('century', 12, 'bold'), bg='#fff5cc')
        pot_name_written.place(x=140, y=5)

        if pot[2]=='':
            plant_name_written = tk.Label(add_pot_canvas, text=f'Nije posađeno', font=('century', 12, 'bold'), bg='#fff5cc', fg='#62B265')
            plant_name_written.place(x=140, y=30)
            message_pot_written=tk.Label(add_pot_canvas, text=f'Nema očitavanja', font=('century', 12), bg='#fff5cc', fg='black')
            message_pot_written.place(x=180, y=150)
        else:
            plant_name_written = tk.Label(add_pot_canvas, text=f'Posađeno: {plant_name}', font=('century', 10), bg='#fff5cc', fg='#AC4913')
            plant_name_written.place(x=140, y=30)
            if saved_values:
                saved_pot_humidity, saved_pot_pH, saved_pot_salinity, saved_pot_illumination, saved_pot_room_temp = saved_values

                saved_pot_humidity = int(saved_pot_humidity)
                saved_pot_pH = float(saved_pot_pH)
                saved_pot_salinity = float(saved_pot_salinity)
                saved_pot_illumination = int(saved_pot_illumination)
                saved_pot_room_temp = int(saved_pot_room_temp)

        # Calculate the acceptable range of values
                humidity_range = (0.8 * saved_pot_humidity, 1.2 * saved_pot_humidity)
                pH_range = (0.8 * saved_pot_pH, 1.2 * saved_pot_pH)
                salinity_range = (0.8 * saved_pot_salinity, 1.2 * saved_pot_salinity)
                illumination_range = (0.8 * saved_pot_illumination, 1.2 * saved_pot_illumination)
                room_temp_range = (0.8 * saved_pot_room_temp, 1.2 * saved_pot_room_temp)

        # Generate random measurements
                pot_humidity_measurement = random.randint(30, 90)
                pot_pH_measurement = round(random.uniform(2, 12), 2)
                pot_salinity_measurement = round(random.uniform(0.8, 2.5), 2)
                pot_illumination_measurement = random.randint(0, 18000)
                pot_room_temp_measurement = random.randint(0, 39)

        # Compare the random data with the saved values and assign labels
                pot_humidity_label = "green" if humidity_range[0] <= pot_humidity_measurement <= humidity_range[1] else "red"
                pot_pH_label = "green" if pH_range[0] <= pot_pH_measurement <= pH_range[1] else "red"
                pot_salinity_label = "green" if salinity_range[0] <= pot_salinity_measurement <= salinity_range[1] else "red"
                pot_illumination_label = "green" if illumination_range[0] <= pot_illumination_measurement <= illumination_range[1] else "red"
                pot_room_temp_label = "green" if room_temp_range[0] <= pot_room_temp_measurement <= room_temp_range[1] else "red"

        # Get the current date and time
                current_datetime = datetime.now()
        # Save the random values to the "RandomValues" database
                cursor.execute("INSERT INTO RandomValues (pot_id, humidity, pH, salinity, illumination, room_temp, datetime) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (pot_id, pot_humidity_measurement, pot_pH_measurement, pot_salinity_measurement, pot_illumination_measurement, pot_room_temp_measurement, current_datetime))
                conn.commit()

        # Update the labels with the new random values
                humidity_label = tk.Label(add_pot_canvas, font=('century', 11), bg='#fff5cc', fg='black')
                pH_label = tk.Label(add_pot_canvas, font=('century', 11), bg='#fff5cc', fg='black')
                salinity_label = tk.Label(add_pot_canvas, font=('century', 11), bg='#fff5cc', fg='black')
                illumination_label = tk.Label(add_pot_canvas, font=('century', 11), bg='#fff5cc', fg='black')
                room_temp_label = tk.Label(add_pot_canvas,font=('century', 11), bg='#fff5cc', fg='black') 

                humidity_label.config(text=f"Vlažnost: {pot_humidity_measurement} %", fg=pot_humidity_label)
                pH_label.config(text=f"PH: {pot_pH_measurement}", fg=pot_pH_label)
                salinity_label.config(text=f"Salinitet: {pot_salinity_measurement} mS/cm", fg=pot_salinity_label)
                illumination_label.config(text=f"Osvjetljenje: {pot_illumination_measurement} lux", fg=pot_illumination_label)
                room_temp_label.config(text=f"Temperatura: {pot_room_temp_measurement} C", fg=pot_room_temp_label)
               
               
        # Position the labels
                humidity_label.place(x=150, y=100)
                pH_label.place(x=150, y=120)
                salinity_label.place(x=150, y=140)
                illumination_label.place(x=150, y=160)
                room_temp_label.place(x=150, y=180)
            else:
                messagebox.showinfo("Error", "No saved values found in the database")
  

        pot_location_written = tk.Label(add_pot_canvas, text=f'Lokacija: {pot_location}', font=('century', 11), bg='#fff5cc', fg='black')
        pot_location_written.place(x=140, y=60)
      
        stars_written = tk.Label(add_pot_canvas, text=f'* * * * * * * * * * * * * * * * * * * * * ', font=('century', 9), bg='#fff5cc', fg='black')
        stars_written.place(x=140, y=80)

        if pot[5] is not None:
            plant_photo_show=pot[5]
            plant_photo= Image.open(plant_photo_show)
            plant_photo = plant_photo.resize((70, 70), resample=Image.LANCZOS)
            plant_photo_garden = ImageTk.PhotoImage(plant_photo)
            plant_photo_label=tk.Label(add_pot_canvas, image=plant_photo_garden)
            plant_photo_label.image=plant_photo_garden
            plant_photo_label.place(x=10, y=10)

        delete_button_pot=tk.Button(add_pot_canvas, text='X', command=lambda id=pot_id:delete_pot(id), bg='#fff5cc')
        delete_button_pot.place(x=340, y=10)

        last_canvas_pot = tk.Canvas(canvas_frame_pitara, width=360, height=210, bg='#fff5cc')
        last_canvas_pot.grid(row=(len(pots) - 1) // 2, column=(len(pots) - 1) % 2, padx=10, pady=10)
    

        image_last_canvas_pot = Image.open('BILJKEappinfo/DodajPitar.png')
        image_last_canvas_pot = image_last_canvas_pot.resize((220, 220), resample=Image.LANCZOS)
        image_last_canvas_pitar = ImageTk.PhotoImage(image_last_canvas_pot)    

# Add the image button to the last canvas
        image_button = tk.Button(last_canvas_pot, image=image_last_canvas_pitar, bd=0, highlightthickness=0, bg='#fff5cc')
        image_button.image = image_last_canvas_pitar  # Keep a reference to the image
        image_button.place(x=80, y=10)
        image_button.bind("<Button-1>", lambda event: add_new_pot())

    # Configure the canvas scroll region to encompass all canvases
        canvas_frame_pitara.update_idletasks()
        canvas_pitara.configure(scrollregion=canvas_pitara.bbox("all"))

refresh_canvas_of_pots()

#---------------------------------------------------GRAFOVI---------------------------------------------------------------------

# Function to handle button click event
def button_clicked():
    # Fetch the pot IDs from the database
    conn = sqlite3.connect('RandomValues.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT pot_id FROM RandomValues")
    pot_ids = [row[0] for row in cursor.fetchall()]

#It retrieves all the rows from the database cursor as a list of tuples. Each tuple represents a row in the result set.
# list comprehension that iterates over each row in the result set. For each row, it selects the first element (row[0]), 
# which corresponds to the pot ID, and creates a new list containing only the pot IDs.

    # Create a new window for the graphs
    graph_window = tk.Toplevel(root)
    graph_window.title('Pot Measurements Graphs')
    #A Toplevel widget is used to create a window on top of all other windows

    # Create and display the graphs for each pot ID
    for pot_id in pot_ids:
        # Fetch the values from the database for the pot ID
        cursor.execute("SELECT datetime, humidity, pH, salinity, illumination, room_temp FROM RandomValues WHERE pot_id = ?",
                       (pot_id,))
        results = cursor.fetchall()

        # Extract the datetime and measurement values
        datetimes = []
        humidity_values = []
        pH_values = []
        salinity_values = []
        illumination_values = []
        room_temp_values = []

        for row in results:
            datetimes.append(datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S'))
            humidity_values.append(row[1])
            pH_values.append(row[2])
            salinity_values.append(row[3])
            illumination_values.append(row[4])
            room_temp_values.append(row[5])

        # Create the line graph
        fig, ax = plt.subplots()
        ax.plot(datetimes, humidity_values, label='Humidity')
        ax.plot(datetimes, pH_values, label='pH')
        ax.plot(datetimes, salinity_values, label='Salinity')
        ax.plot(datetimes, illumination_values, label='Illumination')
        ax.plot(datetimes, room_temp_values, label='Room Temperature')
        ax.set_xlabel('Date and Time')
        ax.set_ylabel('Measurement')
        ax.set_title(f'Pot {pot_id} Measurements Over Time')
        ax.legend()

        # Create a canvas for the graph
        graph_canvas = FigureCanvasTkAgg(fig, master=graph_window)
        graph_canvas.draw()
        graph_canvas.get_tk_widget().pack()

    # Function to close the graph window
    def close_window():
        graph_window.destroy()

    # Button to close the graph window
    close_button = tk.Button(graph_window, text='Close', command=close_window)
    close_button.pack()

# Create a button to show the graphs
show_graphs_button = tk.Button(root, text="GRAFOVI", bg='#fff5cc', command=button_clicked)



#***********************************************UNOS PITARA U BAZI**************************************************************

def show_image_pot_added():
    global file_path_pot, resized_image_pot, label_image_pot # Use the global file_path variable
    # Ask user to select an image file-
    file_path_pot = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

# Load the selected image and display it
    image_Pot = Image.open(file_path_pot)  #ZA OTVARANJE JPG TREBA IMAGE OPEN!!!!
    resized_image_pot = image_Pot.resize((210, 210), Image.LANCZOS)
    resized_image_pot=ImageTk.PhotoImage(resized_image_pot)
    label_image_pot = tk.Label(frame_dodaj_pitar2, image=resized_image_pot)
    label_image_pot.image = resized_image_pot   #ZA UCITANJE SLIKE U LABEL
    label_image_pot.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

def insert_new_pot(): #unesi novi pitar i njezine podatke u bazu
    global file_path_pot
    conn= sqlite3.connect('BILJKEappinfo/MyFloraPosuda.db')
    cursor= conn.cursor()
    
    plant_name = get_selected_plant() #plant name ovdje ubacili
#dohvacamo sliku po izabranom cvijetu
    cursor.execute("SELECT plant_photo FROM plants WHERE plant_name= ?", (plant_name,))
    photo_data=cursor.fetchone()
    conn.execute('''INSERT INTO pots (pot_id, pot_name,plant_name, pot_location, pot_photo, plant_photo)
                VALUES (?,?,?,?,?,?)''', (id__pitara_entry.get(), naziv_pitara_entry.get(), plant_name, lokacija_entry.get(), file_path_pot ,photo_data[0] if photo_data else None))
    
    message_pot=tk.Label(frame_dodaj_pot1, bg='#4BF180', fg='black', font=('century', 12))
    message_pot.config(text=f'Novi pitar {naziv_pitara_entry.get()} je dodan u bazu. :)')
    message_pot.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

#The .get() method is used to retrieve the current value entered by the user in the entry widget
    cursor.execute("SELECT * FROM pots")
    columns2 = cursor.fetchall()
    for column in columns2:
          print(column)

    naziv_pitara_entry.delete(0, tk.END)
    lokacija_entry.delete(0, tk.END)
 
 #the photo-related variables file_path_pot and resized_image_pot are reset
 #the image label (label_image_pot) is removed from the window using place_forget()
# Reset the photo variables
    file_path_pot = " "
    resized_image_pot = None
    label_image_pot.place_forget()
    plant_name=' '
    conn.commit()  # commit the changes to the database
    conn.close()   #close the connection



#BOTUNI I NAREDBE----------------------         
image_pot_add_with_showel = tk.PhotoImage(file='BILJKEappinfo/DodajPitar.png')
button_slika_pot_with_showel=tk.Button(frame_dodaj_pitar2, image=image_pot_add_with_showel, command=show_image_pot_added, width=210, height=210, border=1, relief='raised', bg='#4BF180')
button_slika_pot_with_showel.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

button_dodaj_pitar=tk.Button(frame_dodaj_pitar, text='DODAJ PITAR',command=insert_new_pot, width=30, height=2, border=1, relief='raised', bg='#fbe2aa')
button_dodaj_pitar.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

button_natrag_pitar=tk.Button(frame_dodaj_pitar, text='NATRAG', command=open_biljke, width=30, height=2, border=1,bg='#fbe2aa', relief='raised')
button_natrag_pitar.place(relx=0.5, rely=0.9, anchor=tk.CENTER) 


#-----------------------------------------------------ZA DODAT NOVU BILJKU-------------------------------------------------------


def add_plant():
    frame_dodaj_pot1.place(x=570, y=120)
    naziv_biljke.place(x=10, y=100)
    naziv_biljke_entry.place(x=180, y=100, height=28)
    latinski_naziv.place(x=10, y=180)
    latinski_naziv_entry.place(x=180, y=180, height=28)
    frame_dodaj_pot2.place(x=90, y=120)
    naslov_dodaj_biljku.place(x=450, y=15)
    naslov_dodaj_biljku.lift()
    opis_frame.place(x=40, y=270,width=340, height=200)
    button_slika.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    naslov_dodaj_posudu.place_forget()

    frame_biljaka.place_forget()        
    canvas_biljaka.pack_forget()
    scrollbar.pack_forget()
    naslov_prikaz_biljaka.place_forget()
    

naslov_dodaj_biljku=tk.Label(root, text='DODAJ BILJKU', bg='#4BF180', fg='black', font=('century', 20, 'bold'))

frame_dodaj_pot1 = tk.Frame(root, width=430, height=500, bg='#4BF180')

naziv_biljke=tk.Label(frame_dodaj_pot1, text='NAZIV BILJKE', bg='#4BF180', fg='black', font=('century', 11, 'bold'))

naziv_biljke_entry=tk.Entry(frame_dodaj_pot1, width=25, border=1, bg='white', font=('century', 12,))

latinski_naziv=tk.Label(frame_dodaj_pot1, text='LATINSKI NAZIV', bg='#4BF180', fg='black', font=('century', 11, 'bold'))

latinski_naziv_entry=tk.Entry(frame_dodaj_pot1, width=25, border=1, bg='white', font=('century', 12,))

frame_dodaj_pot2 = tk.Frame(root, width=430, height=500, bg='#4BF180')

opis_frame=tk.Label(frame_dodaj_pot2, text='KARAKTERISTIKE', bg='#4BF180', fg='black', font=('century', 11, 'bold'))
opis_frame.place(x=40, y=240)
#za unos opisa biljke
opis_frame=tk.Text(frame_dodaj_pot2, bg='white', fg='black', font=('century', 11))

opis= opis_frame.get("1.0", "end-1c") #za prikaz teksta od 0 indeksa prve linije
#definiranje kako dodati sliku iz naseg fila sa racunala

#--------------------------------------------------------------------------------------------------------------------------
#ZA ODABIR SLIKE PITARA
def show_image_added():
    global file_path, resized_image_plant, label_image # Use the global file_path variable
    # Remove the "Dodaj sliku" button
    # Ask user to select an image file
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

# Load the selected image and display it
    image_Plant = Image.open(file_path)  #ZA OTVARANJE JPG TREBA IMAGE OPEN!!!!
    resized_image = image_Plant.resize((210, 210), Image.LANCZOS)
    resized_image_plant=ImageTk.PhotoImage(resized_image)
    label_image = tk.Label(frame_dodaj_pot2, image=resized_image_plant)
    label_image.image = resized_image_plant   #ZA UCITANJE SLIKE U LABEL
    label_image.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
   

image_add = tk.PhotoImage(file='Biljkeappinfo/biljkeplus.png')
button_slika=tk.Button(frame_dodaj_pot2, image=image_add, command=show_image_added, width=210, height=210, border=1, relief='raised', bg='#4BF180')

#***************************** nesi novu biljku i njezine podatke u bazu************************************************

def insert_new_plant(): 
    global plant_id, file_path, resized_image_plant
    conn= sqlite3.connect('BILJKEappinfo/MyFloraPosuda.db')
    cursor= conn.cursor()

    cursor.execute("SELECT MAX(plant_id) FROM plants")
    last_plant_id = cursor.fetchone()[0]
    if last_plant_id is None:
        last_plant_id = 0
    else:
        last_plant_id = int(last_plant_id.split('-')[0]) 
# method will split the string at the '-' character and return a list of substrings:npr. ['005', 'plant'].

    plant_id = '{:03d}-plant'.format(last_plant_id + 1)
    
    # :03d "format the number as an integer with a minimum width of 3 digits, padded with leading zeros.
    # For example, if last_plant_id is 7, the result will be '008-plant'.

    conn.execute('''INSERT INTO plants (plant_id, plant_name, plant_name_lat, plant_about, plant_photo)
                 VALUES (?, ?, ?, ?, ?)''', 
                 (plant_id, naziv_biljke_entry.get(), latinski_naziv_entry.get(), opis_frame.get('1.0', 'end-1c'), file_path))
    
    
    
    message_label=tk.Label(frame_dodaj_pot1, bg='#4BF180', fg='black', font=('century', 12))
    message_label.config(text=f'Nova biljka {naziv_biljke_entry.get()} je dodana u bazu. :)')
    message_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
          
    plant_humidity = random.randint(30, 90)
    plant_pH = random.uniform(2, 12)
    plant_salinity = random.uniform(0.8, 2.5)
    plant_illumination = random.randint(0, 18000)
    plant_room_temp = random.randint(0, 39)

    conn.execute("INSERT INTO plant_data (plant_id, plant_humidity, plant_pH, plant_salinity, plant_illumination, plant_room_temp) VALUES (?, ?, ?, ?, ?, ?)",
               (plant_id, plant_humidity, plant_pH, plant_salinity, plant_illumination, plant_room_temp))
    
    cursor.execute("SELECT * FROM plant_data")
    columns2 = cursor.fetchall()
    for column in columns2:
          print(column)
    
    naziv_biljke_entry.delete(0,END)
    latinski_naziv_entry.delete(0,END)
    opis_frame.delete('1.0', 'end')  # Delete all text in the Text widget
    file_path = " "

    label_image.place_forget()
    conn.commit()  # commit the changes to the database

    conn.close()   #close the connection
        

button_dodaj_biljku=tk.Button(frame_dodaj_pot1, text='DODAJ BILJKU', command=insert_new_plant, width=30, height=2, border=1, relief='raised', bg='#fbe2aa')
button_dodaj_biljku.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

button_natrag=tk.Button(frame_dodaj_pot1, text='NATRAG', command=open_biljke, width=30, height=2, border=1,bg='#fbe2aa', relief='raised')
button_natrag.place(relx=0.5, rely=0.8, anchor=tk.CENTER) 
# za botun natrag kako da se otvori prozor sa samo slikama biljaka    

#------------------------------------------------izbornik---------------------------------------------------------
#pdajuci izbornik
choices = ["IZBORNIK","RAČUN","POSUDE", "NOVA POSUDA","BILJKE", "NOVA BILJKA", "ODJAVA"]
selected_choices = tk.StringVar(value=choices[0])

dropdown_menu = tk.OptionMenu(root, selected_choices, *choices)
dropdown_menu.configure(width=10, height=1,bg="#4BF185", fg="black",font=("century", 11))


def handle_odjava():
    confirmation_window = tk.Toplevel(root)
    confirmation_window.title("Confirmation")
    confirmation_window.configure(bg="#fbe2aa")

   # Calculate the center coordinates of the root window
    root.update_idletasks()  # Update the root window's geometry information
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    root_x = root.winfo_rootx()
    root_y = root.winfo_rooty()
    window_width = 300
    window_height = 150
    x = root_x + (root_width // 2) - (window_width // 2)
    y = root_y + (root_height // 2) - (window_height // 2)
    confirmation_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    message_label = tk.Label(confirmation_window, text="Sigurno se želite odjaviti?", font=("century", 12), bg="#fbe2aa", fg="black")
    message_label.pack(padx=20, pady=20)
    
    confirm_button = tk.Button(confirmation_window, text="Da", font=("century", 12), bg="#4BF185", fg="black", command=root.destroy)
    confirm_button.pack(side="left", padx=10, pady=10)
    
    cancel_button = tk.Button(confirmation_window, text="Ne", font=("century", 12), bg="#4BF185", fg="black", command=confirmation_window.destroy)
    cancel_button.pack(side="left", padx=10, pady=10)

main_menu = tk.Menu(dropdown_menu, tearoff=0)
main_menu.add_command(label="RAČUN", command=racun)
main_menu.add_command(label="POSUDE", command=window_pots)
main_menu.add_command(label="NOVA POSUDA", command=add_new_pot)
main_menu.add_command(label="BILJKE", command=open_biljke)
main_menu.add_command(label="NOVA BILJKA", command=add_plant)
main_menu.add_command(label="ODJAVA", command=handle_odjava)

main_menu.configure(bg="#4BF185", fg="black",font=("century", 12))       
dropdown_menu["menu"] = main_menu

root.mainloop()




plants = [ 
    {   "id" : "005-plant",
        "name" : "MONSTERA",
        "name_lat" : "Monstera Deliciosa",
        "about" : "Monstera je biljka penjačica koja uspijeva u toplim i vlažnim područjima, osobito u kišnim šumama Srednje i Južne Amerike gdje može narasti i do deset metara u visinu, a za potporu koristi okolna stabla uz koja se penje.\
        Osobito je korisna u zimskim mjesecima kad se prostori griju, jer donosi potrebnu vlažnosti isušenom zraku. Prepoznatljiva je po oblikovanim listovima te nije zahtjevna za održavanje.U posljednje vrijeme ova je zanimljiva biljka raskošnih,\
        rascjepljenih listova postala veliki hit u uređenju interijera, a uklapa se u svaki prostor.",
        "photo" : '005-plant.jpg'  
    },
    {   
        "id" : "006-plant",
        "name" : "ZANZIBAR GEM",
        "name_lat" : "Zamioculcas Zamiifolia",
        "about" : "Sukulentna biljka porijeklom iz Afrike. Pravi hit postala je krajem dvadesetog stoljeća, zahvaljujući nizozemskim uzgajivačima biljaka, koji su je počeli masovno prodavati. Istovremeno liči na paprat i na sukulent, i zbog\
        interesantnog izgleda i lakog održavanja često se koristi za uređenje prostora. Ime je dobila zbog sličnosti s rodom Zamia i jedina je vrsta u svome rodu. Radi se o biljci visine oko metar, koja tvori više izdanaka u obljiku stabljika na kojima\
        se nalaze parovi sjajnih, glatkih i čvrstih zelenih listova. Biljka cvjeta u razdoblju od sredine ljeta do rane jeseni neobičnim cvijetom, a koji se nalazi pri dnu stabljika. Zamioculcas zamiifolia je biljka koja može izazvati trovanje ako\
        dođe do gutanja nekog dijela biljke!",
        "photo" : '006-plant.jpg'  

    },
    {   "id" : "007-plant",
        "name" : "TULIPAN",
        "name_lat" : "Tulipa",
        "about" : "Delikatni cvijet tulipana koji simbolizira savršenstvo ljubavi dolazi u nekoliko boja.Delikatni cvijet tulipana koji simbolizira savršenstvo ljubavi dolazi u nekoliko boja. Zeljasta je trajna biljka iz porodice ljiljana.\
        Lukovice su jajolike i debele, a stabljika je uspravna i visoka do 30 cm. Listovi su duguljasti, ravni do blago zašiljeni. Cvjetovi uspravni, različite boje i bez mirisa. menke. Porijeklom je iz Male Azije a u Europu je unešen iz Otomanskog \
        Carstva kao dar turskog sultana. Uzgaja se isključivo kao ukrasna biljka.",
        "photo" : '007-plant.jpg'  
    },
    {   "id" : "008-plant",
        "name" : "JASMINOVA RUŽA",
        "name_lat" : "Cape jasmine",
        "about" : "Cijenjena ukrasna biljka. Krasnih cvjetova, očaravajućeg mirisa, te jedinstvenosti, omiljen je izazov za uzgajivače. Zahtjevne su za uzgoj u uobičajenim uvjetima zatvorenog prostora. Širokih, sjajnih zelenih listova i lijepih,\
        nježnih bijelih cvjetova. Porijeklom iz Azije. U svojem prirodnom ekosustavu, gardenija je zimzelen grm ili manje drvo. Zahtjeva dosta svjetlosti, ali ne i direktnu svjetlost koju je ljeti potrebno izbjegavati. ",
        "photo" : '008-plant.jpg'  
    },
{        "id" : "009-plant",
        "name" : "RUŽA",
        "name_lat" : "Rosa",
        "about" : "Najpoznatija je i najomiljenija ukrasna biljka na svijetu pa je zbog toga i prozvana kraljicom cvijeća. Razlog velike popularnosti ruža su raskoš boja i mirisa te velika mogućnost kombiniranja visina i oblika u vrtu.\
        Ruža ima drvenastu stabljiku prekrivenu gustim ili rijetkim trnjem koje može biti zavinuto ili ravno. Postoji veliki broj divljih ruža, čiji se plod (šipak, šipurak) bogat vitaminom C koristi u ishrani i za pripremu čajeva. ",
        "photo" : '009-plant.jpg'  
    },
    {   "id" : "010-plant",
        "name" : "KAKTUS",
        "name_lat" : "Cactaceae",
        "about" : "Autohtona je biljka u sjevernoj i južnoj Americi, a u Meksiku se nalazi najveći broj i najviše vrsta. Iako se ovaj sukulent nalazi u tropskim i suptropskim područjima većina ih živi na suhim područjima pa se tako u Americi\
        nerijetko može vidjeti na području između Arizone i Kalifornije, točnije u pustinji Sonora.Stabljika kaktusa može biti rebrasta i naborana, a rebra mogu biti okomita, vodoravna ili lagano zakrivljena. Bodlje koje prekrivaju stabljiku mogu biti \
        duže ili kraće, ovisno o vrsti, dok neke vrste uopće nemaju bodlje poput peyote kaktusa ili zvjezdastog kaktusa. Većina kaktusa uglavnom cvjeta, a cvijet traje jako kratko. Iako je uglavnom pustinjska biljka i on, kao i druge vrste biljaka,\
        zahtijeva zalijevanje u ranim jutarnjim satima, dok je zimi dovoljno jednom tjedno.",
        "photo" : '010-plant.jpg'  
    }

]

#ukoliko je oznaceno posadena neka se ispise posađeno, kasnije

#ukoliko sve stima:
#napraviti platna za posude
# provjeriti i ispisati bazu za posude
# provjeriti sta s bazom o random podacima
# spojiti botun sa bazom o posudama da ih sprema
# box ispisati sa yt

#natpis unos u bazu treba isto nestati ne ostati


