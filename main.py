p = '============================================================================================================================================================='
import os
import time
import hashlib
from hashlib import sha256
import getpass
from datetime import datetime
import webbrowser
import json
import pyttsx3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

usuario_logado_id = None

#===================== Configurações de e-mail ====================
def enviar_email_confirmacao(destinatario):
    remetente = "plataformapim25@gmail.com"  # Coloque seu e-mail aqui
    senha = "jjir winm guqf huyx"             # Coloque sua senha de app aqui
    assunto = "Cadastro concluído"
    corpo = "Seu cadastro na plataforma foi realizado com sucesso!"

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(corpo, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as servidor:
            servidor.starttls()
            servidor.login(remetente, senha)
            servidor.send_message(msg)
        printn("E-mail de confirmação enviado!")
        narrar("E-mail de confirmação enviado!")
    except Exception as e:
        printn(f"Erro ao enviar e-mail: {e}")
        narrar("Erro ao enviar e-mail.")
# ==================== Funções de vídeo e pasta ====================
def mostrar_video_curso1():
    url = 'https://youtu.be/4p7axLXXBGU?feature=shared'
    webbrowser.open(url)

def mostrar_pasta_curso1():
    url = "https://drive.google.com/file/d/10Xhau4Y3sPArrp1ahwyaglzJuukGogt-/view?usp=sharing"
    webbrowser.open(url)

def mostrar_video_curso2():
    url = "https://youtu.be/caSaRZMVSZk?feature=shared"
    webbrowser.open(url)

def mostrar_pasta_curso2():
    url = "https://drive.google.com/drive/folders/1Y7BI0Iitx4R1G5_vFlpQgFoYG09wJPXR?usp=sharing"
    webbrowser.open(url)

# ==================== Funções de manipulação de JSON ====================
def salvar_usuario_json(user_data):
    caminho = "Thunderstruck.json"
    if os.path.exists(caminho) and os.path.getsize(caminho) > 0:
        with open(caminho, "r", encoding="utf-8") as f:
            usuarios = json.load(f)
    else:
        usuarios = []
    usuarios.append(user_data)
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=4)

def salvar_respostas_json(user_id, respostas, curso):
    caminho = "respostas.json"
    if os.path.exists(caminho) and os.path.getsize(caminho) > 0:
        with open(caminho, "r", encoding="utf-8") as f:
            todas_respostas = json.load(f)
    else:
        todas_respostas = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    resposta_dict = {
        "ID": user_id,
        "Curso": curso,
        "Data e Hora": timestamp,
    }
    for i, resposta in enumerate(respostas):
        resposta_dict[f"Pergunta{i+1}"] = resposta
    todas_respostas.append(resposta_dict)
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(todas_respostas, f, ensure_ascii=False, indent=4)
#===================== Funções de narração ====================
narrar_ativo = False
engine = pyttsx3.init()

def narrar(texto):
    if narrar_ativo:
        engine.say(texto)
        engine.runAndWait()

def inputn(texto):
    if texto != p:  # Só narra se não for a linha de separação
        narrar(texto)
    return input(texto)
def printn(texto):
    print(texto)
    if texto != p:  # Só narra se não for a linha de separação
        narrar(texto)
#===================== Funções de Daltonismo ====================

def trocar_tema_vscode_high_contrast():
    """
    Ativa o tema High Contrast do VS Code (já incluso na instalação padrão).
    """
    try:
        # Caminho do settings.json do VS Code no Windows
        settings_path = os.path.expanduser(r"~\\AppData\\Roaming\\Code\\User\\settings.json")
        import json
        # Lê as configurações atuais
        with open(settings_path, "r", encoding="utf-8") as f:
            settings = json.load(f)
        # Altera o tema para High Contrast
        settings["workbench.colorTheme"] = "High Contrast"
        # Salva as configurações
        with open(settings_path, "w", encoding="utf-8") as f:
            json.dump(settings, f, ensure_ascii=False, indent=4)
        printn("Tema High Contrast ativado! Reinicie o VS Code para aplicar.")
        narrar("Tema High Contrast ativado! Reinicie o Visual Studio Code para aplicar.")
    except Exception as e:
        printn(f"Erro ao trocar o tema: {e}")
        narrar("Erro ao trocar o tema.")
