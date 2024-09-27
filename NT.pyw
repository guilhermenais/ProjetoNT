import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk  # Para o Notebook (abas)
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

# Função para formatar o texto
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

# Função para integração com Gemini IA (exemplo simples)
def consultar_gemini():
    pergunta = entrada_gemini.get("1.0", tk.END).strip()
    # Aqui você faria a chamada à API do Gemini IA com a pergunta
    resposta = f"Simulação de resposta da Gemini IA para: '{pergunta}'"  # Simulando resposta
    saida_gemini.config(state='normal')
    saida_gemini.delete("1.0", tk.END)
    saida_gemini.insert(tk.END, resposta)
    saida_gemini.config(state='disabled')

# Criar janela principal
janela = tk.Tk()
janela.title("Formatador de Texto HTML para Notas Técnicas")

# Desabilitar maximizar e redimensionar a janela
janela.resizable(False, False)

# Iniciar a aplicação em modo tela cheia em janela
janela.state('zoomed')

# Criar Notebook para abas
notebook = ttk.Notebook(janela)
notebook.pack(fill='both', expand=True)

# Aba 1: Formatar texto HTML
aba_formatador = ttk.Frame(notebook)
notebook.add(aba_formatador, text="Formatador de Texto")

# Aba 2: Integração com Gemini IA
aba_gemini = ttk.Frame(notebook)
notebook.add(aba_gemini, text="Gemini IA")

# Frame principal da aba 1 (Formatador)
frame_principal = tk.Frame(aba_formatador)
frame_principal.grid(sticky='nsew', padx=20, pady=20)

# Ajustar responsividade do frame
aba_formatador.grid_columnconfigure(0, weight=1)
aba_formatador.grid_rowconfigure(0, weight=1)

# Criar áreas de entrada de texto
tk.Label(frame_principal, text="Resumo da Nota Técnica:").grid(row=0, column=0, pady=5, sticky='w')
entrada_resumo = scrolledtext.ScrolledText(frame_principal, wrap=tk.WORD)
entrada_resumo.grid(row=1, column=0, padx=10, pady=5, sticky='nsew')

tk.Label(frame_principal, text="Detalhes da Nota Técnica:").grid(row=2, column=0, pady=5, sticky='w')
entrada_detalhes = scrolledtext.ScrolledText(frame_principal, wrap=tk.WORD)
entrada_detalhes.grid(row=3, column=0, padx=10, pady=5, sticky='nsew')

tk.Label(frame_principal, text="Questões:").grid(row=4, column=0, pady=5, sticky='w')
entrada_questoes = scrolledtext.ScrolledText(frame_principal, wrap=tk.WORD)
entrada_questoes.grid(row=5, column=0, padx=10, pady=5, sticky='nsew')

tk.Label(frame_principal, text="Parâmetros Envolvidos:").grid(row=6, column=0, pady=5, sticky='w')
entrada_parametros = scrolledtext.ScrolledText(frame_principal, wrap=tk.WORD)
entrada_parametros.grid(row=7, column=0, padx=10, pady=5, sticky='nsew')

# Criar botão para formatar com tamanho padrão e centralizado
botao_formatar = tk.Button(frame_principal, text="Formatar Texto", command=formatar_texto, width=20)
botao_formatar.grid(row=8, column=0, pady=10, sticky='ew')

# Criar área de saída de texto
saida_texto = scrolledtext.ScrolledText(frame_principal, wrap=tk.WORD)
saida_texto.grid(row=9, column=0, padx=10, pady=10, sticky='nsew')
saida_texto.config(state='disabled') 

# Criar botão para copiar o texto com tamanho padrão e centralizado
botao_copiar = tk.Button(frame_principal, text="Copiar Texto", command=copiar_texto, width=20)
botao_copiar.grid(row=10, column=0, pady=5, sticky='ew')

# Ajustar redimensionamento dos widgets
for i in range(1, 11, 2):
    frame_principal.grid_rowconfigure(i, weight=1)
frame_principal.grid_columnconfigure(0, weight=1)

# Frame da aba 2 (Gemini IA)
frame_gemini = tk.Frame(aba_gemini)
frame_gemini.grid(sticky='nsew', padx=20, pady=20)

# Ajustar responsividade da aba Gemini IA
aba_gemini.grid_columnconfigure(0, weight=1)
aba_gemini.grid_rowconfigure(0, weight=1)

# Criar campos para a integração com o Gemini IA
tk.Label(frame_gemini, text="Pergunta para Gemini IA:").grid(row=0, column=0, pady=5, sticky='w')
entrada_gemini = scrolledtext.ScrolledText(frame_gemini, wrap=tk.WORD)
entrada_gemini.grid(row=1, column=0, padx=10, pady=5, sticky='nsew')

# Botão para consultar o Gemini IA com tamanho padrão e centralizado
botao_gemini = tk.Button(frame_gemini, text="Consultar Gemini", command=consultar_gemini, width=20)
botao_gemini.grid(row=2, column=0, pady=10, sticky='ew')

# Saída de resposta do Gemini IA
saida_gemini = scrolledtext.ScrolledText(frame_gemini, wrap=tk.WORD)
saida_gemini.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')
saida_gemini.config(state='disabled')

# Ajustar redimensionamento dos widgets da aba Gemini
for i in range(1, 4):
    frame_gemini.grid_rowconfigure(i, weight=1)
frame_gemini.grid_columnconfigure(0, weight=1)

# Iniciar loop da interface gráfica
janela.mainloop()
