p = '======================================================================================'
import os
import time
import hashlib
from hashlib import sha256
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import json

# ==================== Funções de manipulação de JSON ====================
def carregar_json(caminho):
    if os.path.exists(caminho) and os.path.getsize(caminho) > 0:
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def salvar_json(caminho, dados):
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

# ==================== Telas e fluxo ====================
def tela_inicio():
    os.system("cls")
    print(p)
    print("Bem-vindo ao setor de administração do sistema!")
    print(p)
    time.sleep(5)
    os.system("cls")

def credencial_texto():
    os.system("cls")
    print(p)
    print("Digite o nome de usuário e senha para acessar o sistema")
    print(p)
    IDmin = input("Digite o nome de usuário: ")
    IDsenha = input("Digite a senha: ")
    print(p)
    if verificar_credenciais(IDmin, IDsenha):
        print("Acesso concedido!")
        print(p)
        time.sleep(2)
        # Continue o fluxo do admin aqui
    else:
        print("Acesso negado")
        time.sleep(2)
        credencial_texto()

def verificar_credenciais(IDmin, IDsenha):
    credenciais = carregar_json("credenciais.json")
    hash_usuario = sha256(IDmin.encode()).hexdigest()
    hash_senha = sha256(IDsenha.encode()).hexdigest()
    for cred in credenciais:
        if cred["usuario"] == hash_usuario and cred["senha"] == hash_senha:
            return True
    return False

def redirecionar():
    os.system("cls")
    print(p)
    print("Redirecionando para o sistema...")
    print(p)
    time.sleep(2)
    os.system("cls")
    # Aqui você pode adicionar o código para redirecionar para o sistema principal

def escolhas():
    os.system("cls")
    print(p)
    print("Escolha uma opção:")
    print("1. Cadastrar novo usuário")
    print("2. Média de usuários por mês")
    print("3. Excluir usuário")
    print("4. Análise de Desempenho")
    print("5. Sair")
    print(p)
    escolha = input("Digite sua escolha: ")
    print(p)
    time.sleep(2)
    return escolha

def cadastrar_usuario():
    os.system("cls")
    print(p)
    print("Cadastrar novo usuário")
    print(p)
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha do usuário: ")
    hash_usuario = sha256(nome.encode()).hexdigest()
    hash_senha = sha256(senha.encode()).hexdigest()
    credenciais = carregar_json("credenciais.json")
    credenciais.append({"usuario": hash_usuario, "senha": hash_senha})
    salvar_json("credenciais.json", credenciais)
    print("Usuario cadastrado com sucesso!")
    time.sleep(2)
    os.system("cls")

def analisar_cadastros_por_mes():
    try:
        usuarios = carregar_json("Thunderstruck.json")
        datas = []
        for usuario in usuarios:
            data_str = usuario.get("Data de Nascimento", "").strip()
            try:
                data = datetime.strptime(data_str, "%d/%m/%Y")
                datas.append(data)
            except ValueError:
                pass  # Ignora datas inválidas

        hoje = datetime.now()
        mes_atual = hoje.month
        ano_atual = hoje.year

        # Mes anterior
        if mes_atual == 1:
            mes_anterior = 12
            ano_anterior = ano_atual - 1
        else:
            mes_anterior = mes_atual - 1
            ano_anterior = ano_atual

        # Mes seguinte
        if mes_atual == 12:
            mes_seguinte = 1
            ano_seguinte = ano_atual + 1
        else:
            mes_seguinte = mes_atual + 1
            ano_seguinte = ano_atual

        count_anterior = sum(1 for d in datas if d.month == mes_anterior and d.year == ano_anterior)
        count_atual = sum(1 for d in datas if d.month == mes_atual and d.year == ano_atual)
        count_seguinte = sum(1 for d in datas if d.month == mes_seguinte and d.year == ano_seguinte)

        print(p)
        print(f"Inscritos no mês anterior ({mes_anterior:02d}/{ano_anterior}): {count_anterior}")
        print(f"Inscritos no mês atual ({mes_atual:02d}/{ano_atual}): {count_atual}")
        print(f"Inscritos no mês seguinte ({mes_seguinte:02d}/{ano_seguinte}): {count_seguinte}")
        print(p)
        time.sleep(5)
    except FileNotFoundError:
        print("Arquivo Thunderstruck.json não encontrado.")
        time.sleep(2)

