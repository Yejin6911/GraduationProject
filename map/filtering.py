import pandas as pd

# pd.set_option('display.max_colwidth', -1)
df = pd.read_csv("./map/static/data/전국.csv", encoding='cp949')

keywords= ['서울특별시 금천구']

df= df.drop(['제공기관코드','제공기관명'], axis=1)

excluded = df[df['설치목적구분'].str.contains('생활방범') == False].index
df = df.drop(excluded)

excluded = df[df['설치목적구분'].str.contains('재난재해')==True].index
df = df.drop(excluded)
df.columns = ["management", "S_address", "L_address", "purpose", "camera_num", "camera_pixel", "shoot_info", "storage_days", "installed_date", "phone", "latitude", "longitude", "data_date"]

count=1
for keyword in keywords:
    dfFiltered = df[(df["S_address"].str.contains(keyword)==True)|(df["L_address"].str.contains(keyword)==True)]
    if len(dfFiltered)>0:
        print(dfFiltered)
        if count==1:
            dfFiltered.to_csv("./map/static/data/금천금천.csv", mode="a", index=False, header=True, encoding="utf-8")
        else:
            dfFiltered.to_csv("./map/static/data/금천금천.csv", mode="a", index=False, header=False, encoding="utf-8")
    count+=1