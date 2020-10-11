import pandas as pd

pd.set_option("display.max_colwidth",-1)

df = pd.read_csv("./map/static/은평구.csv", encoding="cp949")

keywords = [ "녹번동", "수색동", "신사동", "응암동", "증산동" ]

# df = df[df["관리기관명"].str.contains("서울특별시 종로구청")==True]
# for keyword in keywords_2:
#     excluded_2 = df[(df["소재지도로명주소"].str.contains(keyword) == True) | (df["소재지지번주소"].str.contains(keyword) == True)].index
#     df = df.drop(excluded_2)
#
# df= df.drop(['제공기관코드','제공기관명'], axis=1)

df.columns = ["management", "S_address", "L_address", "purpose", "camera_num", "camera_pixel", "shoot_info", "storage_days", "installed_date", "phone", "latitude", "longitude", "data_date"]
df['station'] = "서울서부경찰서"
count=1

for keyword in keywords:
    dfFiltered = df[(df["S_address"].str.contains(keyword)==True)|(df["L_address"].str.contains(keyword)==True)]
    print(keyword,dfFiltered)
    if len(dfFiltered)>0:
        if count==1:
            dfFiltered.to_csv("./map/static/data/서울서부경찰서.csv", mode="a", index=False, header=True, encoding="utf-8")
        else:
            dfFiltered.to_csv("./map/static/data/서울서부경찰서.csv", mode="a", index=False, header=False, encoding="utf-8")
    count+=1
