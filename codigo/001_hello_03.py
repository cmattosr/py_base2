#! /usr/bin/env -S python3
""" Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:
- Tenha a variável LANG devidamente configurada, ex:
    export LANG=pt_BR
- Ou informe através do CLI argument `--lang`
- Ou o usuário terá que digitar
    
Execução:	
    python3 001_hello_03.py --lang=en_US --count=7
    ou
    python3 001_hello_03.py
    ou
    echo "es_ES" | python3 001_hello_03.py 
"""
    
__version__ = "0.1.3"
__author__ = "Cesar Rocha"
__license__ = "Unlicense"

import os
import sys

print(f"{sys.argv=}")

arguments = {
    "lang": None,
    "count": 1,
}

for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    # print(key, value)
    if key not in arguments:
        print(f"Invalid argument: {key}")
        sys.exit()
    arguments[key] = value
    
current_language = arguments["lang"]

# print(current_language)

if current_language is None:
    # print(f"{current_language=}")
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input(
            "What language do you speak? (en_US, pt_BR, it_IT, es_ES, fr_FR, C.UTF) "
        )

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_ES": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
    "C.UTF": "Eita lasqueira",
}

print(msg[current_language] * int(arguments["count"]))    

