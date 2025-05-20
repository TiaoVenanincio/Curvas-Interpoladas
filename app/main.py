from fastapi import FastAPI, Query
from app.curva import Curva
from datetime import datetime, timedelta

app = FastAPI(title="API de Curva Financeira Interpolada")

curva = Curva("data/curva_simulada.csv")

@app.get("/curva/interpolada")
def obter_taxa(prazo_dias: int = Query(..., gt=0)):
    taxa = curva.taxa_para_prazo(prazo_dias)
    return {
        "prazo_dias": prazo_dias,
        "taxa_percentual_interpolada": round(taxa, 4)
    }

@app.get("/curva/completa")
def obter_taxa_n_pontos(qtd_pontos: int = Query(..., gt=0)):
    data_valor = {}
    hoje = datetime.now().date()
    for i in range(1, qtd_pontos):
        data_ponto = hoje + timedelta(days=i)
        data_valor[data_ponto.strftime('%d/%m/%Y')] = curva.taxa_para_prazo(i)
    return data_valor
