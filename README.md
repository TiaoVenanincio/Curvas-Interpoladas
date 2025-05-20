# Curvas-Interpoladas
Este projeto tem como objetivo construir uma API para interpolação de curvas financeiras, como IPCA, DI Futuro, entre outras. Através de dados simulados ou reais, é possível consultar a taxa esperada para qualquer prazo, utilizando métodos de interpolação como o linear.


## Funcionalidades
- Interpolação de curvas com base em pontos discretos (vértices)
- API REST com FastAPI
- Suporte inicial a curva simulada via CSV


## Estrutura do Projeto
```bash
curvas-interpoladas/
├── app/
│ ├── main.py             # Ponto de entrada da API
│ ├── curva.py            # Módulo de interpolação
├── data/
│ └── curva_simulada.csv  # Arquivo com os vértices da curva
├── requirements.txt
├── README.md
```

## Como rodar o projeto localmente?

1. Crie um ambiente virtual e instale as dependências usando:
```bash
python -m venv .venv
source .venv/bin/activate       # Linux/macOS
.venv\Scripts\activate          # Windows
pip install -r requirements.txt 
```

2. Inicie a api com o seguinte comando:
``` bash
uvicorn app.main:app --reload
```

3. Faça um teste com a seguinte URL:
``` bash
http://127.0.0.1:8000/curva/interpolada?prazo_dias=100 
```

4.  Resposta esperada (exemplo):
``` bash
{
  "prazo_dias": 100,
  "taxa_percentual_interpolada": 10.7333
}
```