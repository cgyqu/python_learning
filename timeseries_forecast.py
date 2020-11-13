#%%
import pandas as pd
import matplotlib.pyplot as plt
f = open('./data/hotel_call.csv')
df = pd.read_csv(f,usecols=['Time','ProductRate','AHT','TotalCount','NextTimeCount'])
#%%
print(df.size)
print(df.index.stop)

#%%
import tensorflow as tf
# %%
from numpy import array
from numpy import hstack
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense

# %%
