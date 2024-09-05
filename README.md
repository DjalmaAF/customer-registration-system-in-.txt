# Sistema de Cadastro de Arquivos e Clientes

Este é um sistema simples desenvolvido em Python para gerenciar arquivos de texto e cadastrar clientes neles. O programa permite criar arquivos, cadastrar, listar e remover clientes, com um sistema interativo via terminal.

## Funcionalidades

O sistema oferece as seguintes opções:

1. **Criar Arquivo Novo**: Permite criar um novo arquivo de texto onde os clientes podem ser cadastrados.
2. **Cadastrar Cliente**: Adiciona clientes a um arquivo de texto existente.
3. **Remover Cliente**: Remove clientes de um arquivo de texto selecionado.
4. **Listar Clientes**: Exibe os clientes cadastrados em um arquivo de texto.
5. **Sair do Programa**: Encerra a execução do programa.

## Requisitos

Para executar o programa, você precisará de:

- Python 3.x instalado no seu sistema.
- Sistema operacional Windows (devido ao uso do comando `cls` para limpar a tela).

## Como Executar

1. Clone este repositório ou faça o download dos arquivos.
2. Navegue até o diretório do projeto.
3. Execute o arquivo principal do sistema:

```bash
python main.py
```

4. O menu interativo será exibido no terminal. Escolha as opções conforme desejar.

## Organização do Código

- **menu()**: Exibe as opções principais do sistema.
- **choice()**: Controla a interação do usuário com o menu.
- **make_file()**: Cria um novo arquivo de texto para cadastro de clientes.
- **list_of_files()**: Lista os arquivos de texto disponíveis.
- **new_client()**: Permite cadastrar novos clientes em um arquivo selecionado.
- **delete_client()**: Remove um cliente de um arquivo de texto.
- **read_file()**: Exibe o conteúdo de um arquivo.

## Exemplo de Uso

```text
========================================
        SISTEMA DE CADASTRO v.1
========================================
1 - Criar arquivo novo
2 - Cadastrar cliente
3 - Remover cliente
4 - Listar clientes
5 - Sair do programa
========================================
Digite sua opção: 1
```

## Melhorias Futuras

- Implementação de tratamento de erros mais robusto.
- Integração com banco de dados para armazenar as informações.
- Adicionar interface gráfica (GUI) para facilitar o uso.

## Contribuindo

Sinta-se à vontade para enviar pull requests ou abrir issues com sugestões de melhorias ou correções.

## Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo LICENSE para obter mais detalhes.
