import os
import pandas as pd
import oracledb
from datetime import datetime

# Inicializa a variável de controle de conexão
conexao = False

try:
    # Conexão ao banco de dados usando SID
    conn = oracledb.connect(
    user="SEU_USUARIO",
    password="SUA_SENHA",
    dsn="(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=SEU_HOST)(PORT=SEU_PORT))(CONNECT_DATA=(SID=SEU_SID)))"
)

    conexao = True
    print("\n🟢 Conexão ao banco de dados estabelecida com sucesso!")
except Exception as e:
    print(f"\n🔴 Erro na conexão: {e}")

# Função principal para executar o menu de opções
def main_menu():
    while conexao:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🔧 **Menu Principal** 🔧")
        print("0 - Sair")
        print("1 - Cadastrar Pet")
        print("2 - Listar / Exportar Pets\n")
        
        try:
            escolha = int(input("Escolha uma opção: "))
            print("\n" + "="*30)  # Linha de separação visual
            
            # Abre cursores para operações de banco de dados
            with conn.cursor() as inst_cadastro, conn.cursor() as inst_consulta:
                if escolha == 0:
                    print("🔴 Saindo do sistema...")
                    break
                elif escolha == 1:
                    # Cadastrar um novo pet
                    cadastrar_pet(inst_cadastro)
                elif escolha == 2:
                    # Listar pets e gerar planilha
                    listar_e_exportar(inst_consulta)
                else:
                    print("⚠️ Escolha inválida, tente novamente.")
            
            # Opção para continuar
            input("\nPressione Enter para continuar...")  # Aguarda o usuário pressionar Enter
        except Exception as e:
            print(f"🔴 Ocorreu um erro ao processar sua escolha: {e}")

# Função para cadastrar um novo pet
def cadastrar_pet(inst_cadastro):
    tipo = input("Tipo do Pet.......: ")
    nome = input("Nome do Pet.......: ")
    idade = int(input("Idade do Pet......: "))
    
    # Cria a consulta SQL para inserção
    cadastro_sql = f"""
    INSERT INTO petshop (tipo_pet, nome_pet, idade)
    VALUES ('{tipo}', '{nome}', {idade})
    """
    
    try:
        inst_cadastro.execute(cadastro_sql)
        conn.commit()
        print("\n✅ Dados Gravados com sucesso.")
    except Exception as e:
        print(f"🔴 Erro ao gravar dados: {e}")

# Função para listar os pets e gerar uma planilha
def listar_e_exportar(inst_consulta):
    lista_dados = []
    inst_consulta.execute("SELECT * FROM petshop")
    data = inst_consulta.fetchall()

    for dt in data:
        lista_dados.append(dt)

    lista_dados = sorted(lista_dados)

    # Cria um DataFrame a partir da lista de dados
    dados_df = pd.DataFrame.from_records(lista_dados, columns=['Id', 'Tipo', 'Nome', 'Idade'])

    if dados_df.empty:
        print("⚠️ Não há pets cadastrados.")
    else:
        # Mostra os dados listados
        print("📋 **Dados Listados** 📋")
        print(dados_df.to_string(index=False))  # Remover o índice para uma visualização mais limpa
        print("\n✅ Dados Listados com sucesso.")

        # Pergunta ao usuário se deseja gerar uma planilha
        gerar_planilha = input("Gerar Planilha? [s]im ou [n]ão? ")
        if gerar_planilha.lower() == 's':
            # Obtém a data e hora atual
            agora = datetime.now()
            # Formata a string do nome do arquivo
            nome_arquivo = f"planilha{agora.strftime('%Y%m%d%H%M%S')}.xlsx"
            try:
                dados_df.to_excel(nome_arquivo, index=False)
                print(f"\n✅ Arquivo gerado: {nome_arquivo}")
            except Exception as e:
                print(f"🔴 Erro ao gerar planilha: {e}")

# Inicia o menu principal
if conexao:
    main_menu()
