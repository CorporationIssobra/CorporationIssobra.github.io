def converter_txt_para_chave_valor(caminho_entrada, caminho_saida):
    with open(caminho_entrada, 'r', encoding='utf-8') as arquivo_entrada:
        linhas = arquivo_entrada.readlines()
    
    pares = []
    for linha in linhas:
        nivel, exp = linha.strip().split('\t')
        nivel_sem_virgula = nivel.replace(',', '')
        exp_sem_virgula = exp.replace(',', '')
        pares.append(f"{nivel_sem_virgula}: {exp_sem_virgula}")
    
    with open(caminho_saida, 'w', encoding='utf-8') as arquivo_saida:
        arquivo_saida.write(", ".join(pares))

converter_txt_para_chave_valor(
    caminho_entrada='xpt.txt',
    caminho_saida='xpt2.txt'
)

print("Conversão concluída! Verifique o arquivo de saída.")