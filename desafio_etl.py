import pandas as pd

df = pd.read_csv('sdw2023_usuarios.csv')
print("Dados extraídos com sucesso!")

def gerar_oferta(linha):
    nome = linha['Nome']
    limite = linha['Limite']
    
    if limite > 2000:
        return f"Olá {nome}, você foi selecionado para nosso fundo de investimento VIP!"
    else:
        return f"Olá {nome}, que tal um microcrédito para impulsionar seus planos?"

df['Mensagem_Marketing'] = df.apply(gerar_oferta, axis=1)
print("Transformação concluída!")

df.to_csv('sdw2023_resultado.csv', index=False)
print("Dados carregados no arquivo final: sdw2023_resultado.csv")