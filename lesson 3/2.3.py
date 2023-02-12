import logging
logging.basicConfig(filename="log.txt", level=logging.DEBUG)
try:
    print(123 / "пошшпапароорпаорпаршкррггр")
    try:
        print(12 / 3)
    except:
        print("fghj")
except:
    print("Leloo Dallas!")
    logging.error("Leeloo Dallas!")
finally:
    print("вапролдж")
