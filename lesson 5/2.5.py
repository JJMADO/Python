import tkinter

window = tkinter.Tk()
window.title("Калькулятор")
window.geometry("+900+400")
btn_list = ["%", "CE", "C", "DEL",
            "1/x", "x^2", "x^3", "/",
            "7", "8", "9", "*0",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "+/-", "0", ",", "="]
row = 1
column = 0
for btn in btn_list[2:]:
    cmd = lambda x=btn: calculate(x)
    tkinter.Button(window,
                   text=btn, bg = "#009999",
                   fg = "white", width = 10,
                   command=cmd).grid(row=row,
                                     column=column)
window.mainloop
