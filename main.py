listaEstudantes = []
estudante = {}

# Adicionar um novo registro de estudante (nome, ID e notas)
def addEstudante():
    estudante['nome'] = str(input('Digite o nome do estudante: '))
    estudante['id'] = int(input('Digite o id do estudante: '))
    notas = str(input('Digite as notas do estudante (separadas por espaço): '))
    
    # tratamento para separar e converter as notas.
    notas_separadas = notas.split(' ')
    notas_int = [float(nota) for nota in notas_separadas]
    estudante['notas'] = notas_int

    listaEstudantes.append(estudante.copy())
    print(f'Registro de {estudante["nome"]} adicionado com sucesso!')

# Exibir uma lista de todos os registros de estudantes.
def exibirEstudantes():
    print('''
          ---- Lista dos Estudantes ----

ID  Nome                            Notas  ''')
    if listaEstudantes == []:
        print('Nenhum estudante foi registrado ainda')
    else:    
        for estudante in listaEstudantes:
            print(f"{estudante['id']:<3}", end=' ')
            print(f"{estudante['nome']:<30}", end=' ')
            print(f"{estudante['notas']}")

# Procurar um estudante pelo seu ID e exibir seu registro.
def buscarEstudante():
    if listaEstudantes == []:
        print('Nenhum estudante foi registrado ainda')
    else:
        chave = int(input('Digite o ID do estudante que deseja buscar: '))
        alunoEncontrado = False
        for estudante in listaEstudantes:
            if estudante['id'] == chave:
                alunoEncontrado = True
                print()
                print(f'Id: {estudante["id"]}')
                print(f'Nome: {estudante["nome"]}')
                print('Notas:')
                for k,v in enumerate(estudante['notas']):
                    print(f' {k+1}° nota = {v}')
                break
        if not alunoEncontrado:
            print(f'O id {chave} não está registrado') 

# Calcular e exibir a média de notas de todos os estudantes.
def calcularMedia():
    somaNotas = 0
    totalNotas = 0

    if listaEstudantes == []:
        print('Nenhum estudante foi registrado ainda')
    else:
        for aluno in listaEstudantes:
            for nota in aluno['notas']:
                somaNotas += nota
                totalNotas +=1
    media = somaNotas / totalNotas  
    print(f' media das notas de todos os estudantes: {media}')  

# Salvar os registros de estudantes em um arquivo de texto.
def salvarRegistrosTxt():
    with open('estudantes.txt','w') as arquivo:
        for aluno in listaEstudantes:
            arquivo.write(f'{aluno["id"]}, {aluno["nome"]}, {aluno["notas"]} \n')   


# Carregar os registros de estudantes de um arquivo de texto.
def carregarRegistrosTxt():

    # ler arquivo
    with open('estudantes.txt','r') as arquivo:
        dados = arquivo.readlines()

        # converter dados na string para lista com tipos de dados diferentes
        for linha in dados:
            listaAluno = linha.split(',')
            id = int(listaAluno[0])
            nome = listaAluno[1]
            notas_srt = [listaAluno[2].strip("[' ["), listaAluno[3].strip("] \n']")]
            notas_float = []
            for nota in notas_srt:
                nota = float(nota)
                notas_float.append(nota)

            aluno = {'id': id, 'nome': nome, 'notas': notas_float}
           
            # copiar dados do arquivo para lista com o registro dos estudantes
            listaEstudantes.append(aluno)
            print('Carregamento realizado com sucesso!')


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
        case '2':
            exibirEstudantes()
        case '3':
            buscarEstudante()
        case '4':
            calcularMedia()
        case '5':
            salvarRegistrosTxt()
            print('Registro salvo com sucesso no arquivo "estudantes.txt"')
        case '6':
            carregarRegistrosTxt()
        case '7':
            print('Até logo!')
            break
        case _:
            print(f'Opção inválida. Digite um número do menu: ')