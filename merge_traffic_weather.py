import pandas as pd

df_traffic = pd.read_csv("Agregacion2.csv")
df_traffic["fecha"] = pd.to_datetime(df_traffic["fecha"])

df_weather = pd.read_csv("climatologia_2023_2025.csv")
df_weather["fecha"] = pd.to_datetime(df_weather["fecha"], dayfirst=True)

for col in ["tmed", "prec", "tmin", "tmax", "sol"]:
    df_weather[col] = df_weather[col].str.replace(",", ".").astype(float)

df_combined = pd.merge(df_traffic, df_weather, on="fecha", how="inner")

df_combined.to_csv("datos_combinados_limpios.csv", index=False)

print(f"Traffic rows: {len(df_traffic)}")
print(f"Weather rows: {len(df_weather)}")
print(f"Combined rows: {len(df_combined)}")
print(f"\nColumns: {list(df_combined.columns)}")
print(f"\nSaved to datos_combinados_limpios.csv")
