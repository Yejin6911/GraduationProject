import pandas as pd

pd.set_option('display.max_colwidth', -1)
df = pd.read_csv("./map/static/금천구.csv", encoding='cp949')
df_2 = pd.read_csv("./map/static/관악구.csv", encoding='cp949')

#excluded = df[df['설치목적구분'].str.contains('재난재해')==True].index
# df = df.drop(excluded)
df.columns = ["management", "S_address", "L_address", "purpose", "camera_num", "camera_pixel", "shoot_info", "storage_days", "installed_date", "phone", "latitude", "longitude", "data_date"]
df['station'] = "서울금천경찰서"
df.to_csv("./map/static/data/서울금천경찰서.csv", mode="a", index=False, header=True, encoding="utf-8")

df_2.columns = ["management", "S_address", "L_address", "purpose", "camera_num", "camera_pixel", "shoot_info", "storage_days", "installed_date", "phone", "latitude", "longitude", "data_date"]
df_2['station'] = "서울금천경찰서"
df_2 = df_2[df_2["S_address"].str.contains('조원동')==True]
df.to_csv("./map/static/data/서울금천경찰서.csv", mode="a", index=False, header=False, encoding="utf-8")
