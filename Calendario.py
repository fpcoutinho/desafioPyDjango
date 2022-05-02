# coding: utf-8
import datetime
from Compromisso import Compromisso


class Calendario:
    def __init__(self):
        self.lista = list()

    def addCompromisso(self, compr):
        for c in self.lista:
            if c.data == compr.data:
                raise AttributeError("Um compromisso não pode invadir o tempo do outro.")
        self.lista.append(compr)

    def deletaCompromisso(self, compr):
        self.lista.remove(compr)

    def __str__(self):
        return ''.join([str(x) for x in self.lista])