import pandas_datareader.data as web
import datetime
import pandas as pd
import dash
import numpy as np
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

#data1 = [1,2,3,4,5,6,7]
df = pd.DataFrame(data=['London', 'Bristol', 'Leeds', 'Manchester', 'Bath', 'Reading', 'Peterborough'], columns=['names'])
data = [1,2,3,4,5,6,7]
df['values'] = pd.DataFrame(data)
df['city'] = df['names']
df =df.set_index('names')
#print(df)
print(df[df["city"].isin(["Bristol", "London"])])