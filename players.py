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
        self.__umto34 = False
        self.__doisto35 = False
        self.__tresto36 = False
        self.__red = False
        self.__black = False
        self.__even = False
        self.__odd = False
        self.__umto18 = False
        self.__deznoveto36 = False

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
    def setResetar(self):
        self.__umto12 = False
        self.__trezeto24 = False
        self.__vintecincoto36 = False
        self.__umto34 = False
        self.__doisto35 = False
        self.__tresto36 = False
        self.__red = False
        self.__black = False
        self.__even = False
        self.__odd = False
        self.__umto18 = False
        self.__deznoveto36 = False
    def setCondicoes(self,variavel):
        if variavel == "umto12":
            self.__umto12 = True
        elif variavel == "trezeto24":
            self.__trezeto24 = True
        elif variavel == "vintecincoto36":
            self.__vintecincoto36 = True
        elif variavel == "umto34":
            self.__umto34 = True
        elif variavel == "doisto35":
            self.__doisto35 = True
        elif variavel == "tresto36":
            self.__tresto36 = True
        elif variavel == "red":
            self.__red = True
        elif variavel == "black":
            self.__black = True
        elif variavel == "even":
            self.__even = True
        elif variavel == "odd":
            self.__odd = True
        elif variavel == "umto18":
            self.__umto18 = True
        elif variavel == "deznoveto36":
            self.__deznoveto36 = True



