from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("Canvas")
root.geometry("600x600")
label_color=Label(root,text="Enter a Color :")
color_input=Entry(root)
artist_img=ImageTk.PhotoImage(Image.open("start_point1.png"))
canvas=Canvas(root,width=590,height=510,bg="white",highlightbackground="gray")
my_image=canvas.create_image(50,50,image=artist_img)

direction=""
oldx=50
oldy=50
newx=50
newy=50






def draw(direction,oldx,oldy,newx,newy):
    fill_color=color_input.get()
    
    if(direction=="right"):
        right_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)
        canvas.move(my_image,5,0)
    if(direction=="left"):
        left_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)
        canvas.move(my_image,-5,0)
    if(direction=="up"):
        up_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)
        canvas.move(my_image,0,-5)
    if(direction=="down"):
        down_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)
        canvas.move(my_image,0,5)
    
def right_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newx=newx+5
    direction="right"
    draw(direction,oldx,oldy,newx,newy)
    
def left_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newx=newx-5
    direction="left"
    draw(direction,oldx,oldy,newx,newy)
    
def up_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newy=newy-5
    direction="up"
    draw(direction,oldx,oldy,newx,newy)
    
def down_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newy=newy+5
    direction="down"
    draw(direction,oldx,oldy,newx,newy)
    
    
    
root.bind("<Right>",right_dir)
root.bind("<Left>",left_dir)
root.bind("<Up>",up_dir)
root.bind("<Down>",down_dir)





label_color.place(relx=0.6,rely=0.9,anchor=CENTER)
color_input.place(relx=0.8,rely=0.9,anchor=CENTER)
color_input.insert(0,"black")
canvas.pack()
root.mainloop()