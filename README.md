
# Cadastro de Pets

Um sistema em Python para cadastro de informações de pets com integração ao banco de dados Oracle. 
O sistema oferece uma interface interativa no terminal que permite cadastrar, listar e exportar dados de pets.

## Funcionalidades

- Cadastrar novos pets com informações detalhadas.
- Listar todos os pets cadastrados.
- Exportar os dados dos pets para um arquivo.
- Interface interativa através de menu no terminal.

## Tecnologias Utilizadas

- **Python**
- **Banco de Dados Oracle**

## Pré-requisitos

- **Python 3.x** instalado.
- **Oracle Database** configurado e acessível.
- **Bibliotecas Python** listadas no arquivo `requirements.txt`.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/MarsoL4/Cadastro_Pets.git
   cd Cadastro_Pets
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure o acesso ao banco de dados Oracle, verificando que as credenciais e detalhes de conexão estão corretos no código.

## Utilização

Para iniciar o sistema, execute o seguinte comando:

```bash
python main.py
```

Ao iniciar, o sistema apresentará um menu interativo com as seguintes opções:

1. **Cadastrar Pet**: Permite o cadastro de um novo pet no banco de dados.
2. **Listar Pets**: Mostra uma lista de todos os pets cadastrados.
3. **Exportar Dados**: Exporta os dados dos pets para um arquivo em formato especificado.

Escolha uma opção digitando o número correspondente.

## Exemplo de Uso

### Menu Interativo

```
1 - Cadastrar Pet
2 - Listar Pets
3 - Exportar Dados
0 - Sair

Digite a opção desejada:
```

### Cadastro de um Novo Pet

O sistema solicitará informações como nome, espécie, raça, idade e outras características do pet, que serão armazenadas no banco de dados.

## Contribuindo

Contribuições são bem-vindas! Siga estas etapas para contribuir:

1. Faça um fork do projeto.
2. Crie uma nova branch com sua funcionalidade: `git checkout -b minha-nova-funcionalidade`.
3. Commit suas mudanças: `git commit -m 'Adiciona nova funcionalidade'`.
4. Envie para o branch principal: `git push origin minha-nova-funcionalidade`.
5. Abra um Pull Request.
