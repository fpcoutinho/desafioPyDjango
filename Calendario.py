# coding: utf-8
import datetime
from Compromisso import Compromisso


class Calendario:
    def __init__(self):
        self.lista = list()

    def addCompromisso(self, compr):
        for c in self.lista:
            if (compr.ini >= c.ini and compr.ini < c.fim) or (compr.fim > c.ini and compr.fim <= c.fim):
                raise AttributeError("Erro ao inserir '" + compr.nome +"', um compromisso não pode invadir o tempo do outro.")
        self.lista.append(compr)

    def deletaCompromisso(self, compr):
        self.lista.remove(compr)

    def __str__(self):
        return ''.join([str(x) for x in self.lista])