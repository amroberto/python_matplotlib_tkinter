# 2 estruture no tkinter um sistema de visualização através do clique, 
# MOSTRE:
#    METRICAS
#    GRAFICO DE BARRAS

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import statistics
from matplotlib.figure import Figure

def calcular_estatistica(lista):
    media = statistics.mean(lista)
    mediana = statistics.median(lista)
    moda = statistics.mode(lista)
    desvio = statistics.stdev(lista)
    varianca = statistics.variance(lista)
    return media, mediana, moda, desvio, varianca

def mostrar_analise():

    pib=[150,300,500,800,150,300,900]   
    estados=['SP','RS','BA','PE','ES','MT','MS']

    media, mediana, moda, desvio, varianca = calcular_estatistica(pib)

    resultado_text = (f'''
                        Media: {media:.2f}
                        Mediana; {mediana:.2f}
                        Moda: {moda:.2f}
                        Desvio padrão: {desvio:.2f}
                        Varianca: {varianca:.2f}
                      ''')
    
    resultado_label.config(text = resultado_text)

    fig = Figure(figsize=(6,4), dpi = 100)
    ax = fig.add_subplot(111)
    ax.set_title('PIB POR ESTADO')
    ax.set_xlabel('ESTADOS')
    ax.set_ylabel('PIB')
    ax.bar(estados, pib)
    ax.grid(True)

    canvas =  FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

root = tk.Tk()
root.title('PIB POR ESTADO')

btn = tk.Button(root, text='Mostrar Gráfico', command=mostrar_analise)
btn.pack(pady=10)

resultado_label = tk.Label(root, text='')
resultado_label.pack(pady=10)

root.mainloop()


