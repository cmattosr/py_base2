#! /usr/bin/env -S python3
""" Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:
Tenha a variável LANG devidamente configurada, ex:

    export LANG=pt_BR
    
Execução:	
    
    python3 hello.py
    ou
    ./hello.py
    
Para forçar um idioma diferente basta setar a variável LANG 
    export LANG=it_IT
"""
    
__version__ = "0.1.0"
__author__ = "Cesar Rocha"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]
msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

print(current_language)    
print(msg)
