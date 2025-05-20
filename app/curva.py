import pandas as pd
from scipy.interpolate import interp1d

class Curva:
    def __init__(self, caminho_csv: str):
        df = pd.read_csv(caminho_csv)
        self.prazos = df["prazo_dias"].values
        self.taxas = df["taxa_percentual"].values
        self.interpolador = interp1d(self.prazos, self.taxas, kind="linear", fill_value="extrapolate")

    def taxa_para_prazo(self, prazo_dias: int) -> float:
        return float(self.interpolador(prazo_dias))
