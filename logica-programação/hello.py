#!/usr/bin/env python3
from rich import print  # type: ignore


__version__ = "0.0.1"
__author__ = "Edilton Jr""
__license__ = "Unlicensed"

# ESCREVER FRASES EM PYTHON

# modo mais simples

print ("Hello Pythoners")

# escrever usando .format

print ("{} {} usando {} ".format("Hello" , "Pythoners", "Format"))

# Modo herdado da linguagem C referenciando endereço de memoria

print ("%s %s" % ("Hello", "Pythoners  com E comercial"))

# Formatação de Strings Literal
a = "Hello"
aa = "Pythoners"
aaa = "Com fstring"

print (f"{a} {aa} {aaa}")

# usando a biblioteca rich para mudar o estilo do texto impresso

print("[bold blue]Hello Pythoners[/bold blue] [italic green]totalmente[/italic green] [red]estilizado[/red]")