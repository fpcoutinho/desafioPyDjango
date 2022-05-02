#coding: utf-8
from Calendario import Calendario
from Compromisso import Compromisso

if __name__ == '__main__':
    cal = Calendario()
    comp = Compromisso("Aniversario de Belinha", "2022/05/31", "15:00:00", "22:00:00", "Porquinho", "Levar o bolo.")
    comp2 = Compromisso("Aniversario de Fili", "2022/06/05", "15:00:00", "22:00:00", "Jardim Jericó", "Levar o bolo.")
    cal.addCompromisso(comp)
    cal.addCompromisso(comp2)
    print(cal)
