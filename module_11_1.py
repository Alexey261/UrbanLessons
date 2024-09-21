import tkinter
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

def start_point_get(event):
    global start_x, start_y
    canvas.create_rectangle(event.x, event.y, event.x + 1, event.y + 1, outline="red", tag="rect")
    start_x, start_y = event.x, event.y

def rect_drawing(event):

    if event.x < 0:
        end_x = 0
    else:
        end_x = min(image.width, event.x)
    if event.y < 0:
        end_y = 0
    else:
        end_y = min(image.height, event.y)

    canvas.coords("rect", start_x, start_y, end_x, end_y)

def release_action(event):

    start_x, start_y, end_x, end_y = [int(i) for i in canvas.coords("rect")]
    tkinter.messagebox.showinfo(title="Координаты области", message=f"X0={str(start_x)}\tY0={str(start_y)}\nX1={str(end_x)}\tY1={str(end_y)}")
    canvas.delete("rect")
    insert_pict(start_x, end_x, start_y, end_y)

def insert_pict(x1,x2,y1,y2):
    file_path = filedialog.askopenfilename(title="Open Image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")])
    if file_path:
        image1 = Image.open(file_path)
        image1 = image1.resize((x2-x1, y2-y1), Image.LANCZOS)
        image.paste(image1, (x1,y1), mask=image1)
        image.save('girl1.jpg')
        image_tk = ImageTk.PhotoImage(image)
        canvas.image = image_tk
        canvas.create_image(0, 0, image=image_tk, anchor=tkinter.NW)



if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("My Image")
    root.resizable(0, 0)
    root.attributes("-topmost", True)
    image = Image.open("girl.jpg")
    canvas = tkinter.Canvas(root, width=image.size[0], height=image.size[1])
    canvas.pack()
    image_tk = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=image_tk, anchor=tkinter.NW)

    canvas.bind("<ButtonPress-1>", start_point_get)
    canvas.bind("<Button1-Motion>", rect_drawing)
    canvas.bind("<ButtonRelease-1>", release_action)
    root.mainloop()