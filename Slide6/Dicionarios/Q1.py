"""
Escreva uma função que receba um dicionário que mapeia nomes de países
para suas populações e retorne o nome do país com a maior população. Por
exemplo, se o dicionário for {"Brasil": 211.8, "China": 1400.5, "Índia":
1366.4}, a função deve retornar "China".
"""

dicionario = {"Brasil": 211.8, "China": 1400.5, "Índia":
1366.4}

ValorMaior = max(dicionario, key=dicionario.get)
print(ValorMaior)
