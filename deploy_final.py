# deploy_final.py
from cog.command.push import push
import os

print("Iniciando deploy oficial via Cog...")

try:
    # Fazer push do modelo
    push(
        model="aiaprendefacil-hugo/lele",
        directory=".",
        token=os.getenv("REPLICATE_API_TOKEN")
    )
    print("Deploy concluido com sucesso!")
    
except Exception as e:
    print("Erro no deploy:", e)