#====================== Funções de configuração ====================
def configuracoes():
    global narrar_ativo
    while True:
        os.system("cls")
        print(p)
        printn("Configurações da Plataforma")
        printn("[1] Ativar/Desativar narração [Beta]")
        printn("[2] Ativar tema Daltonismo(High Contrast VS Code) [Beta]")
        printn("[3] Voltar")
        print(p)
        escolha = inputn("Digite sua escolha: ")
        if escolha == "1":
            narrar_ativo = not narrar_ativo
            status = "ativada" if narrar_ativo else "desativada"
            printn(f"Narração {status}!")
            narrar(f"Narração {status}!")
            time.sleep(2)
        elif escolha == "2":
            printn("Ativando tema High Contrast...")
            narrar("Ativando tema High Contrast.")
            trocar_tema_vscode_high_contrast()
            inputn("Pressione Enter para continuar...")
        elif escolha == "3":
            break
        else:
            printn("Opção inválida!")
            narrar("Opção inválida!")
            time.sleep(2)
# ==================== Funções auxiliares ====================
def get_next_user_id():
    try:
        with open("user_id_counter.txt", "r") as id_file:
            last_id = int(id_file.read().strip())
    except FileNotFoundError:
        last_id = 0
    next_id = last_id + 1
    with open("user_id_counter.txt", "w") as id_file:
        id_file.write(str(next_id))
    return f"{next_id:05}"

def tela_inicio():
    os.system("cls")
    print(p)
    printn("Seja muito bem vindo a plataforma de cursos online\nfornecido pelo grupo Thóth")
    print(p)
    time.sleep(5)
    os.system("cls")

def repcadastro():
    os.system("cls")
    print(p)
    printn("Olá caso possua cadastro Digite [1]\n"
          "Caso não possua cadastro Digite [2]\n"
          "Para configurações digite [3]")
    print(p)
    while True:
        try:
            opcao = int(input("Digite:"))
            if opcao in [1, 2, 3]:
                print(p)
                time.sleep(2)
                return opcao
            else:
                print("Opção inválida! Tente novamente.")
                narrar("Opção inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Digite um número.")
            narrar("Entrada inválida! Digite um número.")

def abrir_usuario():
    global usuario_logado_id
    while True:
        os.system("cls")
        print(p)
        printn('Bem-vindo de volta\n')
        print(p)
        usu = inputn(f"\nDigite seu ID: ")
        senha = inputn(f"\nDigite sua senha: ")
        print(p)
        time.sleep(2)
        if verificar_id_e_senha_json(usu, senha):
            usuario_logado_id = usu
            printn("Login feito com sucesso! Acesso concedido.")
            time.sleep(2)
            break
        else:
            printn("ID ou senha inválidos! Por favor, tente novamente.")
            time.sleep(2)

def gerar_hash(valor):
    return hashlib.sha256(valor.encode('utf-8')).hexdigest()

def verificar_senha(senha, hash_senha):
    return gerar_hash(senha) == hash_senha

def verificar_id_e_senha_json(user_id, senha):
    caminho = "Thunderstruck.json"
    if not os.path.exists(caminho):
        print("Arquivo de usuários não encontrado.")
        return False
    with open(caminho, "r", encoding="utf-8") as f:
        usuarios = json.load(f)
        for usuario in usuarios:
            if usuario["ID"] == user_id and verificar_senha(senha, usuario["Senha"]):
                return True
    return False

def info_cadastro_inicio():
    os.system("cls")
    print(p)
    printn("Primeiro precisamos de algumas informações para a formulação de um cadastro na plataforma")
    ini = int(inputn(f"Você aceita realizar o cadastro na plataforma ?\n"
                    "Se sim digite [1]\n"
                    "Caso não queira, digite [2]\n" \
                    f"{p}\n"
                    "Digite: "))
    print(p)
    time.sleep(5)
    os.system("cls")
    return ini

