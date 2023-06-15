import tkinter as tk
from tkinter import messagebox

def criar_botoes():
    botoes = []
    for linha in range(6):
        botoes_linha = []
        for coluna in range(4):

            comando = lambda l=linha, c=coluna:(l, c)
            botao = tk.Button(frame_botoes,
                width=9, height=4, cursor='hand2', command=comando)
            botao.grid(row=linha, column=coluna)
            botoes_linha.append(botao)

        botoes.append(botoes_linha)
    return botoes    
janela = tk.Tk()
janela.title('Calculadora')
janela.resizable(False, False)


imagens = {
    'b': tk.PhotoImage(file='button_.png'),
    '-': tk.PhotoImage(file='button_-.png'),
    '+': tk.PhotoImage(file='button_+.png'),
    '=': tk.PhotoImage(file='button_=.png'),
    '0': tk.PhotoImage(file='button_0.png'),
    '-': tk.PhotoImage(file='button_-.png'),
    '1': tk.PhotoImage(file='button_1.png'),
    '1x': tk.PhotoImage(file='button_1x.png'),
    '2': tk.PhotoImage(file='button_2.png'),
    '3': tk.PhotoImage(file='button_3.png'),
    '4': tk.PhotoImage(file='button_4.png'),
    '5': tk.PhotoImage(file='button_5.png'),
    '6': tk.PhotoImage(file='button_6.png'),
    '7': tk.PhotoImage(file='button_7.png'),
    '8': tk.PhotoImage(file='button_8.png'),
    '9': tk.PhotoImage(file='button_9.png'),
    'back': tk.PhotoImage(file='button_back.png'),
    'c': tk.PhotoImage(file='button_c.png'),
    'ce': tk.PhotoImage(file='button_ce.png'),
    'div': tk.PhotoImage(file='button_div.png'),
    'dot': tk.PhotoImage(file='button_dot.png'),
    'm-': tk.PhotoImage(file='button_m-.png'),
    'm+': tk.PhotoImage(file='button_m+.png'),
    'mc': tk.PhotoImage(file='button_mc.png'),
    'mr': tk.PhotoImage(file='button_mr.png'),
    'ms': tk.PhotoImage(file='button_ms.png'),
    'mul': tk.PhotoImage(file='button_mul.png'),
    'rx': tk.PhotoImage(file='button_rx.png'),
    'x2': tk.PhotoImage(file='button_x2.png'),
    
}

janela.wm_iconphoto(True, imagens['b'])

frame_botoes = tk.Frame(janela)
frame_botoes.pack(padx=15, pady=15)
buttons = criar_botoes()

janela.mainloop()
