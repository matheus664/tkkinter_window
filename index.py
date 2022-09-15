from cProfile import label
from cgitb import text
from distutils.util import execute
from tkinter import *
import sqlite3 as sq
import tkinter




menu_inicial = Tk()
menu_inicial.title("Metronorte.IO")
menu_inicial.geometry ("500x500+150+150")
menu_inicial.resizable (True,True)
menu_inicial.state ("iconic") #zoomed
menu_inicial.iconbitmap ("images/icone.ico")
menu_inicial ['bg'] = "white"



def btn_click (mensagem):
    print (mensagem)

label_1 = Label (menu_inicial,
                text ="Metronorte.IO\nLogin",
                bg="white",
                fg= "black",
                font="Verdana 20 bold",
                relief="raised", #raised,sunken,solid,ridge
                bd=10,
                width=20,
                padx=10,pady=10)

label_2 = Label (menu_inicial,text="Analise os dados!")

btn = Button (menu_inicial,text= "Enviar",command=lambda: btn_click("NOVA MENSAGEM"))
label_usuario= Label (menu_inicial,text="Usuário:")
label_senha= Label (menu_inicial,text="Senha:")

text_usuario = Entry (menu_inicial)
text_senha = Entry (menu_inicial)



print(text_senha,text_usuario)


label_1.pack()
label_2.pack()
label_usuario.pack(),text_usuario.pack()
label_senha.pack(),text_senha.pack()

text_usuario = Entry.get(text_usuario)
str(text_usuario)
text_senha = Entry.get(text_senha)
str(text_senha)
print(text_senha,text_usuario)

def cadastro_banco () :


    try:
            banco = sq.connect('users.db')
            cursor = banco.cursor()
            cursor.execute("INSERT INTO ger_usuario VALUES ('"+text_usuario+"','"+text_senha+"')")
            banco.commit()
            banco.close()
            print('DADOS INSERIDOS COM SUCESSO')
    except sq.Error as erro:
            print('ERRO AO INSERIR NO BANCO DE DADOS',erro)




btn.pack()
btn1 = Button (menu_inicial,text='Cadastrar',command =lambda: print(text_senha,text_usuario))
btn1.pack()









largura = 500
altura = 500
largura_screen = menu_inicial.winfo_screenwidth()
altura_screen = menu_inicial.winfo_screenheight()
print(largura_screen,altura_screen)
posx =largura_screen/2 - largura/2
posy =altura_screen/2 - altura/2
menu_inicial.geometry ("%dx%d+%d+%d" % (largura,altura, posx,posy))

menu_inicial.mainloop()

















