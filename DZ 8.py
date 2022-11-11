import random
import logging

logging.basicConfig(level = logging.DEBUG,
                   filename = "logs.log",
                   filemode = "w",
                   format = "We have next log message:%(asctime)s - %(message)s")
logging.debug("eto soobshenie dlya debaga")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
try:
    class Batya:
        def __init__(self, zarplata):
            self.zarplata = zarplata
            self.pivo = 2


    class Rabota:
        def __init__(self):
            self.zadacha = 8
            self.batya = batya
        def smena(self):
            if self.zadacha >= 8:
                print("Na robotu")
                self.batya.zarplata += 45
                print(f"{self.batya.zarplata}hrivna")
                if self.batya.zarplata > 50:
                    print("Prohladnoy...")
                    self.batya.zarplata -= 42
                    self.batya.pivo += 2
                    print(f"Na vihodnoi{self.batya.pivo}")
        def vihodnoi(self):
            print("Otdohnut bi konechno")
            if self.batya.pivo >= 3:
                self.batya.pivo -= 3
        def live(self, day):
            cube = random.randint(1, 2)
            if cube == 1:
                self.smena()
            elif cube == 2:
                self.vihodnoi()

    batya = Batya(40)
    rabota = Rabota()
    for day in range(365):
        rabota.live(day)
except Exception:
    logging.exception("Exception")
