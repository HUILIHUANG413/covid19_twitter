import pandas as pd
import os
import sys
from langdetect import detect


pathN = "D:/COVID_PROJ" + "/" + "covid19_twitter/dailies/"
ori_savePath ="D:/COVID_PROJ" + "/" + "covid19_twitter/" + "Top30_daily/"

# def is_english(text):
#     # Add language detection code here
#     #lang = TextBlob(text)
#     tmp = detect(text)
#     if tmp == "en":
#         return True
#     else:
#         return False

# Get the path of current working directory
#path = os.getcwd()
directory = os.fsencode(pathN)
#result = pd.DataFrame(columns=['gram','counts'])
# arr = os.listdir()
# print(arr)

count = 0
#
for file in os.listdir(directory):

    #select dates

    # count += 1 
    # if count < 300 :
    #     continue
    # if count > 310 :
    #     break
    
    file_tmp = str(file)
    file_tmp = file_tmp[2:-1]
    foldername = pathN + file_tmp + "/"
    

    for subfile in os.listdir(foldername):
        filename = os.fsdecode(subfile)
        if filename.endswith("trigrams.csv"):
            data = pd.read_csv(foldername + filename, header=None,names=['gram','counts'],skiprows = 0, nrows =200)
            data = data[1:]
            
            drop_index = []
            for index, row in data.iterrows():
                # filter repeated covid/19 combo
                if row["gram"] != "covid 19":
                    if "covid" in row["gram"] or "Covid" in row["gram"] or "19" in row["gram"] or "corona" in row["gram"]:
                        drop_index.append(index)
                #filter ?
                if "?" in row["gram"]:
                    drop_index.append(index)
                #filter non-English
                try:
                    language = detect(row["gram"])
                except:
                    language = "error"
                if (row["gram"] != "covid 19" and  "vaccine" not in row["gram"] and language != "en"):
                    drop_index.append(index)
                #filter big numbers like ,000
                if ("000" in row["gram"] or "people" in row["gram"]):
                    drop_index.append(index)

            data.drop(labels = drop_index, axis = 0, inplace = True)
            savePath = ori_savePath + filename[:-4]+ "_top30.csv"
            data.to_csv(savePath,index=False)
            print(filename[:-4])
        else:
            continue
