import tkinter as tk
from tkinter import ttk

# Função para configurar a janela maximizada
def configurar_janela_maximizada(janela):
    janela.state('zoomed')  # Maximiza a janela ao abrir

def abrir_primeira_janela():
    janela1 = tk.Tk()
    janela1.title("Primeira Janela")
    configurar_janela_maximizada(janela1)  # Configura para abrir maximizada

    rotulo = ttk.Label(janela1, text="Esta é a primeira janela")
    rotulo.grid(row=0, column=0, padx=10, pady=10)
    texto = ttk.Label(janela1, text="informações do paciente")
    texto.grid(row=0, column=1, padx=50, pady=50)

    botao_abrir = ttk.Button(janela1, text="Abrir Segunda Janela", command=lambda: abrir_segunda_janela(janela1))
    botao_abrir.grid(row=1, column=0, padx=10, pady=10)

    janela1.mainloop()

def abrir_segunda_janela(janela_anterior):
    janela_anterior.destroy()
    segunda_janela = tk.Tk()
    segunda_janela.title("Segunda Janela")
    configurar_janela_maximizada(segunda_janela)

    rotulo = ttk.Label(segunda_janela, text="Esta é a segunda janela")
    rotulo.grid(row=0, column=0, padx=10, pady=10)

    botao_proxima = ttk.Button(segunda_janela, text="Abrir Terceira Janela", command=lambda: abrir_terceira_janela(segunda_janela))
    botao_proxima.grid(row=1, column=0, padx=10, pady=10)

    segunda_janela.mainloop()

def abrir_terceira_janela(janela_anterior):
    janela_anterior.destroy()
    terceira_janela = tk.Tk()
    terceira_janela.title("Terceira Janela")
    configurar_janela_maximizada(terceira_janela)

    rotulo = ttk.Label(terceira_janela, text="Esta é a terceira janela")
    rotulo.grid(row=0, column=0, padx=10, pady=10)

    botao_fechar = ttk.Button(terceira_janela, text="Fechar", command=terceira_janela.destroy)
    botao_fechar.grid(row=1, column=0, padx=10, pady=10)

    terceira_janela.mainloop()


def janelinha():
    segunda_janela = tk.Tk()
    segunda_janela.title("Segunda Janela")
    configurar_janela_maximizada(segunda_janela)

    rotulo = ttk.Label(segunda_janela, text="Esta é a segunda janela")
    rotulo.grid(row=0, column=0, padx=10, pady=10)

    botao_proxima = ttk.Button(segunda_janela, text="Abrir Terceira Janela", command=lambda: abrir_terceira_janela(segunda_janela))
    botao_proxima.grid(row=1, column=0, padx=10, pady=10)

    segunda_janela.mainloop()