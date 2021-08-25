import contatos_utils

caminho = 'dados/contatos.csv'
caminho_pickle = 'dados/contatos.pickle'
caminho_json = 'dados/contatos.json'
encoding = 'latin_1'
try:
    contatos = contatos_utils.csv_para_contatos(caminho, encoding)

    contatos_utils.contatos_para_pickle(contatos, caminho_pickle)
    contatos2 = contatos_utils.pickle_para_contatos(caminho_pickle)

    contatos_utils.contatos_para_json(contatos, caminho_json)
    contatos3 = contatos_utils.json_para_contatos(caminho_json)

    for i in contatos3:
        print(f'ID: {i.id}\t'
              f'NOME: {i.nome}\t'
              f'EMAIL: {i.email}\t')
except FileNotFoundError:
    print("Arquivo não encontrado!")
except PermissionError:
    print("Sem permissões necessárias!")

