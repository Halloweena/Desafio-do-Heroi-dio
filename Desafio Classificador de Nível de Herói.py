def saudacao_por_nivel(nivel):
    if nivel <= 1000:
        return "Ferro"
    elif nivel >= 1001 and nivel <= 2000:
        return "Bronze"
    elif nivel >= 2001 and nivel <= 5000:
        return "Prata"
    elif nivel >= 5001 and nivel <= 7000:
        return "Ouro"
    elif nivel >= 7001 and nivel <= 8000:
        return "Platina"
    elif nivel >= 8001 and nivel <= 9000:
        return "Ascendente"
    elif nivel >= 9001 and nivel <= 10000:
        return "Imortal"
    elif nivel >= 10001:
        return "Radiante"

def main():
    nome = input("Olá Herói! Qual o seu nome? ")
    print("Bem vindo(a)", nome, "!")

    while True:
        try:
            nivel = int(input("Qual o seu nível (em números)? "))
            saudacao = saudacao_por_nivel(nivel)
            print("O Herói de nome " + nome + " está no nível " + saudacao + "!")
            break
        except ValueError:
            print("Erro: Seu nível deve conter apenas números.")

if __name__ == "__main__":
    main()