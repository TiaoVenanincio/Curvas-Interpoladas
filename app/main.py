from fastapi import FastAPI, Query
from app.curva import Curva

app = FastAPI(title="API de Curva Financeira Interpolada")

curva = Curva("data/curva_simulada.csv")

@app.get("/curva/interpolada")
def obter_taxa(prazo_dias: int = Query(..., gt=0)):
    taxa = curva.taxa_para_prazo(prazo_dias)
    return {
        "prazo_dias": prazo_dias,
        "taxa_percentual_interpolada": round(taxa, 4)
    }