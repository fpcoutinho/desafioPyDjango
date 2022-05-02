# coding: utf-8
import datetime


class Compromisso:
    def __init__(self, nome, data, ini, fim, local, obs=""):
        self.nome = nome
        self.local = local
        self.obs = obs  # obs não é obrigatório
        self.ini = datetime.datetime.strptime(data + " " + ini, '%Y/%m/%d %H:%M:%S')
        self.fim = datetime.datetime.strptime(data + " " + fim, '%Y/%m/%d %H:%M:%S')
        if self.ini > self.fim or self.ini > datetime.datetime.now():
            raise AttributeError("Data inválida")
        self.status = "Agendado"

    def editCompromisso(self, nome, data, ini, fim, local, status, obs=""):
        self.nome = nome
        self.local = local
        self.obs = obs  # obs não é obrigatório
        self.ini = datetime.datetime.strptime(data + " " + ini, '%Y/%m/%d %H:%M:%S')
        self.fim = datetime.datetime.strptime(data + " " + fim, '%Y/%m/%d %H:%M:%S')
        if self.ini > self.fim or self.ini > datetime.datetime.now():
            raise AttributeError("Data inválida")
        self.status = "Agendado"

    def __str__(self):
        return "\n" + self.nome + "\n" + self.status + "\n" + self.data + "\n" + self.ini + " - " + self.fim + "\n" + self.local + "\n" + self.obs + "\n"
