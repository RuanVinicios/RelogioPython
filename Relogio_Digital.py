import tkinter as tk
from time import strftime

# Feita importação da biblioteca tkinter com uso alias(as) para facilitar o chamamento.
# Strftime para formatar a hora de acordo com o padrão especificado.

janela =  tk.Tk()
janela.title('Relógio Digital')
janela.geometry('250x100')

# linha 7 - é criado uma instância chamado janela para utilizar as funções do método TK()
# linha 8 - método title para inserir o título  da interface
# linha 9 - método geometry() é usado para ajustar o tamanho da tela

def time_clock():
    relogio = strftime('%H:%M:%S %p')
    label.config(text = relogio)
    label.after(1000, time_clock)

# time_clock é um método que retorna um valor flutuante do tempo atual do processador em segundos.
# é criado uma variável(relogio) e atribuída o método strftime com as seguintes especificações
# %H - horas, %M - minutos, %S - segundos e o %p - AM ou PM         
# label.config vai mostrar na tela todas as especificações atribuídas na variável relogio
# label.after vai atualizar o relogio a cada 1000ms
    
label = tk.Label(janela, font=('Arial', 24), background = 'black', foreground='orange')
label.pack(anchor='center', pady=30)

# tk.label especifica como vai ser janela do programa
# label.pack usado para colocar relogio centralizado na janela

time_clock()
janela.mainloop()

# é feito o chamamento time_clock() na linha 32 
# mainloop deixar a GUI aberta esperando pelo acontecimento de eventos. 
