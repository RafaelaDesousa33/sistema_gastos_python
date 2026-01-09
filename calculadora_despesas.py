from colorama import Fore,Style,init

init(autoreset=True)


TITULO = Fore.CYAN + Style.BRIGHT
INPUT = Fore.YELLOW
SUCESSO = Fore.GREEN
ERRO = Fore.RED
INFO = Fore.WHITE

############################
# FUNÇÕES DE GASTO
############################

print(TITULO + "\n=== CONTROLE DE GASTOS ===\n")

def alimentacao(gasto, produto):
    def calcular(saldo):
        return saldo - gasto, gasto,produto
    return calcular

def transporte(gasto, meio_transporte):
    def calcular(saldo):
        return saldo - gasto, gasto, meio_transporte
    return calcular

def lazer(gasto, atividade):
    def calcular(saldo):
        return saldo - gasto, gasto, atividade
    return calcular


############################
# CMD - USUÁRIO
############################

saldo_usuario = float(input(INPUT + "Digite seu saldo inicial: "))
nome_usuario = input(INPUT + "Digite seu nome:")

while True:

    entrada = input(
        INFO + "[E]" + SUCESSO + "Entrar:" +
        INFO + " | [S] " + ERRO + "Sair:"
    ).lower().strip()

    if entrada == "s":
        print("Programa encerrado")
        break

    elif entrada == "e":
        categoria = input("Categoria (lazer, transporte, alimentacao): ").lower()

        if categoria == "lazer":
            atividade = input("Atividade: ")
            gasto = float(input("Gasto: "))
            operacao = lazer(gasto, atividade)

        elif categoria == "alimentacao":
            produto = input("Alimentação: ")
            gasto = float(input("Gasto: "))
            operacao = alimentacao(gasto, produto)

        elif categoria == "transporte":
            meio = input("Transporte: ")
            gasto = float(input("Gasto: "))
            operacao = transporte(gasto, meio)

        else:
            print("Categoria inválida")
            continue


        saldo_anterior = saldo_usuario
        saldo_usuario,gasto,detalhe = operacao(saldo_usuario)
        ###############
        #DICIONARIO DE GASTOS
        #################
        dicionario_gastos = {
            "nome_usuario": nome_usuario,
            "categoria": categoria,
            "detalhe" : detalhe,
            "saldo_anterior": saldo_anterior,
            "saldo_atual": saldo_usuario,
            "gasto" : gasto
            
        }
       
        print(TITULO + "\n--- REGISTRO DE GASTOS ---")
        for chave,valor in  dicionario_gastos.items():
            print(f"{chave}:{valor}")


    else:
        print("Digite uma escolha válida")
