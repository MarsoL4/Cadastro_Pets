# Sistema de Cadastro de Pets

Este é um projeto em Python que permite cadastrar, listar e exportar informações sobre pets utilizando um banco de dados Oracle. A aplicação fornece um menu interativo no terminal para facilitar a interação do usuário.

## Funcionalidades

- **Cadastrar Pets**: Permite ao usuário cadastrar novos pets com tipo, nome e idade.
- **Listar Pets**: Exibe todos os pets cadastrados no banco de dados.
- **Exportar Dados**: Gera uma planilha Excel contendo os dados dos pets cadastrados, com nome de arquivo formatado com a data e hora atuais.

## Tecnologias Utilizadas

- Python
- Pandas
- oracledb (Driver Oracle)
- Excel (para exportação)

## Pré-requisitos

Para executar este projeto, você precisa ter:

- Python 3.x instalado.
- As bibliotecas necessárias instaladas. Você pode instalar as dependências usando o seguinte comando:

```bash
pip install pandas oracledb
```

- Acesso a um banco de dados Oracle e as credenciais necessárias.

## Como Executar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/sistema-cadastro-pets.git
   cd sistema-cadastro-pets
   ```

2. **Abra o arquivo de código e configure as credenciais do banco de dados:**

   Edite o arquivo `seu_arquivo.py` usando seu editor de texto favorito:

   ```bash
   nano seu_arquivo.py
   ```

   No arquivo, modifique as variáveis user, password e dsn com suas credenciais de acesso ao banco de dados Oracle.

3. **Execute o script:**

```bash
python seu_arquivo.py
```

