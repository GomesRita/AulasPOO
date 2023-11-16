"""
Escreva um programa para fazer uma pesquisa de opinião sobre a
satisfação no atendimento de uma farmácia. As opções de respostas
devem ser INSATISFEITO; SATISFEITO; NÃO QUERO RESPONDER. O
algoritmo deverá ainda perguntar quantas usuários irão responder à
pergunta. Ao final apresentar o percentual de resposta de cada opção.
"""

print (''' 
Pesquisa de satisfação:
       
    1 - Insatisfeito;
    2 - Satisfeito;
    3 - Não quero responder;

''')

opniao = int (input("Informe um número conforme sua opinião: "))

if(opniao < 1 or opniao > 3):
    print ("Informe um valor válido!")