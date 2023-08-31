cliente = "PAULA MARTINS"
mes = "JANEIRO"
cupom = "PAULAÉ10"
valor = " 500,00"
desconto = "10"

print("Olá, " + cliente + ". Em " + mes + " você realizou uma compra no valor de R$" + valor  + 
      " e ganhou um desconto de " + desconto + "% em sua próxima compra. Use o cupom " + cupom + ".")

#print('meu nome é {a}, meu sobrenome é {b}'.format{a=nome,b=sobrenome})

nome = input('Digite o seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
mes = 'JANEIRO'
n1 = int(input('Digite o sua 1 nota: '))
n2 = int(input('Digite o sua 2 nota: '))
# desconto = int('10')
# cupom = nome + "É" + desconto
# tipo_nome = type(desconto)
# print(tipo_nome)
soma = n1 + n2 

print(f" O nome é: {nome} {sobrenome} a primeira nota é {n1} e a segunda é {n2} a minha nota geral é {soma}")