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

# Menu principal

while True:
    print('''
    | Sistema de Gerenciamento de Registros de Estudantes |
    ---
    1. Adicionar Registro de Estudante
    2. Exibir Registro de Estudante
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
        case '7':
            print('Até logo!')
            break