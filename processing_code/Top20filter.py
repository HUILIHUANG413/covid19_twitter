import pandas as pd
import os
import sys
from textblob import TextBlob
from langdetect import detect


pathN = "D:/Fall2021/CSE6242" + "/" + "6242Project/covid19_twitter/dailies/"
ori_savePath ="D:/Fall2021/CSE6242" + "/" + "6242Project/covid19_twitter/" + "Top20_daily/"

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


#
for file in os.listdir(directory):
     file_tmp = str(file)
     file_tmp = file_tmp[2:-1]
     foldername = pathN + file_tmp + "/"
     for subfile in os.listdir(foldername):
        filename = os.fsdecode(subfile)
        if filename.endswith("trigrams.csv"):
            data = pd.read_csv(foldername + filename, header=None,names=['gram','counts'],skiprows = 0, nrows =30)
            data = data[1:]
            savePath = ori_savePath + filename[:-4]+ "_top20.csv"
            data.to_csv(savePath,index=False)
        else:
            continue
