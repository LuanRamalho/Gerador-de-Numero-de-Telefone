import tkinter as tk
import random

def gerar_numero_telefone():
    # Gera números de 11 a 99 para o DDD
    ddd = random.randint(11, 99)
    # Gera números de 90000 a 99999 para o número
    numero = random.randint(90000, 99999)
    # Formata o número no formato (XX)XXXXX-XXXX
    numero_telefone = f"({ddd}){numero:05d}-{random.randint(1000, 9999)}"
    label_numero.config(text=numero_telefone)

# Cria a janela principal
root = tk.Tk()
root.title("Gerador de Números de Telefone")
root.geometry("300x150")
root.configure(bg="#e0f7fa")  # Cor de fundo bem colorida

# Adiciona uma label para mostrar o número gerado
label_numero = tk.Label(root, text="Clique no botão para gerar um número", font=("Helvetica", 12), bg="#e0f7fa")
label_numero.pack(pady=20)

# Adiciona o botão para gerar números
botao_gerar = tk.Button(root, text="Gerar Número", command=gerar_numero_telefone, bg="#00796b", fg="white", font=("Helvetica", 12))
botao_gerar.pack(pady=10)

# Inicia a aplicação
root.mainloop()
