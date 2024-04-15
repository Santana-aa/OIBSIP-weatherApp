from tkinter import *
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
def weather():
    try:
        city=location.get()
        data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=14e88dffac38d5fadbdc58d6d8efba0e").json()
        label33.config(text=data["weather"][0]["description"])
        label44.config(text=data["main"]["pressure"])
        label11.config(text=data["main"]["humidity"])
        label22.config(text=data["wind"]["speed"])

        t=int(data["main"]["temp"]-273.15)
        temp.config(text=str(t)+"°")
        w=data["weather"][0]["main"]
        ff=int(data["main"]["feels_like"]-273.15)
        f.config(text=f"{w} | Feels Like {ff}°C")

        icon=data["weather"][0]["icon"]
        photo1=ImageTk.PhotoImage(file=f"images/{icon}@2x.png")
        image1.config(image=photo1)
        image1.image=photo1

    except Exception as e:
        messagebox.showerror("Basic Weather App","Invalid Data")

root=Tk()
root.title("Basic Weather App")
root.geometry("500x500")
root.resizable(False,False)
photo=PhotoImage(file="images/layout11.png")
label=Label(image=photo)
label.place(x=0,y=0)

iconImage = PhotoImage(file="images/iconimg.png")
ic=Label(image=iconImage,bg="white")
ic.place(x=350,y=150)
image1 = Label(bg="white")
image1.place(x=350,y=150)

location=Entry(root,justify="center",font=("Helvetica",12,"bold"),border=0,bg="white")
location.place(x=61,y=58)
location.focus()

button= Button(root,text="Done",font=("Monospace",10,"bold"),bg="white",border=1,command=weather)
button.place(x=130,y=90)

label1= Label(root,text="Humidity",font=("Monospace",10,"bold"),bg="#B6D5F0")
label1.place(x=85,y=400)
label11= Label(root,text=".....",font=("Monospace",10,"bold"),bg="#B6D5F0")
label11.place(x=85,y=425)

label2= Label(root,text="Wind Speed",font=("Monospace",10,"bold"),bg="#B6D5F0")
label2.place(x=250,y=400)
label22= Label(root,text=".....",font=("Monospace",10,"bold"),bg="#B6D5F0")
label22.place(x=250,y=425)

label3= Label(root,text="Description",font=("Monospace",10,"bold"),bg="#B6D5F0")
label3.place(x=85,y=320)
label33= Label(root,text=".....",font=("Monospace",10,"bold"),bg="#B6D5F0")
label33.place(x=85,y=345)

label4= Label(root,text="Pressure",font=("Monospace",10,"bold"),bg="#B6D5F0")
label4.place(x=250,y=320)
label44= Label(root,text=".....",font=("Monospace",10,"bold"),bg="#B6D5F0")
label44.place(x=250,y=345)

temp= Label(text="",font=("arial",60,"bold"),bg="white",fg="#F7522E")
temp.place(x=100,y=160)
f= Label(text="",font=("arial",10,"bold"),bg="white",fg="#F7522E")
f.place(x=100,y=250)

root.mainloop()
