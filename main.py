from data import obter_usuarios
from ai_service import gerar_mensagem

def main():
    usuarios = obter_usuarios()

    print("=== GERANDO MENSAGENS ===\n")

    for usuario in usuarios:
        mensagem = gerar_mensagem(usuario)

        print(f"Usuário: {usuario['nome']}")
        print(f"Mensagem: {mensagem}")
        print("-" * 40)

if __name__ == "__main__":
    main()