def excluir_usuario():
    os.system("cls")
    print(p)
    print("Excluir usuário")
    print(p)
    nome = input("Digite o nome do usuário a ser excluido: ")
    hash_usuario = sha256(nome.encode()).hexdigest()
    credenciais = carregar_json("credenciais.json")
    novas_credenciais = [c for c in credenciais if c["usuario"] != hash_usuario]
    salvar_json("credenciais.json", novas_credenciais)
    print("Usuario excluido com sucesso!")
    time.sleep(2)

def saida():
    os.system("cls")
    print(p)
    print("Saindo do sistema...")
    print(p)
    time.sleep(2)
    os.system("cls")
    exit()

def nome_amigavel_curso(curso):
    if curso == "Educacao_Digital_e_Inclusao_Tecnologica":
        return "Educação Digital e Inclusão Tecnológica"
    return curso

def analisar_desempenho_usuarios():
    gabaritos = {
        "Curso de Python": ['a', 'a', 'd'],
        "Educacao_Digital_e_Inclusao_Tecnologica": ['a', 'a', 'b'],
    }

    # Lê Thunderstruck.json
    usuarios = carregar_json("Thunderstruck.json")
    df_usuarios = pd.DataFrame(usuarios)

    # Lê respostas.json
    respostas = carregar_json("respostas.json")
    # Garante que todas as respostas tenham o campo "Curso"
    for r in respostas:
        if "Curso" not in r:
            r["Curso"] = ""
    df_respostas = pd.DataFrame(respostas)

    # Junta os dados pelo ID
    if not df_respostas.empty and not df_usuarios.empty:
        df = pd.merge(df_respostas, df_usuarios, on="ID", how="left", suffixes=('', '_usuario'))
        if "Curso" not in df.columns:
            df["Curso"] = ""
        df["Curso"] = df["Curso"].fillna("")
    else:
        print("Sem dados suficientes para análise.")
        return

    # Calcula acertos
    def conta_acertos(row):
        curso = row.get("Curso", "")
        gabarito = gabaritos.get(curso, [])
        acertos = 0
        for i in range(1, 4):
            if f"Pergunta{i}" in row and len(gabarito) >= i:
                if str(row.get(f"Pergunta{i}", "")).strip().lower() == gabarito[i-1]:
                    acertos += 1
        return acertos

    df["Acertos"] = df.apply(conta_acertos, axis=1)

    # Tabela de desempenho por usuário
    desempenho = df.groupby(["ID", "Nome", "Curso"])["Acertos"].max().reset_index()
    desempenho = desempenho.sort_values(by=["Curso", "Acertos"], ascending=[True, False])

    print("\nTabela de desempenho dos usuários:")
    # Exibe o nome amigável do curso na tabela
    desempenho["Curso"] = desempenho["Curso"].apply(nome_amigavel_curso)
    print(desempenho.to_string(index=False))

    # Gráfico de desempenho por curso
    cursos_unicos = desempenho["Curso"].unique()
    for curso in cursos_unicos:
        dados_curso = desempenho[desempenho["Curso"] == curso]
        plt.figure(figsize=(8,4))
        plt.bar(
            [f'{row["Nome"]} ({row["ID"]})' for idx, row in dados_curso.iterrows()],
            dados_curso["Acertos"],
            color='skyblue'
        )
        plt.ylabel("Quantidade de Acertos")
        plt.xlabel("Usuário (ID)")
        plt.title(f"Desempenho dos Usuários - {curso}")
        plt.tight_layout()
        plt.show()

    # Gráfico de cursos mais acessados (usa as respostas, não o merge)
    plt.figure(figsize=(6,4))
    # Use nome amigável para exibição
    cursos_exibicao = df_respostas["Curso"].apply(nome_amigavel_curso)
    acessos = cursos_exibicao.value_counts()
    plt.bar(acessos.index, acessos.values, color='orange')
    plt.ylabel("Quantidade de Acessos")
    plt.xlabel("Curso")
    plt.title("Cursos Mais Acessados")
    plt.tight_layout()
    plt.show()

# ==================== Fluxo principal ====================
tela_inicio()
credencial_texto()
redirecionar()
while True:
    escolha = escolhas()
    if escolha == "1":
        cadastrar_usuario()
    elif escolha == "2":
        analisar_cadastros_por_mes()
    elif escolha == "3":
        excluir_usuario()
    elif escolha == "4":
        analisar_desempenho_usuarios()
    elif escolha == "5":
        saida()
    else:
        print("Escolha inválida!")
        time.sleep(2)