'''
Este modulo apenas gera a interface grafica e utiliza as funçoes do modo criptografia
'''

import criptografia

from tkinter import *
import tkinter as tk
import tkinter.scrolledtext as tkscrolled


class App(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.CriarElementosDaInterface()

    def CriarElementosDaInterface(self):
        
        self.masterContainer = Frame(self,bg='white')
        self.masterContainer.grid(row="1", column="1")

        self.containerKey = Frame(self.masterContainer,bg='white')
        self.containerKey.grid(row="2", column="1", columnspan="2", pady=20)
        

        self.botaoCriptografar = Button(
            self.masterContainer, text="CRIPTOGRAFAR", font=("Courier New", "12", 'bold'))
        self.botaoCriptografar.grid(row="5", column="1", pady=20)
        self.botaoCriptografar["command"] = self.criptografa

        self.botaoDescriptografar = Button(
            self.masterContainer, text="DESCRIPTOGRAFAR", font=("Courier New", "12", 'bold'))
        self.botaoDescriptografar.grid(row="5", column="2", pady=20)
        self.botaoDescriptografar["command"] = self.descriptografa

        self.imagem = tk.PhotoImage(file="ifgLogo.png")
        self.titulo = Label(self.masterContainer, image=self.imagem,bg='white')
        self.titulo.grid(row="1", column="1", columnspan="2", padx=20, pady=20)

        self.labelKey = Label(
            self.containerKey, text="CHAVE: ", font=("Courier New", "12"),bg='white')
        self.labelKey.grid(row="1", column="1")

        self.entryKey = Entry(self.containerKey, width="48",borderwidth=2, relief="groove")
        self.entryKey.grid(row="1", column="2")

        self.labelTextoNormal = Label( self.masterContainer, text="MENSAGEM DESCRIPTOGRAFADA: ", font=("Courier New", "12"),bg='white')
        self.labelTextoNormal.grid(row="3", column="1")

        self.textoNormal =  tkscrolled.ScrolledText(self.masterContainer, width=60, height=20,borderwidth=2, relief="groove")
        self.textoNormal.grid(row="4", column="1", padx=10)

        self.labelTextoNormal = Label( self.masterContainer, text="MENSAGEM CRIPTOGRAFADA: ", font=("Courier New", "12"),bg='white')
        self.labelTextoNormal.grid(row="3", column="2")

        self.textoCriptografado =  tkscrolled.ScrolledText(self.masterContainer, width=60, height=20,borderwidth=2, relief="groove")
        self.textoCriptografado.grid(row="4", column="2")

    def criptografa(self):
        content = (self.textoNormal.get("1.0", END))
        key = (self.entryKey.get())
        mensagemCriptografada = criptografia.crypt(content, key)
        self.textoCriptografado.delete('1.0', END)
        self.textoCriptografado.insert('1.0', mensagemCriptografada)

    def descriptografa(self):
        try:
            content = (self.textoCriptografado.get("1.0", END))
            key = (self.entryKey.get())
            mensagemDescriptografada = criptografia.decrypt(content, key)
            self.textoNormal.delete('1.0', END)
            self.textoNormal.insert('1.0', mensagemDescriptografada)
        except:
            self.textoNormal.delete('1.0', END)
            self.textoNormal.insert('1.0', 'Está nao é uma mensagem criptografada utilizando o nosso algoritmo ')



root = tk.Tk()
app = App(master=root) 
app.master.title("IFG-Criptografia") 
app.master.maxsize(1024, 700)
app.master.minsize(1024, 700)
app.master.geometry("1024x900")
root.configure(background='white')
app.mainloop() 
