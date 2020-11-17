# %%
from keras.models import load_model
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import time
from keras.layers import RepeatVector
from keras.layers import TimeDistributed

APP_DIR = os.path.dirname(__file__)
base_dir = os.path.dirname(APP_DIR)
windows_size = 48
n_features = 7
n_step_out = 3
model_path = f'{base_dir}/data/hotel_call_predict.h5'

# %%
def loadData(filepath):
    path = f'{base_dir}//data//{filepath}'
    df = pd.read_csv(path)
    df = df.loc[:, ['Date', 'Month','Day', 'Time', 'ProductRate',
                    'AHT', 'TotalCount']]
    data_size = len(df)
    X = list()
    Y = list()
    for i in range(data_size - windows_size - n_step_out):
        end = i+windows_size
        X.append(df.iloc[i:end, 0:n_features + 1].to_numpy())
        Y.append(df.iloc[end:end + n_step_out,
                         -1].to_numpy().reshape(3))
    return np.array(X), np.array(Y)

#%%
def getPlotData():
    path = f'{base_dir}//data//hotel_call.csv'
    df = pd.read_csv(path)
    df = df.loc[:, ['Date', 'Month','Day', 'Time', 'ProductRate',
                    'AHT', 'TotalCount']]
    X = list()
    Y = list()
    for row_index, row in df.iterrows():
        try:
            x = str(int(row[0])) +"-"+ str(int(row[1])) +"-"+ str(int(row[2])) + " " + str(int(row[3]))
            y = int(row['TotalCount'])
            X.append(x)
            Y.append(y)
        except Exception as ex:
            print("error row ,index:" , row_index)
    return X,Y 
#%%
x,y = getPlotData()
plt.plot(x,y)
plt.show()
# %%
print("prepare data...")
train_x, train_y = loadData("hotel_call.csv")
test_x, test_y = loadData("hotel_call_test.csv")
print("prepare data complete.")
# %%
print(train_x[0:2])
print(train_y[0:10])
# %%
def getModel():
    print("create model...")
    model = Sequential()
    model.add(LSTM(100, activation='relu', return_sequences=True,
                   input_shape=(windows_size, n_features)))
    model.add(LSTM(100, activation='relu'))
    model.add(Dense(n_step_out))
    model.compile(optimizer='adam', loss='mse')
    print("create model complete.")
    return model

# %%
print("strat training...")
time_start = time.time()
model = getModel()
# fit model
model.fit(train_x, train_y, epochs=10, batch_size=200)
time_end = time.time()
model.save(model_path)
print("train success,cost:", time_end-time_start)

# %%
print("evaluate model...")
result = model.evaluate(test_x, test_y)
print('result', result)
print("evaluate model complete.")
# %%
train_model = load_model(model_path)
intput = test_x[0].reshape((1, windows_size, n_features))
# %%
yhat = train_model.predict(intput, verbose=0)
print("predict:", yhat)
print("real", test_y[0])
