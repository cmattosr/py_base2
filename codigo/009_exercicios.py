print("Faça um programa que imprime os números pares de 1 a 200")
for n in range(1, 201):
    if n % 2 == 0:
        print(n)
        
print ("-" * 75)

print("Alarme de temperatura")

import sys
import logging

log = logging.Logger("alerta")

try:
    temperatura = float(input("Informe a temperatura: ").strip())
except ValueError:
    log.error("Temperatura inválida")
    sys.exit(1)
    
try: 
    umidade = float(input("Informe a umidade: ").strip())
except ValueError:
    log.error("Umidade inválida")
    sys.exit(1)
    
if temperatura > 45:
    print("ALERTA!!! \U0001f975 Perigo, calor extremo")
elif temperatura * 3 >= umidade:
    print("ALERTA!!! \U0001f975 \U0001f4a6 Perigo, calor úmido")
elif temperatura >= 10 and temperatura <=30:
    print("Normal \U0001f603")
elif temperatura >= 0 and temperatura <= 10:
    print("Frio \U0001f92a")
else:
    print("Frio extremo \U0001f976")
    
print ("-" * 75)

print("Duplica vogais")

palavras = []
while True:
    palavra = input("Digite uma palavra (ou enter pra sair): ").strip()
    if not palavra:
        break
    nova_palavra = ""
    for letra in palavra:
        if letra.lower() in "aeiouãéíõóüú": 
            nova_palavra += letra * 2
        else:
            nova_palavra += letra
    palavras.append(nova_palavra)
    

print(*palavras, sep="\n")
        
print ("-" * 75)

print("Reserva de Quartos\n\n")

import os
import sys
import logging

path = os.curdir
reservas_arq = os.path.join(path, "009_reservas.txt")
quartos_arq = os.path.join(path, "009_quartos.txt")

ocupados = {}

try:
    for line in open(reservas_arq):
        nome, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {"nome": nome, "dias": int(dias)}
except FileNotFoundError:
    logging.error("Arquivo de reservas não encontrado")
    sys.exit(1)

cliente = input("Informe seu nome: ").strip()

print("Lista de quartos")

quartos = {}

try:
    for line in open(quartos_arq):
        codigo, nome, preco = line.strip().split(",")
        codigo = int(codigo)
        quartos[codigo] = {"nome": nome, "preco": float(preco), "disponivel": False if int(codigo) in ocupados else True}
except FileNotFoundError:
    logging.error("Arquivo de quartos não encontrado")
    sys.exit(1)
for codigo, dados in quartos.items():
    disponivel = "\U0001f6ab" if not dados["disponivel"] else "\U0001f44d"
    print(f"{codigo} - {dados['nome']} - R$ {dados['preco']:.2f} - {disponivel}")

if len(ocupados) == len(quartos):
    print("Todos os quartos estão ocupados")
    sys.exit(1)
    
try:
    quarto = int(input("Em qual quarto deseja ficar? ").strip())
    if not quartos[quarto]["disponivel"]:
        print(f"O quarto {quarto} está ocupado")
        sys.exit(1)
except ValueError:
    logging.error("Número inválido, digite apenas um número inteiro")
    sys.exit(1)
except KeyError:
    logging.error(f"Quarto {quarto} não existe")
    sys.exit(1)
try:
    dias = int(input("Por quantos dias deseja ficar? ").strip())
except ValueError:
    logging.error("Número inválido, digite apenas um número inteiro")
    sys.exit(1)
    
nome_quarto = quartos[quarto]["nome"]
valor = quartos[quarto]["preco"] * dias
disponivel = quartos[quarto]["disponivel"]

with open("009_reservas.txt", "a") as file_:
    file_.write(f"{cliente}, {quarto}, {dias}\n")

print(f"{cliente}, você escolheu o qusrto {nome_quarto} por R$ {valor:.2f} por {dias} dias")
    
