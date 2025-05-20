# Curvas-Interpoladas
A ideia é criar um projeto com curvas financeiras interpoladas, como IPCA, DI Futuro, etc.

# Como rodar?
1. Crie um ambiente virtual e instale as dependências usando:
``` pip install -r requirements.txt ```

2. Rode o comando ``` uvicorn app.main:app --reload ``` para inicar a API.

3. Faça um teste com a seguinte URL:
``` http://127.0.0.1:8000/curva/interpolada?prazo_dias=100 ```