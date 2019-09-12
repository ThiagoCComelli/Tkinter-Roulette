import tkinter as tk
import time
import tkinter
from tkinter import *
from random import randint,shuffle
import random

class Roleta():
    def __init__(self):
        self.__roletaeuro = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36]
        self.__roletafran = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36]
        self.__roletaame =  [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,0,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36]
        self.__num = None
        self.__umto12list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.__trezeto24list = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        self.__vintecincoto36list = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        self.__umto34list = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
        self.__doisto35list = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
        self.__tresto36list = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
        self.__redlist = [1, 3, 5, 7, 9, 12, 14, 18, 16, 21, 23, 25, 27, 28, 30, 32, 34, 36]
        self.__blacklist = [2, 6, 4, 8, 10, 11, 13, 15, 17, 19, 20, 22, 24, 26, 29, 31, 33, 35]
        self.__evenlist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
        self.__oddlist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
        self.__umto18list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.__deznoveto36list = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

    def getNumEuro(self):
        self.__num = random.choice(self.__roletaeuro)
        return self.__num

    def getNumFran(self):
        self.__num = random.choice(self.__roletafran)
        return self.__num

    def getNumAme(self):
        self.__num = random.choice(self.__roletaame)
        return self.__num

    def getNum(self):
        return self.__num

"""
    def fazerApostaBotoes(self,numero):
        if numero == "ODD":
            lista = [[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]]
            for i in lista:
                self.__playersjogando[self.getVez()].setJogadas(i)
            self.__playersjogando[self.getVez()].setCondicoes("odd")
        elif numero == "EVEN":
            lista = [[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]]
            for i in lista:
                self.__playersjogando[self.getVez()].setJogadas(i)
            self.__playersjogando[self.getVez()].setCondicoes("even")
        elif numero == "RED":
            lista = [[1,3,5,7,9,12,14,16,18,21,23,25,27,28,30,32,34,36]]
            for i in lista:
                self.__playersjogando[self.getVez()].setJogadas(i)
            self.__playersjogando[self.getVez()].setCondicoes("red")
        elif numero == "BLACK":
            lista = [[2,4,6,8,10,11,13,15,17,19,20,22,24,26,29,31,33,35]]
            for i in lista:
                self.__playersjogando[self.getVez()].setJogadas(i)
            self.__playersjogando[self.getVez()].setCondicoes("black")
        elif numero == "UMTO18":
            lista = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]]
            for i in lista:
                self.__playersjogando[self.getVez()].setJogadas(i)
            self.__playersjogando[self.getVez()].setCondicoes("umto18")
        elif numero == "DEZNOVETO36":
            lista = [[19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36]]
            for i in lista:
                self.__playersjogando[self.getVez()].setJogadas(i)
            self.__playersjogando[self.getVez()].setCondicoes("deznoveto36")
        elif numero == "LINHA1":
            lista = [[1,4,7,10,13,16,19,22,25,28,31,34]]
            for i in lista:
                self.__playersjogando[self.getVez()].setJogadas(i)
            self.__playersjogando[self.getVez()].setCondicoes("umto34")
        elif numero == "LINHA2":
            lista = [[2,5,8,11,14,17,20,23,26,29,32,35]]
            for i in lista:
                self.__playersjogando[self.getVez()].setJogadas(i)
            self.__playersjogando[self.getVez()].setCondicoes("doisto35")
        elif numero == "LINHA3":
            lista = [[3,6,9,12,15,18,21,24,27,30,33,36]]
            for i in lista:
                self.__playersjogando[self.getVez()].setJogadas(i)
            self.__playersjogando[self.getVez()].setCondicoes("tresto36")
        elif numero == "UMST12":
            lista = [[1,2,3,4,5,6,7,8,9,10,11,12]]
            for i in lista:
                self.__playersjogando[self.getVez()].setJogadas(i)
            self.__playersjogando[self.getVez()].setCondicoes("umto12")
        elif numero == "DOISST12":
            lista = [[13,14,15,16,17,18,19,20,21,22,23,24]]
            for i in lista:
                self.__playersjogando[self.getVez()].setJogadas(i)
            self.__playersjogando[self.getVez()].setCondicoes("trezeto24")
        elif numero == "TRESST12":
            lista = [[25,26,27,28,29,30,31,32,33,34,35,36]]
            for i in lista:
                self.__playersjogando[self.getVez()].setJogadas(i)
            self.__playersjogando[self.getVez()].setCondicoes("vintecincoto36")
        else:
            self.__playersjogando[self.getVez()].setJogadas(numero)
"""


