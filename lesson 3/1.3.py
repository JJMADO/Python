with open("test", "w") as f:
    # tyu
    lines = 0
    words = 0
    try:
        for line in f:
            lines += 1
            words += len(line.split())
        print(lines, words)
    except:
        print("Не получилось прочитать файл.")
