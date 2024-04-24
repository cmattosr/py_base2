#!/usr/bin/env python3

import logging
from logging import handlers

# cria nossa instância de logging
log = logging.Logger("008_logs.py", level=logging.DEBUG)

# level
# ch = logging.StreamHandler() # manda pra tela
fh = handlers.RotatingFileHandler("008_logs.log", maxBytes=100, backupCount=5) # manda pra arquivo, normalmente maxBytes=10**6
# ch.setLevel(logging.DEBUG)

# formatação
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s %(message)s",
)
# ch.setFormatter(fmt)
fh.setFormatter(fmt)

# destino da mensagem (por padrão stderr)
# log.addHandler(ch)
log.addHandler(fh)

# logging.debug("Mensagem de debug")
# logging.info("Mensagem de info")
# logging.warning("Mensagem de warning")
# logging.error("Mensagem de error")
# logging.critical("Mensagem de critical")

log.debug("Mensagem de debug")
log.info("Mensagem de info")
log.warning("Mensagem de warning")
log.error("Mensagem de error")
log.critical("Mensagem de critical")

print("-" * 80 + "\n")

try:
    1/0
except ZeroDivisionError as e:
    # logging.error("Deu erro: %s", str(e))
    log.error("Deu erro: %s", str(e))
    