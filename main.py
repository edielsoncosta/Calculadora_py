#importando tkinter

from tkinter import *
from tkinter import ttk

# cores
cor1 = "#3b3b3b"  # preta
cor2 = "#feffff"  # branca
cor3 = "#38576b"  # azul carregado
cor4 = "#ECEFF1"  # cinzenta
cor5 = "#FFAB40"  # laranja

# Configurando a janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)

# Criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Variável para armazenar os valores
todos_valores = ''

# Variável para atualizar o texto na tela
valor_texto = StringVar()

# Função para entrada de valores
def entrar_valores(valor):
    global todos_valores
    todos_valores += str(valor)
    valor_texto.set(todos_valores)

# Função para calcular o resultado
def calcular():
    global todos_valores
    try:
        resultado = eval(todos_valores)  # Avalia a expressão matemática
        valor_texto.set(str(resultado))
        todos_valores = str(resultado)  # Atualiza a variável com o resultado
    except:
        valor_texto.set("Erro")
        todos_valores = ''

# Função para limpar a tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

# Label para exibição dos valores
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT,
                  anchor="e", justify=RIGHT, font="Ivy 18", bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

# Criando botões
botoes = [
    ("C", limpar_tela, 0, 0, 11),
    ("%", lambda: entrar_valores('%'), 118, 0, 5),
    ("/", lambda: entrar_valores('/'), 177, 0, 5),
    ("7", lambda: entrar_valores('7'), 0, 52, 5),
    ("8", lambda: entrar_valores('8'), 59, 52, 5),
    ("9", lambda: entrar_valores('9'), 118, 52, 5),
    ("*", lambda: entrar_valores('*'), 177, 52, 5),
    ("4", lambda: entrar_valores('4'), 0, 104, 5),
    ("5", lambda: entrar_valores('5'), 59, 104, 5),
    ("6", lambda: entrar_valores('6'), 118, 104, 5),
    ("-", lambda: entrar_valores('-'), 177, 104, 5),
    ("1", lambda: entrar_valores('1'), 0, 156, 5),
    ("2", lambda: entrar_valores('2'), 59, 156, 5),
    ("3", lambda: entrar_valores('3'), 118, 156, 5),
    ("+", lambda: entrar_valores('+'), 177, 156, 5),
    ("0", lambda: entrar_valores('0'), 0, 208, 11),
    (".", lambda: entrar_valores('.'), 118, 208, 5),
    ("=", calcular, 177, 208, 5),
]

for texto, comando, x, y, largura in botoes:
    Button(frame_corpo, command=comando, text=texto, width=largura, height=2, bg=cor4 if texto not in "/*-+=" else cor5,
           fg=cor2 if texto in "/*-+=" else cor1, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=x, y=y)

# Executando o loop da janela
janela.mainloop()
