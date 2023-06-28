import tkinter as tk
from tkinter import messagebox

def criar_botoes(imagens):
    botoes = []
    for linha in range(6):
        botoes_linha = []
        for coluna in range(4):
            comando = lambda l=linha, c=coluna:(l, c)
            botao = tk.Button(frame_botoes,
                image=imagens[(linha, coluna)],
                width=45, height=45, cursor='hand2', 
                command=comando)
            botao.grid(row=linha, column=coluna)
            botoes_linha.append(botao)

        botoes.append(botoes_linha)
    return botoes    

janela = tk.Tk()
janela.title('Calculadora')
janela.config(padx=10, pady=10, background='#fff')
janela.resizable(False, False)

def janela_visor(root):
    visor = tk.Entry(root)
    visor.grid(row=1, columnspan=0, pady=(0, 10))
    visor.config(
        font=('helvetica', 40,'bold'),
        justify='right'
    )
visor = tk.Entry(janela, width=25, font=('Arial', 14), justify=tk.RIGHT)
visor.pack(pady=10)


imagens = {
    #  tk.PhotoImage(file='button_.png'),
    (0, 0): tk.PhotoImage(file='button_+-.png'),
    (0, 1): tk.PhotoImage(file='button_-.png'),
    (0, 2): tk.PhotoImage(file='button_+.png'),
    (0, 3): tk.PhotoImage(file='button_=.png'),
    (1, 0): tk.PhotoImage(file='button_0.png'),
    (1, 1): tk.PhotoImage(file='button_-.png'),
    (1, 2): tk.PhotoImage(file='button_1.png'),
    (1, 3): tk.PhotoImage(file='button_1x.png'),
    (2, 0): tk.PhotoImage(file='button_2.png'),
    (2, 1): tk.PhotoImage(file='button_3.png'),
    (2, 2): tk.PhotoImage(file='button_4.png'),
    (2, 3): tk.PhotoImage(file='button_5.png'),
    (3, 0): tk.PhotoImage(file='button_6.png'),
    (3, 1): tk.PhotoImage(file='button_7.png'),
    (3, 2): tk.PhotoImage(file='button_8.png'),
    (3, 3): tk.PhotoImage(file='button_9.png'),
    (4, 0): tk.PhotoImage(file='button_back.png'),
    (4, 1): tk.PhotoImage(file='button_c.png'),
    (4, 2): tk.PhotoImage(file='button_ce.png'),
    (4, 3): tk.PhotoImage(file='button_div.png'),
    (5, 0): tk.PhotoImage(file='button_dot.png'),
    (5, 1): tk.PhotoImage(file='button_m-.png'),
    (5, 2): tk.PhotoImage(file='button_m+.png'),
    (5, 3): tk.PhotoImage(file='button_mc.png')
    # 'b': tk.PhotoImage(file='button_.png'),
    # '+-' tk.PhotoImage(file='button_+-.png'),
    # '-': tk.PhotoImage(file='button_-.png'),
    # '+': tk.PhotoImage(file='button_+.png'),
    # '=': tk.PhotoImage(file='button_=.png'),
    # '0': tk.PhotoImage(file='button_0.png'),
    # '-': tk.PhotoImage(file='button_-.png'),
    # '1': tk.PhotoImage(file='button_1.png'),
    # '1x': tk.PhotoImage(file='button_1x.png'),
    # '2': tk.PhotoImage(file='button_2.png'),
    # '3': tk.PhotoImage(file='button_3.png'),
    # '4': tk.PhotoImage(file='button_4.png'),
    # '5': tk.PhotoImage(file='button_5.png'),
    # '6': tk.PhotoImage(file='button_6.png'),
    # '7': tk.PhotoImage(file='button_7.png'),
    # '8': tk.PhotoImage(file='button_8.png'),
    # '9': tk.PhotoImage(file='button_9.png'),
    # 'back': tk.PhotoImage(file='button_back.png'),
    # 'c': tk.PhotoImage(file='button_c.png'),
    # 'ce': tk.PhotoImage(file='button_ce.png'),
    # 'div': tk.PhotoImage(file='button_div.png'),
    # 'dot': tk.PhotoImage(file='button_dot.png'),
    # 'm-': tk.PhotoImage(file='button_m-.png'),
    # 'm+': tk.PhotoImage(file='button_m+.png'),
    # 'mc': tk.PhotoImage(file='button_mc.png'),
    # 'mr': tk.PhotoImage(file='button_mr.png'),
    # 'ms': tk.PhotoImage(file='button_ms.png'),
    # 'mul': tk.PhotoImage(file='button_mul.png'),
    # 'rx': tk.PhotoImage(file='button_rx.png'),
    # 'x2': tk.PhotoImage(file='button_x2.png')
    
}

janela.wm_iconphoto(True, imagens[(0,0)])

frame_botoes = tk.Frame(janela)
frame_botoes.pack(padx=45, pady=45)
buttons = criar_botoes(imagens)

janela.mainloop()

# imagenb = tk.PhotoImage(file='button_.png'),
# imagena =tk.PhotoImage(file='button_-.png'),
# rotulo1 = tk.Label(janela, image=imagenb)
# rotulo2 = tk.Label(janela, image=imagena)
# rotulo3 = tk.Label(janela, text="C",
# fg="white", bg="green")
# rotulo4 = tk.Label(janela, text="D",
# fg="white", bg="blue")
# rotulo5 = tk.Label(janela, text="C",
# fg="white", bg="green")
# rotulo6 = tk.Label(janela, text="D",
# fg="white", bg="blue")
# rotulo7 = tk.Label(janela, text="C",
# fg="white", bg="green")
# rotulo8 = tk.Label(janela, text="D",
# fg="white", bg="blue")
# rotulo9 = tk.Label(janela, text="C",
# fg="white", bg="green")
# rotulo10 = tk.Label(janela, text="D",
# fg="white", bg="blue")
# rotulo11 = tk.Label(janela, text="C",
# fg="white", bg="green")
# rotulo12 = tk.Label(janela, text="D",
# fg="white", bg="blue")
# rotulo1.pack()
# rotulo1.grid(row=0, column=0)
# rotulo2.grid(row=0, column=1)
# rotulo3.grid(row=0, column=2)
# rotulo4.grid(row=0, column=3)
# rotulo5.grid(row=1, column=0)
# rotulo6.grid(row=1, column=1)
# rotulo7.grid(row=1, column=2)
# rotulo8.grid(row=1, column=3)
# rotulo9.grid(row=2, column=0)
# rotulo10.grid(row=2, column=1)
# rotulo11.grid(row=2, column=2)
# rotulo12.grid(row=2, column=3)
