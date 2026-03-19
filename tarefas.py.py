import tkinter as tk
from tkinter import messagebox

# ===== FUNÇÕES =====
def salvar_tarefas():
    with open("tarefas.txt", "w") as arquivo:
        for t in tarefas:
            arquivo.write(t + "\n")


def carregar_tarefas():
    try:
        with open("tarefas.txt", "r") as arquivo:
            return [linha.strip() for linha in arquivo if linha.strip() != ""]
    except:
        return []


def atualizar_lista():
    lista.delete(0, tk.END)
    for t in tarefas:
        lista.insert(tk.END, t)

    total = len(tarefas)

    if total == 0:
        contador.config(text="Nenhuma tarefa", fg="red")
    else:
        contador.config(text=f"Total de tarefas: {total}", fg="lightgreen")


def adicionar():
    tarefa = entrada.get().strip()

    if tarefa == "":
        messagebox.showwarning("Erro", "Digite uma tarefa!")
        return

    tarefas.append(tarefa)
    salvar_tarefas()
    atualizar_lista()
    entrada.delete(0, tk.END)


def remover():
    selecionado = lista.curselection()

    if not selecionado:
        messagebox.showwarning("Erro", "Selecione uma tarefa!")
        return

    index = selecionado[0]
    tarefas.pop(index)
    salvar_tarefas()
    atualizar_lista()


def editar():
    selecionado = lista.curselection()

    if not selecionado:
        messagebox.showwarning("Erro", "Selecione uma tarefa!")
        return

    index = selecionado[0]

    # joga texto antigo na caixa
    entrada.delete(0, tk.END)
    entrada.insert(0, tarefas[index])

    nova = entrada.get().strip()

    if nova == "":
        messagebox.showwarning("Erro", "Digite o novo texto!")
        return

    tarefas[index] = nova
    salvar_tarefas()
    atualizar_lista()
    entrada.delete(0, tk.END)


def limpar_tudo():
    confirm = messagebox.askyesno("Confirmação", "Deseja apagar tudo?")

    if confirm:
        tarefas.clear()
        salvar_tarefas()
        atualizar_lista()


# ===== DADOS =====
tarefas = carregar_tarefas()

# ===== JANELA =====
janela = tk.Tk()
janela.title("Lista de Tarefas")
janela.geometry("350x450")
janela.configure(bg="#1e1e1e")

# ===== COMPONENTES =====
titulo = tk.Label(janela, text="📋 Lista de Tarefas", bg="#1e1e1e", fg="white", font=("Arial", 14))
titulo.pack(pady=10)

entrada = tk.Entry(janela, font=("Arial", 12))
entrada.pack(pady=10, padx=10, fill="x")

entrada.bind("<Return>", lambda event: adicionar())

frame_botoes = tk.Frame(janela, bg="#1e1e1e")
frame_botoes.pack(pady=5)

tk.Button(frame_botoes, text="Adicionar", command=adicionar).grid(row=0, column=0, padx=5)
tk.Button(frame_botoes, text="Editar", command=editar).grid(row=0, column=1, padx=5)
tk.Button(frame_botoes, text="Remover", command=remover).grid(row=0, column=2, padx=5)

lista = tk.Listbox(janela, font=("Arial", 12))
lista.pack(expand=True, fill="both", padx=10, pady=10)

contador = tk.Label(janela, text="", bg="#1e1e1e", fg="white", font=("Arial", 10))
contador.pack()

tk.Button(janela, text="🗑 Limpar Tudo", command=limpar_tudo).pack(pady=5)

# ===== INICIAR =====
atualizar_lista()
janela.mainloop()
