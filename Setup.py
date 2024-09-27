import sys
from cx_Freeze import setup, Executable

# Define base como 'Win32GUI' para ocultar o console em aplicações com interface gráfica no Windows
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('NT.pyw', base=base)
]

setup(
    name='NT Application',
    version='1.0',
    description='Aplicação Tkinter sem console',
    executables=executables
)