def registro_usuario():
    global usuario_logado_id
    os.system("cls")
    print(p)
    printn("Ótimo! precisamos agora das seguintes informações")
    nome = inputn(f"{p}\ndigite seu nome: ")
    Data = inputn(f"{p}\ndigite sua Data de Nascimento[dd/mm/aaaa]: ")
    user_id = get_next_user_id()
    usuario_logado_id = user_id
    while True:
        cpf = inputn(f"{p}\ndigite seu CPF (apenas números, 11 dígitos): ")
        if len(cpf) == 11 and cpf.isdigit():
            hash_cpf = gerar_hash(cpf)
            break
        else:
            printn("CPF inválido! Certifique-se de digitar exatamente 11 números.")
            time.sleep(2)
    # NOVO: Pergunta e criptografa o e-mail
    while True:
        email = inputn(f"{p}\nDigite seu e-mail: ")
        if "@" in email and "." in email:
            hash_email = gerar_hash(email)
            break
        else:
            printn("E-mail inválido! Tente novamente.")
            time.sleep(2)
    Curso = inputn(f"{p}\ndigite seu Curso atual ou caso não esteja cursando (apenas siglas e caso não esteja coloque N apenas): ")
    senha = getpass.getpass(f"{p}\nCrie uma senha para sua conta: ")
    hash_senha = gerar_hash(senha)
    print(p)
    user_data = {
        "ID": user_id,
        "Nome": nome,
        "Data de Nascimento": Data,
        "CPF": hash_cpf,
        "Email": hash_email,  # Salva o e-mail criptografado
        "Curso": Curso,
        "Senha": hash_senha
    }
    salvar_usuario_json(user_data)
    # Envia e-mail de confirmação
    enviar_email_confirmacao(email)
    time.sleep(5)
    os.system("cls")
    print(p)
    printn('Cadastro realizado com sucesso\n')
    printn(f'Seu ID de usuário é: {user_id}\n')
    printn('Redirecionando para a plataforma de cursos')
    print(p)
    time.sleep(7)
    os.system("cls")
    loading()

def loading():
    print(p)
    printn('Aguarde')
    print(p)
    time.sleep(5)

def cursos():
    while True:
        os.system("cls")
        print(p)
        printn("Aqui estão os cursos disponíveis:" \
              "\n1. Curso de Python[1]\n2. Educação Digital e Inclusão Tecnológica[2]")
        print(p)
        time.sleep(4)
        try:
            opcao2 = int(inputn("Escolha um curso digitando o número correspondente: "))
            if opcao2 in [1, 2]:
                return opcao2
            else:
                printn("Opção inválida. Por favor, escolha um curso válido.")
                time.sleep(2)
        except ValueError:
            printn("Entrada inválida. Por favor, digite um número.")
            time.sleep(2)

def fim_programa():
    os.system("cls")
    print(p)
    printn("Infelizmente não poderemos prosseguir com o fornecimento do conteúdo, obrigado pela colaboração até o momento\n"
          "esperamos que possa recomendar para novas pessoas")
    print(p)
    time.sleep(5)
    os.system("cls")
    exit()

def cursoes(opcao2):
    if opcao2 == 1:
        time.sleep(5)
        os.system("cls")
        print(p)
        printn("Você escolheu o Curso de Python.")
        print(p)
        time.sleep(4)
        os.system("cls")
        print(p)
        printn("python é uma linguagem versatil e simples.\n"
              "Dentre as linguagens de programação ela é a que mais se aproxima da linguagem humana\n"
              "e possui uma extensa biblioteca disponível para a utilização\n"
              "as informações do cursos estão presente em um drive da plataforma google\n"
              "podendo ser acessada pelo link: https://drive.google.com/file/d/10Xhau4Y3sPArrp1ahwyaglzJuukGogt-/view?usp=sharing \n"
              "\n"
              "\n"
              "Após a realização do curso haverá um questionário sobre a matéria e uma avaliação do curso")
        mostrar_video_curso1()
        mostrar_pasta_curso1()
        print(p)
        time.sleep(15)
        resultado_questionario = Questionario_Pyhton()
        if resultado_questionario == 1:
            printn("Iniciando o questionário de Python...")

    elif opcao2 == 2:
        time.sleep(5)
        os.system("cls")
        print(p)
        printn("Você escolheu o Curso de Educação Digital e Inclusão Tecnológica.")
        print(p)
        time.sleep(4)
        os.system("cls")
        print(p)
        printn("Este curso aborda o uso de tecnologias para promover a inclusão digital\n"
              "e ensinar habilidades digitais essenciais para o mundo moderno.\n"
              "As informações do curso estão disponíveis em um drive da plataforma Google\n"
              "podendo ser acessadas pelo link: https://drive.google.com/drive/folders/1Y7BI0Iitx4R1G5_vFlpQgFoYG09wJPXR?usp=sharing \n"
              "\n"
              "\n"
              "Após a realização do curso, haverá um questionário sobre a matéria e uma avaliação do curso.")
        print(p)
        mostrar_video_curso2()
        mostrar_pasta_curso2()
        time.sleep(5)
        resultado_questionario = Questionario_Educacao_Digital()
        if resultado_questionario == 1:
            printn("Iniciando o questionário de Educação Digital...")

