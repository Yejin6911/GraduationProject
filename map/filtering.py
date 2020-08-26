import pandas as pd

pd.set_option('display.max_colwidth',-1)

df = pd.read_csv("./map/static/data/관악구.csv", encoding='cp949')

keywords = ["관악구 조원동"]

for keyword in keywords:
    dfFiltered = df[(df['소재지지번주소'].str.contains(keyword)==True) | (df['소재지도로명주소'].str.contains(keyword)==True)]
    if(len(dfFiltered)>0):
        print(dfFiltered)

df.to_excel("./map/static/data/서울금천경찰서.xlsx",sheet_name="Sheet1")