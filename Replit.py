import tkinter as tk
from tkinter import messagebox

def validar_renda(renda_entry):
    renda = renda_entry.get()
    try:
        renda = float(renda)
        if 1000 <= renda <= 100000:
            return renda
        else:
            messagebox.showerror("Erro", "Sua renda deve estar entre R$1000 e R$100000.")
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido, insira um valor numérico válido.")

def calcular_emprestimo(renda_entry, valor_entry, prazo_entry, resultado_text):
    renda = validar_renda(renda_entry)

    if renda is not None:
        valor_emprestimo = valor_entry.get()

        try:
            valor_emprestimo = float(valor_emprestimo)

            limite_emprestimo = renda * 5  
            limite_prestacao = renda * 0.3  

            if valor_emprestimo > limite_emprestimo:
                messagebox.showerror("Erro", f"O valor do empréstimo não pode ser superior a R${limite_emprestimo:.2f}")
            else:
                prazo_meses = prazo_entry.get()

                try:
                    prazo_meses = int(prazo_meses)

                    limite_prazo = 60  # 5 anos
                  
                    if prazo_meses > limite_prazo:
                        messagebox.showerror("Erro", "A quantidade de parcelas não pode exceder 60.")
                    else:
                        
                        taxa_juros = 0.1  # 10% de juros
                        
                        juros_total = 0
                        for i in range(prazo_meses):
                            juros = valor_emprestimo * taxa_juros
                            juros_total += juros
                            valor_emprestimo -= (valor_emprestimo * taxa_juros)
                       
                        prestacao = (juros_total + float(valor_entry.get())) / prazo_meses

                        resultado_text.config(text=f"Valor das parcelas: R${prestacao:.2f}\n"
                                                   f"Valor Total do Empréstimo: R${prestacao * prazo_meses:.2f}\n"
                                                   f"Total de Juros: R${juros_total:.2f}")
                except ValueError:
                    messagebox.showerror("Erro", "Valor inválido, insira um valor numérico válido.")
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido, insira um valor numérico válido.")

def main():
    root = tk.Tk()
    root.title("BRB")

    renda_label = tk.Label(root, text="Informa sua renda")
    renda_label.pack()

    renda_entry = tk.Entry(root)
    renda_entry.pack()

    valor_label = tk.Label(root, text="Valor do empréstimo desejado")
    valor_label.pack()

    valor_entry = tk.Entry(root)
    valor_entry.pack()

    prazo_label = tk.Label(root, text="Parcelas")
    prazo_label.pack()

    prazo_entry = tk.Entry(root)
    prazo_entry.pack()

    resultado_text = tk.Label(root, text="")
    resultado_text.pack()

    calcular_button = tk.Button(root, text="Calcular Empréstimo", command=lambda: calcular_emprestimo(renda_entry, valor_entry, prazo_entry, resultado_text))
    calcular_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
