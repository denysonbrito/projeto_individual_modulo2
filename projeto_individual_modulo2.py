#Função para filtrar a nota dos candidatos e inserir na lista de aprovados
def filtrar_por_notas(candidatos, nota_entrevista, teste_teorico, teste_pratico, soft_skills):
    aprovados = []

    for registros in candidatos:
        notas = registros['notas']

        if int(notas[1]) >= nota_entrevista and int(notas[4]) >= teste_teorico and int(notas[7]) >= teste_pratico and int(notas[10]) >= soft_skills:
            aprovados.append(registros)

    return aprovados

#Lista de candidatos no formato de dicionário com chave: candidato e valor: nota
candidatos = [{'candidato': 'Denyson', 'notas': 'e6_t8_p9_s7'}, {'candidato': 'José', 'notas': 'e8_t9_p6_s8'},
{'candidato': 'Everaldo', 'notas': 'e2_t5_p4_s6'}, {'candidato': 'Pereira', 'notas': 'e6_t6_p7_s9'}]

while True: #Tratamento e validação dos dados de entrada
    try:
        nota_entrevista = int(input('Qual a nota mínima da entrevista: '))
        if nota_entrevista < 11:
            break
        else:
            print('O número deve ser menor que 11. Tente novamente.')
    except ValueError:
        print('Entrada inválida. Digite um número inteiro válido.')
while True: #Tratamento e validação dos dados de entrada
    try:
        teste_teorico = int(input('Qual a nota mínima do teste teorico: '))
        if teste_teorico < 11:
            break
        else:
            print('O número deve ser menor que 11. Tente novamente.')
    except ValueError:
        print('Entrada inválida. Digite um número inteiro válido.')

while True: #Tratamento e validação dos dados de entrada
    try:
        teste_pratico = int(input('Qual a nota mínima do teste prático: '))
        if teste_pratico < 11:
            break
        else:
            print('O número deve ser menor que 11. Tente novamente.')
    except ValueError:
        print('Entrada inválida. Digite um número inteiro válido.')

while True: #Tratamento e validação dos dados de entrada
    try:
        soft_skills = int(input('Qual a nota mínima de soft skills: '))
        if teste_pratico < 11:
            break
        else:
            print('O número deve ser menor que 11. Tente novamente.')
    except ValueError:
        print('Entrada inválida. Digite um número inteiro válido.')

#chamei a função para buscar os candidatos conforme critérios e inserir na lista aprovados
aprovados = filtrar_por_notas(candidatos, nota_entrevista, teste_teorico, teste_pratico, soft_skills)

#Mostra o indice do candidato na lista "aprovados", bem como as organiza em linha para
#melhor visualização do usuário
for index, registros in enumerate(aprovados, start=1):
    nome = registros['candidato']
    notas = registros['notas']
    print("\033[0;32m"f'{index}: {nome} {notas}')
    if aprovados == []: #Apresenta uma mensagem caso não tenha candidato nos critérios informados
        print("\033[1;31m"'Não temos candidatos nesses critérios, tente novamente!')