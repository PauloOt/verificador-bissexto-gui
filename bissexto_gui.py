import tkinter as tk
from tkinter import messagebox

def verificar_ano():
    ano = entry_ano.get()
    if not ano.isdigit():
        messagebox.showerror("Erro", "Digite um ano válido (número inteiro).")
        return

    ano = int(ano)
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        resultado = f"{ano} é um ano bissexto!"
    else:
        resultado = f"{ano} não é um ano bissexto."

    messagebox.showinfo("Resultado", resultado)

# Interface gráfica com estilo
janela = tk.Tk()
janela.title("Verificador de Ano Bissexto")
janela.geometry("350x200")
janela.configure(bg="#f0f0f0")  # Cor de fundo da janela

# Fonte padrão
fonte_padrao = ("Arial", 12)

# Label estilizado
label_instrucao = tk.Label(janela, text="Digite um ano:", font=fonte_padrao, bg="#f0f0f0", fg="#333")
label_instrucao.pack(pady=10)

# Campo de entrada
entry_ano = tk.Entry(janela, width=20, font=fonte_padrao, justify='center')
entry_ano.pack(pady=5)

# Botão estilizado
botao_verificar = tk.Button(
    janela,
    text="Verificar",
    command=verificar_ano,
    font=("Arial", 11, "bold"),
    bg="#09EB4D",
    fg="white",
    activebackground="#09EB4D",
    padx=10,
    pady=5,
    relief="raised",
    bd=2
)
botao_verificar.pack(pady=15)

janela.mainloop()
