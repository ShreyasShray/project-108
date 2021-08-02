import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("project108.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Average"])
fig.show()