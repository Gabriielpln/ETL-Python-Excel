# Pandas pra ler csv e transformar em Dataframe
import pandas as pd

# pandas profiling
from ydata_profiling import ProfileReport 

df = pd.read_csv("data.csv")
profile = ProfileReport(df, title="Profiling Report")
profile.to_file("output.html")
