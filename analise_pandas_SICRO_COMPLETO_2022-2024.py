import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("SICRO_COMPLETO_2022-2024.xlsx")
df = df.dropna()
print(df)