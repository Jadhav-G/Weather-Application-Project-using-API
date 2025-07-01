from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk


root = Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False, False)


def getweather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geoapiEercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(
        text=f"{round(location.latitude,4)}°N{round(location.longitude,4)}°E"
    )

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    ### weather api
    APIkey = "e700edd09e614b165ff236ec367ec86f"
    api = f"https://api.openweathermap.org/data/2.5/weather?lat={location.longitude}&lon={location.latitude}&appid={APIkey}&units=metric"
    print(api)
    json_data = requests.get(api).json()
    # api="https://api.openweathermap.org/data/2.5/weather?q={city }&appid={APIkey}"
    # json_data = requests.get(api).json()
    print(json_data)

    ### current
    
    temp = json_data['main']['temp']
    humidity = json_data['main']['humidity']
    pressure = json_data['main']['pressure']
    wind = json_data['wind']['speed']
    description  = json_data['weather'][0]['description']
   # print(temp)"""

    t.config(text=(temp, "°C"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind, "m/s"))
    d.config(text=description)



    firstdayimage = json_data['weather'][0]['icon']
    photo1 =ImageTk.PhotoImage(file=f"icon/{firstdayimage}@2x.png")
    firstimage.config(image=photo1)
    firstimage.image=photo1

    ##second cell
    """seconddayimage = json_data['weather'][0]['icon']
    img=(Image.open(f"icon/{seconddayimage}@2x.png"))    
    resize_image = img.resize((50,50))
    photo2 = ImageTk.PhotoImage(resize_image)
    secondimage.config(image=photo2)
    secondimage.image=photo2



    ##third cell
    thierddayimage = json_data['daily'][2]['weather'][0]['icon']
    print(thierddayimage)


    ### fourthc celll
    fourthdayimage = json_data['daily'][3]['weather'][0]['icon']
    print(fourthdayimage)


    ##fifth cell
    fifthdayimage = json_data['daily'][4]['weather'][0]['icon']
    print(fifthdayimage)


    ###sixth cellll
    sixthdayimage = json_data['daily'][5]['weather'][0]['icon']
    print(sixthdayimage)


    ## seveth celll
    seventhdayimage = json_data['daily'][6]['weather'][0]['icon']
    print(seventhdayimage)"""





    ##day(display day)
    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    # second = first+timedelta(days=1)
    # day2.config(text=second.strftime("%A"))

    # third = first+timedelta(days=2)
    # day3.config(text=third.strftime("%A"))

    # fourth = first+timedelta(days=3)
    # day4.config(text=fourth.strftime("%A"))

    # fifth = first+timedelta(days=4)
    # day5.config(text=fifth.strftime("%A"))

    # sixth = first+timedelta(days=5)
    # day6.config(text=sixth.strftime("%A"))

    # seventh = first+timedelta(days=6)
    # day7.config(text=seventh.strftime("%A"))









## icon
image_icon = PhotoImage(file="images/logo.png")
root.iconphoto(False, image_icon)

Round_box = PhotoImage(file="images/Rounded Rectangle 1.png")
Label(root, image=Round_box, bg="#57adff").place(x=30, y=110)

##lable
Label1 = Label(
    root, text="Temperature", font=("Helvetica", 11), fg="white", bg="#203243"
)
Label1.place(x=50, y=120)

Label2 = Label(root, text="Humidity", font=("Helvetica", 11), fg="white", bg="#203243")
Label2.place(x=50, y=140)

Label3 = Label(root, text="Pressure", font=("Helvetica", 11), fg="white", bg="#203243")
Label3.place(x=50, y=160)

Label4 = Label(
    root, text="Wind speed", font=("Helvetica", 11), fg="white", bg="#203243"
)
Label4.place(x=50, y=180)

Label5 = Label(
    root, text="Description", font=("Helvetica", 11), fg="white", bg="#203243"
)
Label5.place(x=50, y=200)


### search box
Search_images = PhotoImage(file="images/Rounded Rectangle 3.png")
myimage = Label(image=Search_images, bg="#57adff")
myimage.place(x=270, y=120)

