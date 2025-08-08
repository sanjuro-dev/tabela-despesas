import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import font

import pandas as pd
from datetime import datetime
import os

import matplotlib.pyplot as plt
import numpy as np


def soma_categoria(categoria, dados):
    soma = 0
    for item in dados:
        if item["Categoria"] == categoria and item["Data"].month == datetime.now().month and item["Data"].year == datetime.now().year:


            soma += item["Valor"]
    return soma

def soma_mensal(mes, dados):
    soma = 0
    for item in dados:
        if item["Data"].month == mes and item["Data"].year == datetime.now().year:

            soma += item["Valor"]
    return soma



def adicionar_despesa():

    # Validar campos
    if not entry_valor.get() or not combobox.get():
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return


    categoria = combobox.get()
    descricao = entry_descricao.get()
    try:
        valor = float(entry_valor.get().replace(",", "."))	
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido. Digite um número inteiro.")
        return

    df = pd.read_excel("planilha.xlsx")

    data = pd.to_datetime(datetime.now().date())

    novo_item = {
        "Categoria": categoria,
        "Descrição": descricao,
        "Valor": valor,
        "Data": data            
    }

    df = pd.concat([df, pd.DataFrame([novo_item])], ignore_index=True)
    df['Data'] = pd.to_datetime(df['Data'])
    df.to_excel("planilha.xlsx", index=False)

    entry_descricao.delete(0, END)
    entry_valor.delete(0, END)


    messagebox.showinfo("Sucesso", "Despesa adicionada com sucesso!")

    return None

def gerar_dados():
    df = pd.read_excel("planilha.xlsx")

    opcoes = ["Luz", "Wi-Fi", "Transporte", "Comida", "Lazer"]
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    valores = list()
    mensal = list()

    for o in opcoes:
        soma = soma_categoria(o, df.to_dict(orient="records"))
        valores.append(soma)
    
    for m in range(12):
        soma = soma_mensal(m+1, df.to_dict(orient="records"))
        mensal.append(soma)


    


    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    # Gráfico de pizza
    axs[0].pie(valores, labels=opcoes, autopct='%1.1f%%', startangle=140)

    axs[0].set_title('Distribuição dos Gastos (%)')
    axs[0].axis('equal')

    # Gráfico de barras
    axs[1].bar(meses, mensal)

    axs[1].set_title('Gastos Mensais (R$)')
    axs[1].set_ylabel('Valor (R$)')
    axs[1].set_xticklabels(meses, rotation=45)

    # Exibir os gráficos
    plt.tight_layout()
    plt.show()

            

if not os.path.exists("planilha.xlsx"):
    df = pd.DataFrame(columns=["Categoria", "Descrição", "Valor", "Data"])
    df.to_excel("planilha.xlsx", index=False)


root = tk.Tk()
root.title("Tabela de Despesas")
root.geometry("600x300")
root.resizable(False, False)

font.Font(family="Helvetica", size=25)
root.option_add("*Font", "Helvetica 25")
root.configure(bg="#f0f0f0")

style = ttk.Style()
style.theme_use("clam")  # ou "default", "alt", "vista", "xpnative"
style.configure("TButton",relief="flat" ,background="#4CAF50", foreground="white", font="Helvetica 25", padding=6)

style.configure("TLabel", font="Helvetica 25")
style.configure("TEntry", font="Helvetica 25")


# Categoria
lb_categoria = tk.Label(root, text="Categoria")
lb_categoria.grid(row=0, column=0, padx=10, pady=10)


opcoes = ["Luz", "Wi-Fi", "Transporte", "Comida", "Lazer"]
combobox = ttk.Combobox(root, values=opcoes)
combobox.grid(row=0, column=1, padx=10, pady=10)

lb_descricao = tk.Label(root, text="Descrição")
lb_descricao.grid(row=1, column=0, padx=10, pady=10)

entry_descricao = tk.Entry(root)
entry_descricao.grid(row=1, column=1, padx=10, pady=10)

lb_valor = tk.Label(root, text="Valor R$")
lb_valor.grid(row=2, column=0, padx=10, pady=10)

entry_valor = tk.Entry(root)
entry_valor.grid(row=2, column=1, padx=10, pady=10)


# Botão
btn_adicionar = tk.Button(root, text="Adicionar", command=adicionar_despesa)
btn_adicionar.grid(row=3, column=0, padx=10, pady=10)

btn_adicionar = tk.Button(root, text="Gerar Dados", command=gerar_dados)
btn_adicionar.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()



