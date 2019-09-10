import tkinter as tk
import time
import tkinter
from tkinter import *
from random import randint,shuffle
import random


class Player():
    def __init__(self,nome):
        self.__nome = nome
        self.__tips = 100
        self.__jogadas = []
        self.__aposta = 0
        self.__rodadasSemApostar = 0
        self.__prosseguir = True
        self.__umto12 = False
        self.__trezeto24 = False
        self.__vintecincoto36 = False

    def getNome(self):
        return self.__nome
    def getTip(self):
        return self.__tips
    def getJogadas(self):
        return self.__jogadas
    def getAposta(self):
        return self.__aposta
    def getProsseguir(self):
        return self.__prosseguir
    def getRodadas(self):
        return self.__rodadasSemApostar

    def setRodadasSemApostar(self):
        self.__rodadasSemApostar += 1

    def setTip(self,value):
        self.__tips += value
    def setAposta(self,value):
        self.__aposta += value
    def setApostaZerar(self):
        self.__aposta = 0
    def setJogadas(self,jogada):
        if jogada in self.__jogadas:
            pass
        elif jogada == "CLEAR":
            self.__jogadas = []
        else:
            self.__jogadas.append(jogada)

    def setProsseguir(self,condicao):
        self.__prosseguir = condicao

