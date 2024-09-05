def linha(tam=42):
    return '=' * tam


def clear():
    import os
    os.system('cls')


def head(txt):
    clear()
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(opcoes):
    c = 0
    for item in opcoes:
        c += 1
        print(f'{c} - {item}')


def loading_dots():
    from time import sleep
    for c in range(5):
        if c < 4:
            dots = '.' * c
            sleep(0.8)
            clear()
            print(f'Selecionando arquivo {dots}')
            sleep(2)


def choice(opc=0):
    print(linha())
    while True:
        head('SISTEMA DE CADASTRO v.1')
        menu(['Criar arquivo novo', 'Cadastrar cliente',
             'Remover cliente', 'Listar clientes', 'Sair do programa'])
        opc = int(input('Digite sua opção: '))
        if opc == 1:
            make_file()
            break
        if opc == 2:
            new_client()
            print('CADASTRO ATUALIZADO!'.center(42))
            break
        if opc == 3:
            delete_client()
            print('CLIENTE REMOVIDO COM SUCESSO'.center(42))
        if opc == 4:
            head('DIGITE O NOME DO ARQUIVO QUE DESEJA LISTAR')
            list_of_files()
            read_file(file_name=str(input(':')))
        if opc == 5:
            break
    head('PROGRAMA FINALIZADO')


def make_file():
    clear()
    directory = r'C:\Users\netto\OneDrive\Documentos\lib\ArcFile'
    file_name = str(input('Digite o nome do arquivo: '))
    path = f'{directory}\\{file_name}.txt'
    with open(path, 'x') as directory:
        print(f'Arquivo criado! [ {file_name} ]')


def list_of_files():
    clear()
    head('LISTA DE ARQUIVOS')
    import os
    directory = r'C:\Users\netto\OneDrive\Documentos\lib\ArcFile'
    content = os.listdir(directory)
    archives = [archive for archive in content if os.path.isfile(
        os.path.join(directory, archive))]
    c = 0
    for archive in archives:
        c += 1
        print(f'{c} - {archive}')


def new_client():
    import os
    list_of_files()
    print('Digite o nome do arquivo que deseja realizar a ação: ')
    file_name = str(input('\n: '))
    directory = r'C:\Users\netto\OneDrive\Documentos\lib\ArcFile'
    path = os.path.join(directory, file_name)
    if not os.path.isfile(path):
        print(f'O arquivo {file_name} não existe.')
    print(f'Arquivo selecionado: {file_name}')
    while True:
        name = str(input('Digite o nome que deseja cadastrar: ').capitalize())
        with open(path, 'a') as file:
            file.write(name + '\n')
            print(f'{name} adicionado com sucesso!')
        head('DESEJA CONTINUAR ?')
        continuar = str(input('Digite [ n ] para finalizar. \n:').upper())
        if continuar == 'N':
            break
        read_file(file_name)


def delete_client():
    import os
    list_of_files()
    print('Digite o nome do arquivo que deseja realizar a ação: ')
    file_name = str(input('\n: '))
    directory = r'C:\Users\netto\OneDrive\Documentos\lib\ArcFile'
    path = os.path.join(directory, file_name)
    if not os.path.isfile(path):
        print(f'O arquivo {file_name} não existe.')
    loading_dots()
    print(f'Arquivo selecionado: {file_name}')
    read_file(file_name)
    while True:
        name_to_remove = str(
            input('Digite o nome que deseja remover: '.capitalize()))
        with open(path, 'r') as file:
            lines = file.readlines()
        with open(path, 'w') as file:
            for line in lines:
                if line.strip() != name_to_remove:
                    file.write(line)
        head('DESEJA CONTINUAR ?')
        continuar = str(input('Digite [ n ] para finalizar. \n:').upper())
        if continuar == 'N':
            break
        read_file(file_name)


def read_file(file_name=0):
    import os
    directory = r'C:\Users\netto\OneDrive\Documentos\lib\ArcFile'
    path = os.path.join(directory, file_name)
    if not os.path.isfile(path):
        print(f'O arquivo {file_name} não existe.')
        clear()
    with open(path, 'r') as file:
        content = file.read()
        print(content)
