from fastapi import FastAPI

app = FastAPI()

filas = {}

@app.post("/empresa/{empresa_id}/entrar")
def entrar_na_fila(empresa_id: str, nome: str):
    if empresa_id not in filas:
        filas[empresa_id] = []
    filas[empresa_id].append(nome)
    posicao = len(filas[empresa_id])
    return {"mensagem": f"{nome} entrou na fila", "posicao": posicao}

@app.get("/empresa/{empresa_id}/fila")
def ver_fila(empresa_id: str):
    fila = filas.get(empresa_id, [])
    return {"fila": fila, "total": len(fila)}

@app.delete("/empresa/{empresa_id}/chamar")
def chamar_proximo(empresa_id: str):
    if empresa_id not in filas or len(filas[empresa_id]) == 0:
        return {"mensagem": "Fila vazia"}
    proximo = filas[empresa_id].pop(0)
    return {"mensagem": f"Chamando {proximo}", "restantes": len(filas[empresa_id])}