import tkinter
from tkinter import messagebox


def ent():
    while not messagebox.askyesno("ТЫ ПОШЁЛ НЕ ТУДА", "МОЖЕТ ПЕРЕДУМАЕШЬ?"):
        messagebox.showinfo("Плохо", "Попробуй ещё раз")
    messagebox.showinfo("Молодец!", "Продолжим заполнять анкету дальше?")


window = tkinter.Tk()
window.title("Анкета")
window.geometry("600x600+150+150")

txt = tkinter.Label(window, text="АНКЕТА ДЛЯ ВК", font=("Impact", 50)).grid(column=0, row=0)
# canvas = tkinter.Canvas(window, height=400, width=700)
# photo = tkinter.PhotoImage(
# file="l3DY9e0JYmqtjSbwwKPKCd2PHM4nSoZlZekjPPUpezdUGFL8TNPrHlrdElOrNbIWUyn6mm2DvWXKaPSAaTZ1kWB0.jpg")
# image = canvas.create_image(0, 0, photo).grid(column=1, row=1)
btn = tkinter.Button(window, text="ОТКОСИТЬ", bg="pink", fg="purple", command=ent).grid(column=1, row=1)
fio = tkinter.Entry(window, width=20).grid(column=1, row=2)
txt2 = tkinter.Label(window, text="Фамилия Имя Отчество").grid(column=0, row=1)
tkinter.mainloop()