def começo():
    os.system("cls")
    print(p)
    printn("Vamos começar")
    print(p)
    time.sleep(5)

def Questionario_Pyhton():
    os.system("cls")
    print(p)
    printn("Bem vindo ao questionário")
    print(p)
    printn("Haverá 3 questões sendo que cada questão tera uma alternativa correta dentre 4")
    print(p)
    printn("digite [1] para começar [2] para retonar")
    try:
        começar = int(inputn("Digite sua resposta: "))
        if começar == 1:
            return 1
        elif começar == 2:
            return 2
        else:
            printn("Opção inválida. Tente novamente.")
            time.sleep(2)
            return Questionario_Pyhton()
    except ValueError:
        printn("Entrada inválida. Por favor, digite um número.")
        time.sleep(2)
        return Questionario_Pyhton()

def salvar_respostas(user_id, respostas, curso):
    salvar_respostas_json(user_id, respostas, curso)

def Questionario_Educacao_Digital():
    os.system("cls")
    print(p)
    printn("Bem-vindo ao questionário sobre Educação Digital e Inclusão Tecnológica")
    print(p)
    printn("Haverá 3 questões, sendo que cada questão terá uma alternativa correta dentre 4")
    print(p)
    printn("Digite [1] para começar ou [2] para retornar")
    try:
        comecar = int(inputn("Digite sua resposta: "))
        if comecar == 1:
            return 1
        elif comecar == 2:
            return 2
        else:
            printn("Opção inválida. Tente novamente.")
            time.sleep(2)
            return Questionario_Educacao_Digital()
    except ValueError:
        printn("Entrada inválida. Por favor, digite um número.")
        time.sleep(2)
        return Questionario_Educacao_Digital()

def encerramento():
    print(p)
    printn("Agradecemos sua participação e desejamos que recomende para mais pessoas")
    print(p)
    time.sleep(5)
    os.system("cls")
    print(p)
    retorna = inputn(" Caso deseje retornar digite 1\n"
                    " Caso deseje encerrar digite 2\n" \
                    f"{p}\n"
                    "Digite: ")
    print(p)
    if retorna == "1":
        print(p)
        printn("Voltando para opções de curso")
        print(p)
        return 1
    elif retorna == "2":
        exit()
    else:
        printn("Opção inválida! Tente novamente.")
        time.sleep(2)
        return encerramento()

# ==================== Fluxo principal ====================
tela_inicio()
while True:
    intro = repcadastro()
    if intro == 1:
        abrir_usuario()
        break
    elif intro == 2:
        choice = info_cadastro_inicio()
        if choice == 1:
            registro_usuario()
            break
        else:
            fim_programa()
            break
    elif intro == 3:
        configuracoes()
    else:
        print("Opção inválida! Tente novamente.")
        narrar("Opção inválida! Tente novamente.")
        time.sleep(2)
        tela_inicio()

