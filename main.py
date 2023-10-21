listaEstudantes = []
estudante = {}

# Adicionar um novo registro de estudante (nome, ID e notas)
def addEstudante():
    estudante['nome'] = str(input('Digite o nome do estudante: '))
    estudante['id'] = str(input('Digite o id do estudante: '))
    notas = str(input('Digite as notas do estudante (separadas por espaço): '))
    
    # tratamento para separar e converter as notas
    notas_separadas = notas.split(' ')
    notas_int = [float(nota) for nota in notas_separadas]
    estudante['notas'] = notas_int

    listaEstudantes.append(estudante.copy())

# Exibir uma lista de todos os registros de estudantes
def exibirEstudantes():
    print('''
          ---- Lista dos Estudantes ----

ID  Nome                            Notas  ''')
    if listaEstudantes == []:
        print('Nenhum estudante foi registrado')
    else:    
        for aluno in listaEstudantes:
            print(f"{aluno['id']:<3}", end=' ')
            print(f"{aluno['nome']:<30}", end=' ')
            print(f"{aluno['notas']}")
                  
    

# Menu principal

while True:
    print('''
    | Sistema de Gerenciamento de Registros de Estudantes |
    ---
    1. Adicionar Registro de Estudante
    2. Exibir Registro de Estudantes
    3. Procurar por um Estudante
    4. Calcular Média das Notas
    5. Salvar Registros em Arquivo
    6. Carregar Registros de Arquivo
    7. Sair
    ---''')

    escolha = str(input('Digite sua escolha (1-7) '))

    match escolha:
        case '1':
            addEstudante()
            print(f'Registro de {estudante["nome"]} adicionado com sucesso!')
        case '2':
            exibirEstudantes()
        case '7':
            print('Até logo!')
            break