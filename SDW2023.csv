import pandas as pd
import os

def load_csv(usuarios, arquivo_saida='output/saida.csv'):
    os.makedirs('output', exist_ok=True)

    dados = []

    for user in usuarios:
        dados.append({
            "id": user.get("id"),
            "nome": user.get("name") or user.get("nome"),
            "saldo": user.get("saldo"),
            "mensagem": user["news"][0]["message"]
        })

    df = pd.DataFrame(dados)
    df.to_csv(arquivo_saida, index=False, encoding='utf-8-sig')