while True:
    opcao2 = cursos()
    cursoes(opcao2)

    if opcao2 == 1:
        resultado_questionario = Questionario_Pyhton()
        if resultado_questionario == 1:
            os.system("cls")
            print(p)
            printn("Vamos começar o questionário de Python!")
            print(p)
            time.sleep(2)
            respostas = []
            pergunta1 = inputn("Qual a origem do python ?\n"
                              "a) Serie\n"
                              "b) Animal\n"
                              "c) Filme\n"
                              "d) Indicação\n"
                              f'{p}\n'
                              "Digite sua resposta (a, b, c ou d): ").lower()
            respostas.append(pergunta1)
            if pergunta1 == 'a':
                print(p)
                printn("Resposta correta!")
                print(p)
            else:
                print(p)
                printn("Resposta incorreta!")
                print(p)
            time.sleep(2)
            os.system("cls")
            print(p)
            printn("Agora vamos para a segunda pergunta")
            print(p)
            time.sleep(2)
            pergunta2 = inputn("Qual é a linguagem de programação mais popular?\n"
                              "a) Python\n"
                              "b) Java\n"
                              "c) C++\n"
                              "d) Ruby\n"
                              f'{p}\n'
                              "Digite sua resposta (a, b, c ou d): ").lower()
            respostas.append(pergunta2)
            if pergunta2 == 'a':
                print(p)
                printn("Resposta correta!")
                print(p)
            else:
                print(p)
                printn("Resposta incorreta!")
                print(p)
            time.sleep(2)
            os.system("cls")
            print(p)
            printn("Agora vamos para a terceira pergunta")
            print(p)
            time.sleep(2)
            pergunta3 = inputn("Qual é a função que serva para exibir dados na tela?\n"
                              "a) time.sleep\n"
                              "b) if\n"
                              "c) Def\n"
                              "d) Print\n"
                              f'{p}\n'
                              "Digite sua resposta (a, b, c ou d): ").lower()
            respostas.append(pergunta3)
            if pergunta3 == 'd':
                print(p)
                printn("Resposta correta!")
                print(p)
            else:
                print(p)
                printn("Resposta incorreta!")
                print(p)
            time.sleep(2)
            os.system("cls")
            salvar_respostas(usuario_logado_id, respostas, "Curso de Python")
            printn("Respostas salvas com sucesso!")
            time.sleep(5)
            os.system("cls")
            resultado_encerramento = encerramento()
            if resultado_encerramento == 2:
                break

    elif opcao2 == 2:
        resultado_questionario = Questionario_Educacao_Digital()
        if resultado_questionario == 1:
            os.system("cls")
            print(p)
            printn("Vamos começar o questionário de Educação Digital!")
            print(p)
            time.sleep(2)
            respostas = []
            pergunta1 = inputn("O que é Educação Digital?\n"
                              "a) Uso de tecnologias para ensinar e aprender\n"
                              "b) Ensino de programação apenas\n"
                              "c) Uso de livros físicos em sala de aula\n"
                              "d) Ensino de matemática avançada\n"
                              f'{p}\n'
                              "Digite sua resposta (a, b, c ou d): ").lower()
            respostas.append(pergunta1)
            if pergunta1 == 'a':
                print(p)
                printn("Resposta correta!")
                print(p)
            else:
                print(p)
                printn("Resposta incorreta!")
                print(p)
            time.sleep(2)
            os.system("cls")
            print(p)
            printn("Agora vamos para a segunda pergunta")
            print(p)
            time.sleep(2)
            pergunta2 = inputn("Qual é o principal objetivo da Inclusão Tecnológica?\n"
                              "a) Garantir acesso à internet para todos\n"
                              "b) Ensinar apenas programação\n"
                              "c) Substituir professores por máquinas\n"
                              "d) Criar redes sociais\n"
                              f'{p}\n'
                              "Digite sua resposta (a, b, c ou d): ").lower()
            respostas.append(pergunta2)
            if pergunta2 == 'a':
                print(p)
                printn("Resposta correta!")
                print(p)
            else:
                print(p)
                printn("Resposta incorreta!")
                print(p)
            time.sleep(2)
            os.system("cls")
            print(p)
            printn("Agora vamos para a terceira pergunta")
            print(p)
            time.sleep(2)
            pergunta3 = inputn("Qual é um exemplo de ferramenta de Educação Digital?\n"
                              "a) Lousa tradicional\n"
                              "b) Plataforma de ensino online\n"
                              "c) Calculadora\n"
                              "d) Caderno\n"
                              f'{p}\n'
                              "Digite sua resposta (a, b, c ou d): ").lower()
            respostas.append(pergunta3)
            if pergunta3 == 'b':
                print(p)
                printn("Resposta correta!")
                print(p)
            else:
                print(p)
                printn("Resposta incorreta!")
                print(p)
            time.sleep(2)
            os.system("cls")
            salvar_respostas(usuario_logado_id, respostas, "Educacao_Digital_e_Inclusao_Tecnologica")
            printn("Respostas salvas com sucesso!")
            time.sleep(5)
            os.system("cls")
            resultado_encerramento = encerramento()
            if resultado_encerramento == 2:
                break