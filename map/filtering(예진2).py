import pandas as pd

pd.set_option("display.max_colwidth",-1)

df = pd.read_csv("./map/static/전국.csv", encoding="cp949")

keywords = [ "권농동", "동숭동", "명륜동", "봉익동", "숭인동", "연건동", "연지동", "예지동", "원남동", "이화동", "인의동", "장사동",
             "종로4가", "종로5가", "종로6가", "창신동", "충신동", "혜화동", "홍제동", "훈정동", "묘동", "와룡동", "종로3가"]

keywords_2 = ["돈화문로 27", "돈화문로 29", "돈화문로 29-1", "돈화문로 지하 30", "돈화문로 지하 31", "돈화문로 지하 33", "돈화문로 지하 33-1",
"돈화문로 지하 35", "돈화문로 지하 35-1", "돈화문로 지하 37", "돈화문로 지하 37-1", "돈화문로 지하 39-1", "돈화문로 지하 41", "돈화문로 지하 41-1",
"돈화문로 지하 45", "돈화문로 지하 47", "돈화문로 지하 49", "돈화문로 지하 49-1", "돈화문로 지하 51", "돈화문로 지하 51-1", "돈화문로 지하 53",
"돈화문로 지하 53-1", "돈화문로 지하 53-2", "돈화문로 지하 55", "돈화문로 지하 55-1", "돈화문로 지하 57", "돈화문로 지하 59", "돈화문로 지하 59-1",
"돈화문로 지하 61", "돈화문로 지하 63", "돈화문로 지하 63-1", "돈화문로 11길 2", "돈화문로 5가길 4", "돈화문로 11가길 16-1", "돈화문로 9길 2",
"돈화문로 65", "돈화문로 67", "돈화문로 69", "돈화문로 69-1", "돈화문로 69-2", "돈화문로 71", "돈화문로 73", "돈화문로 79", "돈화문로 81", "돈화문로 81-1",
"돈화문로 83", "돈화문로 83-1", "돈화문로 83-2", "돈화문로 85", "돈화문로 89", "돈화문로 93", "돈화문로 97", "돈화문로 11가길 46", "돈화문로 11가길 48",
"삼일대로30길 56", "율곡로 96", "돈화문로 23", "돈화문로 25", "수표로 98", "수표로 104", "수표로20길 7", "수표로20길 9", "수표로20길 13", "수표로20길 15",
"수표로20길 17", "수표로20길 33", "수표로20길 39", "수표로20길 43", "종로 108", "종로 109", "종로 110", "종로 111", "종로 112", "종로 113", "종로 114",
"종로 115", "종로 116", "종로 117", "종로 118", "종로 119", "종로 120", "종로 121", "종로 122", "종로 123", "종로 124", "종로 125", "종로 126", "종로 127",
"종로 128", "종로 지하 129"]

df = df[df["관리기관명"].str.contains("서울특별시 종로구청")==True]

for keyword in keywords_2:
    excluded_2 = df[(df["소재지도로명주소"].str.contains(keyword) == True) | (df["소재지지번주소"].str.contains(keyword) == True)].index
    df = df.drop(excluded_2)

df= df.drop(['제공기관코드','제공기관명'], axis=1)

df.columns = ["management", "S_address", "L_address", "purpose", "camera_num", "camera_pixel", "shoot_info", "storage_days", "installed_date", "phone", "latitude", "longitude", "data_date"]
print(df)
count=1

for keyword in keywords:
    dfFiltered = df[(df["S_address"].str.contains(keyword)==True)|(df["L_address"].str.contains(keyword)==True)]
    print(keyword,dfFiltered)
    if len(dfFiltered)>0:
        if count==1:
            dfFiltered.to_csv("./map/static/data/서울혜화경찰서.csv", mode="a", index=False, header=True, encoding="utf-8")
        else:
            dfFiltered.to_csv("./map/static/data/서울혜화경찰서.csv", mode="a", index=False, header=False, encoding="utf-8")
    count+=1
