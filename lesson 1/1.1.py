import random


def draw_desk():
    global desk
    print("-------------")
    for i in range(0, 9, 3):
        print("|", desk[i], "|", desk[i + 1], "|", desk[i + 2], "|")
        print("-------------")


def examinataion(X):
    #print("р")
    if str(desk[X]) in "X0" and 0 < X < 9:
        return False
    else:
        return False


desk = list(range(1, 10))
#
draw_desk()
while True:
    user = input("Введите кем Вы хотите быть? X/0")
    if user in "X0":
        break
state = False
if user == "X":
    while state == False:
        hod = int(input("Введите позицию:  "))
        if not examinataion(hod-1):
            desk[int(hod) - 1] = "X"
        state = True

    draw_desk()
    state = False
    print("Теперь мой ход")
    while state == False:
        hod2 = random.randint(0, 9)
        if examinataion(hod):
            desk[hod] = "0"
            state = True
    draw_desk()
