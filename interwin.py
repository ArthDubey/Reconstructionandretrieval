import tkinter as tk

from PIL import ImageTk,Image

root=tk.Tk()

root.title("EASE")

fname=tk.Canvas(bg="black",height=2000,width=800,relief='ridge',highlightthickness=0,bd=0)

fname.pack()

img1=ImageTk.PhotoImage(file='mech.jpg')

imgur1=ImageTk.PhotoImage(file='recon.png')

imgur2=ImageTk.PhotoImage(file='ret.png')

imgg1= ImageTk.PhotoImage(Image.open("logo.png"))

panel = tk.Label(root, image = imgg1,bg="black")

panel.pack(side = "top", fill = "both", expand = "no")

img=fname.create_image(900,1000,anchor='se',image=img1)

fname.pack()

#wel=tk.Label(root,bg="black",text="Welcome!",fg="blue",font="comicsans 26 bold ",padx=10,pady=10)

#wel.pack(pady=20)

msg1="Our software helps in reconstructing 3d models by using CNN's with limited data, as well as retrieving 3d models from online repositories without any hassle.\n"#write whatever you wish to

mess1=tk.Message(root,text=msg1)

mess1.config(fg="grey",bg="black",font="comicsans 14",justify="center",padx=30,width=600) #change the font as per your choice

mess1.pack(pady=10)

msg2="Choose the feature that you wish to use.\n"

mess2=tk.Message(root,text=msg2)

mess2.config(fg="grey",bg="black",font="comicsans 15",justify="center",padx=30,width=600) #change the font as per your choice

mess2.pack(pady=10)

b1=tk.Button(root,compound="left",image=imgur1,text=" Reconstruction",font='times 22 bold',height=2,width=10,relief='raised',bg='white',fg='DarkOrchid4',bd=3,cursor='hand1')

b1.pack(ipadx=125,ipady=20,padx=5, pady=20)

b2=tk.Button(root,compound="left",image=imgur2,text=" Retrieval-OD",font='times 24 bold',height=2,width=10,relief='raised',bg='white',fg='DarkOrchid4',bd=3,cursor='hand1')

b2.pack(ipadx=125,ipady=20,padx=5, pady=20)

def close():
    
    root.destroy()

bt=tk.Button(root,text="Exit",font='times 22 bold',height=1,width=15,relief='raised',bg='white',fg='red',bd=3,cursor='hand1',command=close)

bt.pack(padx=5, pady=20)

fname.pack(side="left")

root.configure(background='black')

root.mainloop()
