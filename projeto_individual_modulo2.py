def filtrar_por_notas(candidatos, nota_entrevista, teste_teorico, teste_pratico, soft_skills):
    aprovados = []

    for registros in candidatos:
        notas = registros['notas']

        if int(notas[1]) >= nota_entrevista and int(notas[4]) >= teste_teorico and int(notas[7]) >= teste_pratico and int(notas[10]) >= soft_skills:
            aprovados.append(registros)

    return aprovados

candidatos = [{'candidato': 'Denyson', 'notas': 'e6_t8_p9_s7'}, {'candidato': 'José', 'notas': 'e8_t9_p6_s8'}]

nota_entrevista = int(input('Qual a nota mínima? '))
teste_teorico = int(input('Qual a nota mínima? '))
teste_pratico = int(input('Qual a nota mínima? '))
soft_skills = int(input('Qual a nota mínima? '))

aprovados = filtrar_por_notas(candidatos, nota_entrevista, teste_teorico, teste_pratico, soft_skills)

for index, registros in enumerate(aprovados, start=1):
    nome = registros['candidato']
    notas = registros['notas']
    print(f'{index}: {nome} {notas}')