import pandas as pd

pd.set_option("display.max_colwidth",-1)
# #금천경찰서, 혜화경찰서, 성북경찰서 "서울서부경찰서""서울도봉경찰서"
# stations = ["서울중부경찰서", "서울종로경찰서", "서울남대문경찰서", "서울서대문경찰서", "서울용산경찰서", "서울동대문경찰서", "서울마포경찰서",
#             "서울영등포경찰서", "서울성동경찰서", "서울동작경찰서", "서울광진경찰서", "서울강북경찰서", "서울중랑경찰서", "서울강남경찰서",
#             "서울관악경찰서", "서울강서경찰서", "서울강동경찰서", "서울종암경찰서", "서울구로경찰서", "서울서초경찰서", "서울양천경찰서", "서울송파경찰서", "서울노원경찰서",
#             "서울방배경찰서", "서울은평경찰서", "서울수서경찰서"]
#
# for station in stations:
#     path = "./map/static/data/"+station+".csv"
#     df = pd.read_csv(path, encoding="utf-8")
#     df['station'] = station
#     df.to_csv(path, mode="w", index=False, header=True, encoding="utf-8")

df = pd.read_csv("./map/static/data/")
