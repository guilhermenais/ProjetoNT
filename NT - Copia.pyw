import tkinter as tk
from tkinter import scrolledtext
import re

# Função para substituir quebras de linha por tags <br>
def adicionar_quebras_linha(texto):
        return texto.replace('\n', '<br>')

# Função para deixar o texto em negrito entre aspas duplas
def adicionar_negrito(texto):
    return re.sub(r'"([^"]*)"', r'<strong>\1</strong>', texto)

# Função para copiar o texto
def copiar_texto():
    janela.clipboard_clear()
    janela.clipboard_append(saida_texto.get('1.0', tk.END))
    janela.update()

def formatar_texto():
    resumo = entrada_resumo.get("1.0", tk.END).strip()
    detalhes = entrada_detalhes.get("1.0", tk.END).strip()
    questoes = entrada_questoes.get("1.0", tk.END).strip()
    parametros = entrada_parametros.get("1.0", tk.END).strip()

    # Aplicar formatação
    resumo = adicionar_quebras_linha(resumo)
    detalhes = adicionar_quebras_linha(detalhes)
    questoes = adicionar_quebras_linha(questoes)
    parametros = adicionar_quebras_linha(parametros)
    
    texto_formatado = f"""<h4><strong>Resumo da Nota Técnica</strong></h4>
<p>{adicionar_negrito(resumo)}</p>
<h4><strong>Detalhes da Nota Técnica</strong></h4>
<p>{adicionar_negrito(detalhes)}</p>
<p><strong><strong>Questões:</strong><br></strong></p>
<p>{adicionar_negrito(questoes)}</p>
<h4><strong>Parâmetros Envolvidos</strong></h4>
<p>{adicionar_negrito(parametros)}</p>
"""
    saida_texto.config(state='normal') 
    saida_texto.delete("1.0", tk.END)
    saida_texto.insert(tk.END, texto_formatado)
    saida_texto.config(state='disabled')

# Criar janela principal
janela = tk.Tk()
janela.title("Formatador de Texto HTML para Notas Técnicas")

# Configurar janela para tela cheia em modo janela
janela.state('zoomed')
janela.resizable(False, False)

# Ajustar responsividade
janela.grid_columnconfigure(0, weight=1)
janela.grid_rowconfigure(0, weight=1)

# Criar frame principal para organizar os widgets
frame_principal = tk.Frame(janela)
frame_principal.grid(sticky='nsew', padx=20, pady=20)

# Ajustar responsividade do frame
frame_principal.grid_columnconfigure(0, weight=1)

# Criar áreas de entrada de texto
tk.Label(frame_principal, text="Resumo da Nota Técnica:").grid(row=0, column=0, pady=5, sticky='w')
entrada_resumo = scrolledtext.ScrolledText(frame_principal, width=80, height=5)
entrada_resumo.grid(row=1, column=0, padx=10, pady=5, sticky='nsew')

tk.Label(frame_principal, text="Detalhes da Nota Técnica:").grid(row=2, column=0, pady=5, sticky='w')
entrada_detalhes = scrolledtext.ScrolledText(frame_principal, width=80, height=10)
entrada_detalhes.grid(row=3, column=0, padx=10, pady=5, sticky='nsew')

tk.Label(frame_principal, text="Questões:").grid(row=4, column=0, pady=5, sticky='w')
entrada_questoes = scrolledtext.ScrolledText(frame_principal, width=80, height=5)
entrada_questoes.grid(row=5, column=0, padx=10, pady=5, sticky='nsew')

tk.Label(frame_principal, text="Parâmetros Envolvidos:").grid(row=6, column=0, pady=5, sticky='w')
entrada_parametros = scrolledtext.ScrolledText(frame_principal, width=80, height=3)
entrada_parametros.grid(row=7, column=0, padx=10, pady=5, sticky='nsew')

# Criar botão para formatar
botao_formatar = tk.Button(frame_principal, text="Formatar Texto", command=formatar_texto)
botao_formatar.grid(row=8, column=0, pady=10)

# Criar área de saída de texto
saida_texto = scrolledtext.ScrolledText(frame_principal, width=80, height=20)
saida_texto.grid(row=9, column=0, padx=10, pady=10, sticky='nsew')
saida_texto.config(state='disabled') 

# Criar botão para copiar o texto
botao_copiar = tk.Button(frame_principal, text="Copiar Texto", command=copiar_texto)
botao_copiar.grid(row=10, column=0, pady=5)

# Ajustar redimensionamento dos widgets
for i in range(1, 11, 2):
    frame_principal.grid_rowconfigure(i, weight=1)

# Iniciar loop da interface gráfica
janela.mainloop()
