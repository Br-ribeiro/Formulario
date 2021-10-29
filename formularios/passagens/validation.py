def origem_destino_iguas(origem,destino, lista_de_erros):

     if origem ==  destino:
            lista_de_erros['destino'] = 'Origem e destino não podem ser iguais'

def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):

    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua numero neste campo'