weat_images = PhotoImage(file="images/Layer 7.png")
watherimages = Label(root, image=weat_images, bg="#203243")
watherimages.place(x=290, y=127)


textfield = tk.Entry(
    root,
    justify="center",
    width=15,
    font=("poppins", 25, "bold"),
    bg="#203243",
    border=0,
    fg="white",
)
textfield.place(x=370, y=130)
textfield.focus()

Search_icon = PhotoImage(file="images/Layer 6.png")
myimage_icon = Button(
    image=Search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=getweather
)
myimage_icon.place(x=645, y=125)


### bottem box
frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

## bottem boxes
firstbox = PhotoImage(file="images/Rounded Rectangle 2.png")
secondbox = PhotoImage(file="images/Rounded Rectangle 2 copy.png")

Label(frame, image=firstbox, bg="#212120").place(x=30, y=20)
"""Label(frame, image=secondbox, bg="#212120").place(x=300, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=400, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=500, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=600, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=700, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=800, y=30)"""

### clock(here we will place time)
clock = Label(root, font=("Helvetica", 30, "bold"), fg="white", bg="#57adff")
clock.place(x=30, y=20)

## timeZone
timezone = Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
timezone.place(x=700, y=20)

long_lat = Label(root, font=("Helvetica", 10), fg="white", bg="#57adff")
long_lat.place(x=700, y=50)


### thpwd
t = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
t.place(x=150, y=120)
h = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
h.place(x=150, y=140)
p = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
p.place(x=150, y=160)
w = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
w.place(x=150, y=180)
d = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
d.place(x=150, y=200)


### first cell
firstframe = Frame(root,width=230 , height=132,bg="#282829")
firstframe.place(x=35,y=315)

day1=Label(firstframe,font="arial 20" ,bg="#282829" ,fg="#fff")
day1.place(x=100,y=5)

firstimage = Label(firstframe, bg="#282829")
firstimage.place(x=1,y=15)

day1temp =Label(firstframe, bg="#282829",fg="#57adff",font="arial 15 bold")
day1temp.place(x=7,y=20)


### second cell
"""secondframe = Frame(root,width=70 , height=115,bg="white")
secondframe.place(x=305,y=325)

day2=Label(secondframe ,bg="#282829" ,fg="#fff")
day2.place(x=10,y=5)

secondimage = Label(secondframe ,bg="#282829")
secondimage.place(x=7,y=20)

### third cell (yethe frame white keli aahe)
thirdframe = Frame(root,width=70 , height=115,bg="white")
thirdframe.place(x=405,y=325)

day3=Label(thirdframe ,bg="#282829" ,fg="#fff")
day3.place(x=10,y=5)

thirdimage = Label(thirdframe ,bg="#282829")
thirdimage.place(x=7,y=20)

### fourth cell
fourthframe = Frame(root,width=70 , height=115,bg="white")
fourthframe.place(x=505,y=325)

day4=Label(fourthframe ,bg="#282829" ,fg="#fff")
day4.place(x=10,y=5)

fourthimage = Label(fourthframe ,bg="#282829")
fourthimage.place(x=7,y=20)

### fifth cell
fifthframe = Frame(root,width=70 , height=115,bg="white")
fifthframe.place(x=605,y=325)

day5=Label(fifthframe ,bg="#282829" ,fg="#fff")
day5.place(x=10,y=5)

fifthimage = Label(fifthframe ,bg="#282829")
fifthimage.place(x=7,y=20)

### sixth cell
sixthframe = Frame(root,width=70 , height=115,bg="white")
sixthframe.place(x=705,y=325)

day6=Label(sixthframe ,bg="#282829" ,fg="#fff")
day6.place(x=10,y=5)

sixthimage = Label(sixthframe ,bg="#282829")
sixthimage.place(x=7,y=20)

### seveth celll
seventhframe = Frame(root,width=70 , height=115,bg="white")
seventhframe.place(x=805,y=325)

day7=Label(seventhframe ,bg="#282829" ,fg="#fff")
day7.place(x=10,y=5)

sevenimage = Label(seventhframe ,bg="#282829")
secondimage.place(x=7,y=20)"""







root.mainloop()
