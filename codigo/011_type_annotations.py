from decimal import Decimal

produto = "Caneta"
valor = Decimal(4.5)
quantidade = 5


def calcula_total(valor: Decimal, quantidad: int) -> Decimal:
    return valor * quantidade


total_da_compra = calcula_total(valor, quantidade)

print("Tipo: ", type(total_da_compra))
print(f"A compra de {quantidade} {produto}s deu R$ {total_da_compra}")