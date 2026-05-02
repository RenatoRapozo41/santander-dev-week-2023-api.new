def gerar_mensagem(usuario):
    saldo = usuario["saldo"]
    nome = usuario["nome"]

    if saldo > 2000:
        return f"Olá {nome}, você está com um ótimo saldo! Que tal investir?"
    elif saldo > 1000:
        return f"Oi {nome}, seu saldo está estável. Continue assim!"
    else:
        return f"{nome}, atenção ao seu saldo. Que tal revisar seus gastos?"