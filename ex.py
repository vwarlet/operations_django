def media(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    dados = arquivo.read()
    dados = dados.split('\n')
    lista = []
    l = []
    for x in dados:
        lista_notas = x.split(',')
       
        aluno = lista_notas[0]
        lista_notas.pop(0)
        num_notas = len(lista_notas)
        med = lambda notas: sum([int(i) for i in lista_notas]) / num_notas
        
        lista.append({aluno:med(lista_notas)})
    
    return lista

if __name__ == '__main__':
    lista_media = media('teste.txt')
    print(lista_media)