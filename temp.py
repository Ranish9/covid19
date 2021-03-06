import plotly
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
excel_file = 'animate.xlsx'
df = pd.read_excel(excel_file)
print(df)
data = [go.Scatter( x=df['Date'], y=df['fulldeaths'])]
fig = go.Figure(data)
plotly.offline.plot(fig, filename="fulldeaths.html")
