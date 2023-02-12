import random


def draw_desk():
    global desk
    print("--------------")
    for i in range(0, 9, 3):
        print("|", desk[i], "|", desk[i + 1], "|", desk[i + 2], "|")
        print("--------------")


def examination(x):
    #print(desk[x])
    if str(desk[x]) not in "x0" and 0 < x < 9:
        return False
    else:
        return True


desk = list(range(1, 10))
# print(desk)
draw_desk()
while True:
    user = input("Введите кем Вы хотите управлять? x/0")
    if user in "x0":
        break
state = False
if user == "x":
    while state == False:
        hod = int(input("Введите позицию: "))
        print(examination(hod - 1))
        if not examination(hod - 1): #jdgfkfjldkfhxdkfjsdfh
            desk[int(hod) - 1] = "x"
            state = True

    draw_desk()
    state = False
    print("Теперь мой ход")
    while state == False:
        hod = random.randint(0, 9)
        if not examination(hod):
            desk[hod] = "0"
            state = True

    draw_desk()
