arquivo_contatos = open('dados/contatos-escrita.csv', mode='a+', encoding='latin_1')

contatos = ['11,Carol,carol@carol.com.br\n'
           '12,Ana,ana@ana.com.br\n'
           '13,Tais,tais@tais.com.br\n'
           '14,Felipe,felipe@felipe.com.br\n']

'''
conteudo = arquivo_contatos.readlines()
data = [linha.split() for linha in conteudo]
for i in data:
    print(f'{i}')
for linha in arquivo_contatos:
    print(linha, end="")
'''
for contato in contatos:
    arquivo_contatos.write(contato)

arquivo_contatos.flush()
input('Pressione <Enter> para encerrar o programa')

arquivo_contatos.seek(0)
for linha in arquivo_contatos:
    print(linha, sep="")