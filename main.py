import tkinter as tk
import time
import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import *
from random import randint
from roleta import Roleta
from players import Player

class Cassino:
    def __init__(self, master):
        self.__roleta = Roleta()
        self.__players = 0
        self.__vez = 0
        self.__playersjogando = []
        self.__modo = "NENHUM"
        self.__banco = 1000
        self.__apostados = []
        self.__falencia = []
        self.__faliram = ""
        self.menu()

    def fazerAposta(self,valor):
        if valor == 0:
            self.__playersjogando[self.getVez()].setApostaZerar()
        else:
            self.__playersjogando[self.getVez()].setAposta(valor)
        self.valornatela.configure(text='{}'.format(self.__playersjogando[self.getVez()].getAposta()), font="Times 25 bold", fg="red", bg="black")
        self.listadejogadas.configure(text='JOGADAS: {}'.format(self.__playersjogando[self.getVez()].getJogadas()), font="Times 25 bold", fg="red", bg="black")

    def limparJogada(self):
        self.listadejogadas.configure(text='JOGADAS: {}'.format(self.__playersjogando[self.getVez()].setJogadas("CLEAR")), font="Times 25 bold", fg="red", bg="black")
        self.__playersjogando[self.getVez()].setResetar()

    def fazerApostaBotoes(self,numero):
        if numero == "ODD":
            self.__playersjogando[self.getVez()].setJogadas("ODD")
            self.__playersjogando[self.getVez()].setCondicoes("odd")
        elif numero == "EVEN":
            self.__playersjogando[self.getVez()].setJogadas("EVEN")
            self.__playersjogando[self.getVez()].setCondicoes("even")
        elif numero == "RED":
            self.__playersjogando[self.getVez()].setJogadas("RED")
            self.__playersjogando[self.getVez()].setCondicoes("red")
        elif numero == "BLACK":
            self.__playersjogando[self.getVez()].setJogadas("BLACK")
            self.__playersjogando[self.getVez()].setCondicoes("black")
        elif numero == "UMTO18":
            self.__playersjogando[self.getVez()].setJogadas("1-18")
            self.__playersjogando[self.getVez()].setCondicoes("umto18")
        elif numero == "DEZNOVETO36":
            self.__playersjogando[self.getVez()].setJogadas("19-36")
            self.__playersjogando[self.getVez()].setCondicoes("deznoveto36")
        elif numero == "LINHA1":
            self.__playersjogando[self.getVez()].setJogadas("1ST LINE")
            self.__playersjogando[self.getVez()].setCondicoes("umto34")
        elif numero == "LINHA2":
            self.__playersjogando[self.getVez()].setJogadas("2ST LINE")
            self.__playersjogando[self.getVez()].setCondicoes("doisto35")
        elif numero == "LINHA3":
            self.__playersjogando[self.getVez()].setJogadas("3ST LINE")
            self.__playersjogando[self.getVez()].setCondicoes("tresto36")
        elif numero == "UMST12":
            self.__playersjogando[self.getVez()].setJogadas("1ST 12")
            self.__playersjogando[self.getVez()].setCondicoes("umto12")
        elif numero == "DOISST12":
            self.__playersjogando[self.getVez()].setJogadas("2ST 12")
            self.__playersjogando[self.getVez()].setCondicoes("trezeto24")
        elif numero == "TRESST12":
            self.__playersjogando[self.getVez()].setJogadas("3ST 12")
            self.__playersjogando[self.getVez()].setCondicoes("vintecincoto36")
        else:
            self.__playersjogando[self.getVez()].setJogadas(numero)

        self.listadejogadas.configure(text='JOGADAS: {}'.format(self.__playersjogando[self.getVez()].getJogadas()), font="Times 25 bold", fg="red", bg="black")


    def voltarMenu(self):
        if self.getPl() == 0:
            self.menu()
            self.buttonsMenu()

    def getPlayersJogando(self):
        return self.__playersjogando

    def getModo(self):
        return self.__modo

    def getPl(self):
        return self.__players

    def getVez(self):
        return self.__vez

    def getTipBanco(self):
        return self.__banco

    def getRoleta(self):
        return self.__roleta

    def setpl(self, qtde):
        self.__players = qtde
        self.jogadorestit.configure(text='QUANTIDADE DE JOGADORES: {}'.format(self.__players), font="Times 25 bold",fg="red", bg="black")

    def setModo(self, modo):
        self.__modo = modo
        self.modedejogotit.configure(text='MODO DE JOGO: {}'.format(self.__modo), font="Times 25 bold", fg="red",bg="black")

    def setPlayers(self):
        nomes = ["ALPHA", "BETA", "CHARLIE", "DELTA"]
        for i in range(self.__players):
            nomes[i] = Player(nomes[i])
            a = nomes[i]
            self.__playersjogando.append(a)

    def setTipBanco(self, valor):
        self.__banco += valor

    def setPassar(self):
        if self.__playersjogando[self.getVez()].getTip() <= 0:
            self.__vez += 1

            self.jogadordavez.configure(text='{}'.format(self.__playersjogando[self.getVez()].getNome()),font="Times 25 bold", fg="red", bg="black")
            self.valornatela.configure(text='{}'.format(self.__playersjogando[self.getVez()].getAposta()),font="Times 25 bold", fg="red", bg="black")
            self.jogadortip.configure(text='SEU DINHEIRO: {}'.format(self.__playersjogando[self.getVez()].getTip()),font="Times 25 bold", fg="red", bg="black")
            self.listadejogadas.configure(text='JOGADAS: {}'.format(self.__playersjogando[self.getVez()].getJogadas()),font="Times 25 bold", fg="red", bg="black")

        elif self.__playersjogando[self.getVez()].getRodadas() <= 2:
            self.__playersjogando[self.getVez()].setRodadasSemApostar()
            self.__playersjogando[self.getVez()].setProsseguir(False)

            self.__vez += 1

            if self.getVez() == self.getPl():
                self.jogadordavez.configure(text='', font="Times 25 bold", fg="red", bg="black")
                self.valornatela.configure(text='', font="Times 25 bold", fg="red", bg="black")
                self.listadejogadas.configure(text='', font="Times 25 bold", fg="red", bg="black")
                self.jogadortip.configure(text='', font="Times 25 bold", fg="red", bg="black")
                self.clique.configure(text='CLIQUE! =>', font="Times 20 bold", fg="red", bg="black")

            self.jogadordavez.configure(text='{}'.format(self.__playersjogando[self.getVez()].getNome()), font="Times 25 bold",fg="red", bg="black")
            self.valornatela.configure(text='{}'.format(self.__playersjogando[self.getVez()].getAposta()), font="Times 25 bold",fg="red", bg="black")
            self.jogadortip.configure(text='SEU DINHEIRO: {}'.format(self.__playersjogando[self.getVez()].getTip()),font="Times 25 bold", fg="red", bg="black")
            self.listadejogadas.configure(text='JOGADAS: {}'.format(self.__playersjogando[self.getVez()].getJogadas()),font="Times 25 bold", fg="red", bg="black")

        elif self.__playersjogando[self.getVez()].getRodadas() > 3:
            self.jogadordavez.configure(text='{}'.format(self.__playersjogando[self.getVez()].getNome()),font="Times 25 bold", fg="red", bg="black")
            self.valornatela.configure(text='{}'.format(self.__playersjogando[self.getVez()].getAposta()),font="Times 25 bold", fg="red", bg="black")
            self.jogadortip.configure(text='SEU DINHEIRO: {}'.format(self.__playersjogando[self.getVez()].getTip()),font="Times 25 bold", fg="red", bg="black")
            self.listadejogadas.configure(text='JOGADAS: {}'.format(self.__playersjogando[self.getVez()].getJogadas()),font="Times 25 bold", fg="red", bg="black")

    def updatetimer(self):
        self.validade.configure(text='', font="Times 60 bold", fg="yellow", bg="black")

    def setVez(self):
        if (self.__playersjogando[self.getVez()].getAposta()*len(self.__playersjogando[self.getVez()].getJogadas())) > self.__playersjogando[self.getVez()].getTip():
            self.validade.configure(text='APOSTA INVALIDA', font="Times 100 bold", fg="yellow", bg="black")
            self.validade.after(2000, self.updatetimer)

        else:
            if self.__playersjogando[self.getVez()].getAposta() != 0 and len(self.__playersjogando[self.getVez()].getJogadas()) > 0:
                self.__playersjogando[self.getVez()].setResetarSemJogar()
                self.__vez += 1

                if self.getVez() == self.getPl():
                    self.jogadordavez.configure(text='',font="Times 25 bold", fg="red", bg="black")
                    self.valornatela.configure(text='',font="Times 25 bold", fg="red", bg="black")
                    self.listadejogadas.configure(text='',font="Times 25 bold", fg="red", bg="black")
                    self.jogadortip.configure(text='',font="Times 25 bold", fg="red", bg="black")

                    self.clique.configure(text='CLIQUE! =>', font="Times 20 bold", fg="red", bg="black")

                self.jogadordavez.configure(text='{}'.format(self.__playersjogando[self.getVez()].getNome()), font="Times 25 bold", fg="red", bg="black")
                self.valornatela.configure(text='{}'.format(self.__playersjogando[self.getVez()].getAposta()), font="Times 25 bold", fg="red", bg="black")
                self.jogadortip.configure(text='SEU DINHEIRO: {}'.format(self.__playersjogando[self.getVez()].getTip()), font="Times 25 bold", fg="red", bg="black")
                self.listadejogadas.configure(text='JOGADAS: {}'.format(self.__playersjogando[self.getVez()].getJogadas()), font="Times 25 bold", fg="red", bg="black")

    def verificarApostasJogadores(self):
        for i in range(self.__players):
            qtde = len(self.__playersjogando[self.getVez()].getJogadas())
            if self.__playersjogando[i].getProsseguir() == True:
                # intern
                apostou = self.__playersjogando[i].getAposta()
                if self.getRoleta().getNum() == 0:
                    self.setTipBanco(apostou)
                    break

                elif self.getRoleta().getNum() in self.__playersjogando[i].getJogadas():
                    print("1")
                    self.getPlayersJogando()[i].setTip(apostou*36)
                    self.setTipBanco(-apostou*36)
                else:
                    self.setTipBanco(apostou*qtde)
                    self.getPlayersJogando()[i].setTip(-apostou*qtde)

                #extern
                if self.__playersjogando[i].getumto12() == True and self.getRoleta().umto12check(self.getRoleta().getNum()):
                    print("3")
                    self.getPlayersJogando()[i].setTip(apostou*3)
                    self.setTipBanco(-apostou*3)

                if self.__playersjogando[i].gettrezeto24() == True and self.getRoleta().trezeto24check(self.getRoleta().getNum()):
                    print("5")
                    self.getPlayersJogando()[i].setTip(apostou*3)
                    self.setTipBanco(-apostou*3)

                if self.__playersjogando[i].getunto34() == True and self.getRoleta().umto34check(self.getRoleta().getNum()):
                    print("7")
                    self.getPlayersJogando()[i].setTip(apostou*3)
                    self.setTipBanco(-apostou*3)

                if self.__playersjogando[i].getdoisto35() == True and self.getRoleta().doisto35check(self.getRoleta().getNum()):
                    print("9")
                    self.getPlayersJogando()[i].setTip(apostou*3)
                    self.setTipBanco(-apostou*3)

                if self.__playersjogando[i].gettresto36() == True and self.getRoleta().tresto36check(self.getRoleta().getNum()):
                    print("11")
                    self.getPlayersJogando()[i].setTip(apostou*3)
                    self.setTipBanco(-apostou*3)

                if self.__playersjogando[i].getred() == True and self.getRoleta().redlistcheck(self.getRoleta().getNum()):
                    print("13")
                    self.getPlayersJogando()[i].setTip(apostou*2)
                    self.setTipBanco(-apostou*2)

                if self.__playersjogando[i].getublack() == True and self.getRoleta().blacklistcheck(self.getRoleta().getNum()):
                    print("15")
                    self.getPlayersJogando()[i].setTip(apostou*2)
                    self.setTipBanco(-apostou*2)

                if self.__playersjogando[i].geteven() == True and self.getRoleta().evenlistcheck(self.getRoleta().getNum()):
                    print("17")
                    self.getPlayersJogando()[i].setTip(apostou*2)
                    self.setTipBanco(-apostou*2)

                if self.__playersjogando[i].getodd() == True and self.getRoleta().oddlistcheck(self.getRoleta().getNum()):
                    print("19")
                    self.getPlayersJogando()[i].setTip(apostou*2)
                    self.setTipBanco(-apostou*2)

                if self.__playersjogando[i].getumto18() == True and self.getRoleta().umto18listcheck(self.getRoleta().getNum()):
                    print("21")
                    self.getPlayersJogando()[i].setTip(apostou*2)
                    self.setTipBanco(-apostou*2)

                if self.__playersjogando[i].getdeznoveto36() == True and self.getRoleta().deznoveto36check(self.getRoleta().getNum()):
                    print("23")
                    self.getPlayersJogando()[i].setTip(apostou*2)
                    self.setTipBanco(-apostou*2)

        for i in self.getPlayersJogando():
            i.setApostaZerar()
            i.setProsseguir(True)
            i.setResetar()

            self.falencia(i)

        if self.getTipBanco() < 0:
            self.gameoverBanco()



        self.bancot.configure(text='DINHEIRO DO BANCO: {}'.format(self.__banco), font="Times 25 bold", fg="red",bg="black")

    def gameoverBanco(self):
        self.photo = PhotoImage(file="images/preto.gif")
        self.backlabel = Label(root, image=self.photo).place(x=-1, y=-1)

        self.gameover = tk.Label(root)
        self.gameover.grid(row=0, column=0)
        self.gameover.configure(text='GAME OVER, BANCO FALIU', font="Times 70 bold", fg="RED", bg="black")
        self.gameover.place(x=400, y=400)

    def gameoverPlayers(self):
        self.photo = PhotoImage(file="images/preto.gif")
        self.backlabel = Label(root, image=self.photo).place(x=-1, y=-1)

        self.gameover = tk.Label(root)
        self.gameover.grid(row=0, column=0)
        self.gameover.configure(text='GAME OVER, BANCO GANHOU', font="Times 70 bold", fg="RED", bg="black")
        self.gameover.place(x=400, y=400)





    def getNumganhador(self):
        if self.getVez() == self.getPl():
            if self.getModo() == "EUROPEU":
                num = self.__roleta.getNumEuro()
            elif self.getModo() == "AMERICANO":
                num = self.__roleta.getNumAme()
            elif self.getModo() == "FRANCES":
                num = self.__roleta.getNumFran()

            self.numganhador.configure(text='{}'.format(num), font="Times 70 bold", fg="black", bg="white")
            self.clique.configure(text='', font="Times 20 bold", fg="red", bg="black")
            self.__vez = 0

            self.verificarApostasJogadores()

            for i in self.getPlayersJogando():
                i.setJogadas("CLEAR")

        if self.getPl() == 0:
            self.gameoverPlayers()
        else:
            self.valornatela.configure(text='{}'.format(self.__playersjogando[self.getVez()].getAposta()), font="Times 25 bold", fg="red", bg="black")
            self.jogadordavez.configure(text='{}'.format(self.__playersjogando[self.getVez()].getNome()), font="Times 25 bold", fg="red", bg="black")
            self.jogadortip.configure(text='SEU DINHEIRO: {}'.format(self.__playersjogando[self.getVez()].getTip()), font="Times 25 bold", fg="red", bg="black")
            self.listadejogadas.configure(text='JOGADAS: {}'.format(self.__playersjogando[self.getVez()].getJogadas()), font="Times 25 bold", fg="red", bg="black")

    def getFalencia(self):
        print(len(self.__falencia))
        return len(self.__falencia)

    def menu(self):

        self.photo = PhotoImage(file="images/preto.gif")
        self.backlabel = Label(root, image=self.photo).place(x=-1, y=-1)

        self.titulo = tk.Label(root)
        self.titulo.grid(row=0, column=0)
        self.titulo.configure(text='JOGO DA ROLETA!', font="Times 25 bold",fg="red",bg="black")
        self.titulo.place(x=750,y=50)

        self.jogadorestit = tk.Label(root)
        self.jogadorestit.grid(row=0, column=0)
        self.jogadorestit.configure(text='QUANTIDADE DE JOGADORES: {}'.format(self.__players), font="Times 25 bold", fg="red", bg="black")
        self.jogadorestit.place(x=1000,y=450)

        self.modedejogotit = tk.Label(root)
        self.modedejogotit.grid(row=0, column=0)
        self.modedejogotit.configure(text='MODO DE JOGO: {}'.format(self.__modo), font="Times 25 bold", fg="red", bg="black")
        self.modedejogotit.place(x=1000, y=300)

        self.modedejogo = tk.Label(root)
        self.modedejogo.grid(row=0, column=0)
        self.modedejogo.configure(text='MODO DE JOGO:', font="Times 25 bold",fg="red", bg="black")
        self.modedejogo.place(x=100, y=300)

        self.jogadores = tk.Label(root)
        self.jogadores.grid(row=0, column=0)
        self.jogadores.configure(text='JOADORES:', font="Times 25 bold", fg="red", bg="black")
        self.jogadores.place(x=181, y=450)


        self.root = root.geometry("1850x1013"), root.resizable(width=False, height=False)

        add1 = tkinter.Button(master=root, text="EUROPEU", width=13, command=lambda: self.setModo("EUROPEU"), fg="red",bg="black", font="Times 13 bold").place(x=400, y=300)
        add2 = tkinter.Button(master=root, text="AMERICANO", width=13, command=lambda: self.setModo("AMERICANO"),fg="red", bg="black", font=("Times 13 bold")).place(x=400, y=335)
        add3 = tkinter.Button(master=root, text="FRANCES", width=13, command=lambda: self.setModo("FRANCES"), fg="red",bg="black", font=("Times 13 bold")).place(x=400, y=370)

        add4 = tkinter.Button(master=root, text="UM JOGADOR", width=20, command=lambda: self.setpl(1), fg="red",bg="black", font=("Times 13 bold")).place(x=400, y=450)
        add5 = tkinter.Button(master=root, text="DOIS JOGADORES", width=20, command=lambda: self.setpl(2), fg="red",bg="black", font=("Times 13 bold")).place(x=400, y=485)
        add6 = tkinter.Button(master=root, text="TRES JOGADORES", width=20, command=lambda: self.setpl(3), fg="red",bg="black", font=("Times 13 bold")).place(x=400, y=520)
        add7 = tkinter.Button(master=root, text="QUATRO JOGADORES", width=20, command=lambda: self.setpl(4), fg="red",bg="black", font=("Times 13 bold")).place(x=400, y=555)

        add8 = tkinter.Button(master=root, text="JOGAR", width=20, command=self.jogar, fg="red", bg="black",font=("Times 13 bold")).place(x=1000, y=600)



    def apostas(self):

        ap3 = tkinter.Button(master=root,text="3",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(3)).place(x=568,y=462)
        ap6 = tkinter.Button(master=root,text="6",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(6)).place(x=663,y=462)
        ap9 = tkinter.Button(master=root,text="9",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(9)).place(x=757,y=462)
        ap12 = tkinter.Button(master=root,text="12",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(12)).place(x=855,y=462)
        ap15 = tkinter.Button(master=root,text="15",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(15)).place(x=950,y=462)
        ap18 = tkinter.Button(master=root,text="18",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(18)).place(x=1051,y=462)
        ap21 = tkinter.Button(master=root,text="21",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(21)).place(x=1145,y=462)
        ap24 = tkinter.Button(master=root,text="24",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(24)).place(x=1242,y=462)
        ap27 = tkinter.Button(master=root,text="27",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(27)).place(x=1340,y=462)
        ap30 = tkinter.Button(master=root,text="30",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(30)).place(x=1436,y=462)
        ap33 = tkinter.Button(master=root,text="33",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(33)).place(x=1533,y=462)
        ap36 = tkinter.Button(master=root,text="36",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(36)).place(x=1630,y=462)

        ap2 = tkinter.Button(master=root, text="2", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(2)).place(x=568, y=615)
        ap5 = tkinter.Button(master=root, text="5", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(5)).place(x=663, y=615)
        ap8 = tkinter.Button(master=root, text="8", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(8)).place(x=757, y=615)
        ap11 = tkinter.Button(master=root, text="11", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(11)).place(x=855, y=615)
        ap14 = tkinter.Button(master=root, text="14", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(14)).place(x=950, y=615)
        ap17 = tkinter.Button(master=root, text="17", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(17)).place(x=1051, y=615)
        ap20 = tkinter.Button(master=root, text="20", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(20)).place(x=1145, y=615)
        ap23 = tkinter.Button(master=root, text="23", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(23)).place(x=1242, y=615)
        ap26 = tkinter.Button(master=root, text="25", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(26)).place(x=1340, y=615)
        ap29 = tkinter.Button(master=root, text="29", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(29)).place(x=1436, y=615)
        ap32 = tkinter.Button(master=root, text="32", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(32)).place(x=1533, y=615)
        ap35 = tkinter.Button(master=root, text="35", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(35)).place(x=1630, y=615)

        ap1 = tkinter.Button(master=root, text="1", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(1)).place(x=568, y=769)
        ap4 = tkinter.Button(master=root, text="4", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(4)).place(x=663, y=769)
        ap7 = tkinter.Button(master=root, text="7", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(7)).place(x=757, y=769)
        ap10 = tkinter.Button(master=root, text="10", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(10)).place(x=855, y=769)
        ap13 = tkinter.Button(master=root, text="13", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(13)).place(x=950, y=769)
        ap16 = tkinter.Button(master=root, text="16", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(16)).place(x=1051, y=769)
        ap19 = tkinter.Button(master=root, text="19", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(19)).place(x=1145, y=769)
        ap22 = tkinter.Button(master=root, text="22", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(22)).place(x=1242, y=769)
        ap25 = tkinter.Button(master=root, text="25", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(25)).place(x=1340, y=769)
        ap28 = tkinter.Button(master=root, text="28", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(28)).place(x=1436, y=769)
        ap31 = tkinter.Button(master=root, text="31", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(31)).place(x=1533, y=769)
        ap34 = tkinter.Button(master=root, text="34", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes(34)).place(x=1630, y=769)

        linha1 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes("LINHA3")).place(x=1727, y=462)
        linha2 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes("LINHA2")).place(x=1727, y=615)
        linha3 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes("LINHA1")).place(x=1727, y=769)

        ap1to12 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes("UMST12")).place(x=710, y=830)
        ap2to12 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes("DOISST12")).place(x=1100, y=830)
        ap3to12 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes("TRESST12")).place(x=1490, y=830)

        umto18 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes("UMTO18")).place(x=615, y=900)
        even = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes("EVEN")).place(x=806, y=900)
        red = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes("RED")).place(x=997, y=900)
        black = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes("BLACK")).place(x=1188, y=900)
        odd = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes("ODD")).place(x=1379, y=900)
        dezenoveto36 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold",command=lambda:self.fazerApostaBotoes("DEZNOVETO36")).place(x=1579, y=900)


        um = tkinter.Button(master=root, text="1", width=5, height=0, fg="red", bg="black",font="Times 13 bold",command=lambda:self.fazerAposta(1)).place(x=50, y=750)
        dois = tkinter.Button(master=root, text="2", width=5, height=0, fg="red", bg="black",font="Times 13 bold",command=lambda:self.fazerAposta(2)).place(x=130, y=750)
        tres = tkinter.Button(master=root, text="5", width=5, height=0, fg="red", bg="black",font="Times 13 bold",command=lambda:self.fazerAposta(5)).place(x=210, y=750)
        quatro = tkinter.Button(master=root, text="10", width=5, height=0, fg="red", bg="black",font="Times 13 bold",command=lambda:self.fazerAposta(10)).place(x=50, y=790)
        cinco = tkinter.Button(master=root, text="20", width=5, height=0, fg="red", bg="black",font="Times 13 bold",command=lambda:self.fazerAposta(20)).place(x=130, y=790)
        seis = tkinter.Button(master=root, text="25", width=5, height=0, fg="red", bg="black",font="Times 13 bold",command=lambda:self.fazerAposta(25)).place(x=210, y=790)
        sete = tkinter.Button(master=root, text="50", width=5, height=0, fg="red", bg="black",font="Times 13 bold",command=lambda:self.fazerAposta(50)).place(x=50, y=830)
        oito = tkinter.Button(master=root, text="75", width=5, height=0, fg="red", bg="black",font="Times 13 bold",command=lambda:self.fazerAposta(75)).place(x=130, y=830)
        nove = tkinter.Button(master=root, text="100", width=5, height=0, fg="red", bg="black",font="Times 13 bold",command=lambda:self.fazerAposta(100)).place(x=210, y=830)
        zerar = tkinter.Button(master=root, text="ZERAR", width=5, height=0, fg="red", bg="black",font="Times 13 bold",command=lambda:self.fazerAposta(0)).place(x=130, y=870)

        apostar = tkinter.Button(master=root, text="APOSTAR", width=5, height=0, fg="red", bg="black",font="Times 13 bold",command=lambda:self.setVez()).place(x=130, y=930)
        passar = tkinter.Button(master=root, text="PASSAR", width=5, height=0, fg="red", bg="black",font="Times 13 bold",command=lambda:self.setPassar()).place(x=50, y=930)

        girar = tkinter.Button(master=root, text="GIRAR", width=20, fg="red",bg="black", font="Times 13 bold",command=lambda: self.getNumganhador()).place(x=1530, y=38)

        limparjogadas = tkinter.Button(master=root, text="LIMPAR JOGADAS", width=20, fg="red",bg="black", font="Times 13 bold",command=lambda: self.limparJogada()).place(x=50, y=970)

    def falencia(self,player):
        if player.getTip() <= 0:
            self.__faliram += " | " + player.getNome() + " | "
            self.__players -= 1
            self.__falencia.append(player)
            self.__playersjogando.remove(player)
            self.faliram.configure(text='JOGADORES QUE FALIRAM: {}'.format(self.getFaliram()), font="Times 20 bold", fg="RED", bg="black")

        self.valornatela.configure(text='{}'.format(self.__playersjogando[self.getVez()].getAposta()),font="Times 25 bold", fg="red", bg="black")
        self.jogadordavez.configure(text='{}'.format(self.__playersjogando[self.getVez()].getNome()),font="Times 25 bold", fg="red", bg="black")
        self.jogadortip.configure(text='SEU DINHEIRO: {}'.format(self.__playersjogando[self.getVez()].getTip()),font="Times 25 bold", fg="red", bg="black")
        self.listadejogadas.configure(text='JOGADAS: {}'.format(self.__playersjogando[self.getVez()].getJogadas()),font="Times 25 bold", fg="red", bg="black")

    def getFaliram(self):
        return self.__faliram

    def jogar(self):
        self.setPlayers()
        if self.getPl() != 0:
            self.photo = PhotoImage(file="images/tabela.gif")
            self.backlabel = Label(root, image=self.photo).place(x=-1,y=-1)

            self.apostas()

            self.titulo = tk.Label()
            self.titulo.grid(row=0, column=0)
            self.titulo.configure(text='EUROPEU', font="Times 25 bold",fg="red",bg="black")
            self.titulo.place(x=180,y=5)

            voltar = tkinter.Button(master=root,text="voltar para o menu",width=15,command=self.voltarMenu,fg="red",bg="black",font=("Times 13 bold")).place(x=10,y=10)

            self.valornatela = tk.Label()
            self.valornatela.grid(row=0, column=0)
            self.valornatela.configure(text='{}'.format(self.__playersjogando[self.getVez()].getAposta()), font="Times 25 bold", fg="red", bg="black")
            self.valornatela.place(x=50, y=870)

            self.jogadordavez = tk.Label()
            self.jogadordavez.grid(row=0, column=0)
            self.jogadordavez.configure(text='{}'.format(self.__playersjogando[self.getVez()].getNome()), font="Times 25 bold", fg="red", bg="black")
            self.jogadordavez.place(x=210, y=927)

            self.jogadortip = tk.Label()
            self.jogadortip.grid(row=0, column=0)
            self.jogadortip.configure(text='SEU DINHEIRO: {}'.format(self.__playersjogando[self.getVez()].getTip()), font="Times 25 bold", fg="red", bg="black")
            self.jogadortip.place(x=40, y=700)

            self.listadejogadas = tk.Label()
            self.listadejogadas.grid(row=0, column=0)
            self.listadejogadas.configure(text='JOGADAS: {}'.format(self.__playersjogando[self.getVez()].getJogadas()), font="Times 25 bold", fg="red", bg="black")
            self.listadejogadas.place(x=460, y=400)

            self.numganhador = tk.Label(root)
            self.numganhador.grid(row=0, column=0)
            self.numganhador.configure(text='', font="Times 20 bold",bg="white")
            self.numganhador.place(x=1580, y=170)

            self.clique = tk.Label(root)
            self.clique.grid(row=0, column=0)
            self.clique.configure(text='', font="Times 20 bold", fg="red", bg="black")
            self.clique.place(x=1360, y=38)

            self.bancot = tk.Label()
            self.bancot.grid(row=0, column=0)
            self.bancot.configure(text='DINHEIRO DO BANCO: {}'.format(self.__banco), font="Times 25 bold", fg="red", bg="black")
            self.bancot.place(x=535, y=965)

            self.validade = tk.Label(root)
            self.validade.grid(row=0, column=0)
            self.validade.configure(text='', font="Times 60 bold", fg="yellow", bg="black")
            self.validade.place(x=120, y=100)

            self.faliram = tk.Label(root)
            self.faliram.grid(row=0, column=0)
            self.faliram.configure(text='JOGADORES QUE FALIRAM: {}'.format(self.getFaliram()), font="Times 20 bold", fg="RED", bg="black")
            self.faliram.place(x=1000, y=965)

            self.gameover = tk.Label(root)
            self.gameover.grid(row=0, column=0)
            self.gameover.configure(text='', font="Times 70 bold", fg="RED", bg="black")
            self.gameover.place(x=400, y=400)




root = tk.Tk()
Cassino(root)
root.mainloop()


