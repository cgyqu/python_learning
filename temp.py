import numpy as np
import pandas as pd
import jieba

def loadfile():
    fopen = open('data/hotel_train3.txt', 'r', encoding='utf-8')
    data = []
    for line in fopen:
        data.append(line.split()[1:3])
    y = np.hstack((data))
    return data, y
def getstopword():
    lines = open('data/stopword.txt', 'r', encoding='utf-8').readlines()
    words = []
    for line in lines:
        words.append(line.split('\n')[0])
    return words

stopwords = getstopword()
print(stopwords)


data, y = loadfile()
# print(data_array)
df = pd.DataFrame(data)
dict = {}
for name, group in df[1].groupby(df[0]):
    dict[name] = group
for key in dict.keys():
    print("key:" + key + ",length:" + str(len(dict[key])))

asks = df[1]
print(len(asks))

wordCount = {}

for ask in asks:
   words = jieba.cut(ask)
   for word in words:
       if(stopwords.count(word)>0):
           continue
       if wordCount.__contains__(word):
            wordCount[word] = wordCount[word] + 1
       else:
            wordCount[word] = 1
           
wordCount = sorted(wordCount.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
wordCount = list(filter(lambda m: m[1] > 10,wordCount))
sorted(wordCount , key=lambda x: x[1],reverse=True)

# print(wordCount)
# 拿到字符串编码
print(len(wordCount))
print(wordCount)
#np.zeros(len(wordCount))


