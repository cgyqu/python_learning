#-- coding: utf-8 --
#%%
from gensim.models import Word2Vec
import os
import numpy as np
import jieba
#%% 
def loadData():
    fopen = open('../data/hotel_train3.txt', 'r',encoding='utf-8')
    data = []
    for line in fopen.readlines():
        data.append(line.replace('\n','').split('\t')[1:3])
    data_array = np.array(data)
    return data_array

#%% 
words=[]
datas = loadData()
#%%
stopwords = []
with open('../data/stopword.txt', 'r',encoding='utf-8') as f:
    for word in f.readlines():
        stopwords.append(word.replace("\n",""))
stopwords.append('\n')
stopwords.append('\t')
stopwords.append('\r\n')
stopwords.append('\r')
print(stopwords)

#%%
temp = [word for word in jieba.cut(datas[0,1])]
print(temp)
#%%
for data in datas:
    cuts = jieba.cut(data[1].replace("\n",""))
    for word in cuts:
        if word not in stopwords:
             words.append(word)
print(len(words))
with open('../data/hotel_words.txt', 'w',encoding='utf-8') as f:
    f.write(" ".join(words))

# %%
model = Word2Vec([words], min_count=5)
dataPath = "../data/word2vec.model"
model.save(dataPath)
# %%
#加载模型
model = Word2Vec.load(dataPath)
vector = model['啊']
print(vector)

# %%
testwords = ['预订','电话','地址']
for i in range(len(testwords)) :
    res = model.wv.most_similar(testwords[i])
    print (testwords[i])
    print (res)
# %%