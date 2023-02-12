import tkinter

import pygame


def cmd2(btn):
    global text
    if btn in "0123456789,.+-*/":
        text.insert(tkinter.END, btn)
    elif btn == "=":
        a = text.get()

        result = eval(text.get())
        # print(result)
        text.delete(0, tkinter.END)
        text.insert(tkinter.END, result)
        primer.config(text=a + "=")
    elif btn == "DEL":
        text.delete(len(text.get()) - 1)
        # print(len(text.get()))
    elif btn == "C":
        text.delete(0, tkinter.END)
        primer.config(text="")
    elif btn == "%":
        a = text.get()
        b = a[:a.find("-")]
        c = a[a.find("-")+1:]
        print(b, c)


window = tkinter.Tk()
window.title("Calculator")
pygame.mixer.init()
pygame.mixer.music.load("nokiaarab.mp3")
pygame.mixer.music.play(-1)
photo = tkinter.PhotoImage(
    file="C:\\Users\\Студент15\\Desktop\\нога\\lesson 5\\68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f4944773872493334657a764672673d3d2d3935343230343239372e313633633162373538343534356630633 (1).png")
w = tkinter.Label(window, image=photo)
w.grid(row=0, column=0, columnspan=4, rowspan=8)
btn = ("%", "CE", "C", "DEL",
       "1/x", "x^2", "x^3", "/",
       "7", "8", "9", "*",
       "4", "5", "6", "-",
       "1", "2", "3", "+",
       "+/-", "0", ",", "=")
primer = tkinter.Label(window, bg="black", fg="white", width=60, font=("Helvetica", 15))
primer.grid(row=0, column=0, columnspan=4)

text = tkinter.Entry(window, width=75, font=("Helvetica", 20))
text.grid(row=1, column=0, columnspan=4)
text.focus()
c = 0
r = 2
for i in btn:
    cmd = lambda x=i: cmd2(x)
    tkinter.Button(window, text=i, bg="black", fg="white", width=15, command=cmd).grid(row=r, column=c)
    c += 1
    if c > 3:
        c = 0
        r += 1

window.mainloop()
