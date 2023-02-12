try:
    lec = pract = lab = 0
    with open("timetable", "r", encoding="utf - 8") as f:
        for line in f:
            if "лекц" in line.lower():
                lec += 1
            pract += line.lower().count("практ.")
            #print(line)
            print(lec, pract)
        f.seek(0)
        print(f.read().count("лаб."))

except FileNotFoundError:
    print("Такого файла не существует")
