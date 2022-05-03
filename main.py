#coding: utf-8
from Calendario import Calendario
from Compromisso import Compromisso

if __name__ == '__main__':
    cal = Calendario()
    try:
        comp = Compromisso("Aniversario de Belinha", "31/05/2022", "15:00:00", "22:00:00", "Porquinho", "Levar o bolo.")
        comp2 = Compromisso("Aniversario de Fili", "05/06/2022", "16:00:00", "23:00:00", "Jardim Jericó", "Levar o bolo.")
        comp3 = Compromisso("Aniversario de João", "16/12/2022", "16:00:00", "23:00:00", "Jardim Jericó")
        cal.addCompromisso(comp)
        cal.addCompromisso(comp2)
        cal.addCompromisso(comp3)
    except Exception as e:
        print(e)

    print(cal)