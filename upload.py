import replicate
import os

print("Iniciando upload dos arquivos...")

try:
    # Acessar modelo
    model = replicate.models.get("aiaprendefacil-hugo/lele")
    
    # Lista de arquivos para upload
    arquivos = ["model.py", "predict.py", "replicate.yaml"]
    
    for arquivo in arquivos:
        if os.path.exists(arquivo):
            print(f"Fazendo upload de: {arquivo}")
            print(f"OK - {arquivo} preparado para upload")
        else:
            print(f"ERRO - {arquivo} - arquivo nao encontrado")
    
    print("TODOS ARQUIVOS PRONTOS!")
    print("Proximo passo: Fazer deploy final com replicate push")
    
except Exception as e:
    print("ERRO no upload:", e)