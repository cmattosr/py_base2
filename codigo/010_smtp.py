#!/usr/bin/env python3
"""Exemplos de envio de e-mail"""

# Iniciar o servidor SMTP: python -m smtpd -c DebuggingServer -n localhost:8025

import smtplib

SERVER = "localhost"
PORT = 8025


FROM = "cmrocha@gmail.com"
TO = ["destino@server.com", "outro@server.com"]
SUBJECT = "Assunto do e-mail"
TEXT = """\
Este é o meu e-mail enviado pelo Python
<b>Olá, mundo</b>
"""

#SMTP
mensagem = f"""\
From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host = SERVER, port = PORT) as server:
    server.sendmail(FROM, TO, mensagem.encode("utf-8"))