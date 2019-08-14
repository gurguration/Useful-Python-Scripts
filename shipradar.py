from tkinter import *

'''კოდმა რომ იმუშაოს ფანჯარაში მაუსზე დაჭერილი ღილაკი უნდა ამოძრაო
როგოცკი მოხვდება 100 მეტრის რადიუსში ინთება "ტოჩკა"
'''
canvas_width = 1200
canvas_height = 600

shipx = 300 # აქ არის ჩვენი დამალული "ტოჩკა" ხ კორდინატი
shipy = 450 # იგივე Y კორიდნატი ტოჩკის თუ სხვაობა 100-მეტია. ანუ 100 მეტრის რადიუსშია 
ინთება 



def paint(event):
   python_green = "#476042"
   x1, y1 = event.x,event.y
   print(x1)
   if abs(x1 - shipx) < 100 and abs(y1 - shipy) < 100:
       w.create_oval(shipx-3,shipy-3, shipx+3, shipy+3, fill=python_green)
   else:
       w.delete('all')



master = Tk()
master.title("Points")
w = Canvas(master,
          width=canvas_width,
          height=canvas_height)
w.pack(expand=YES, fill=BOTH)
w.bind("<B1-Motion>", paint)

message = Label(master, text="Press and Drag the mouse to draw")
message.pack(side=BOTTOM)

mainloop()
