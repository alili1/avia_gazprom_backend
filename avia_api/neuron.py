import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np


file = 'Data_Train.xlsx'


xl = pd.ExcelFile(file)

df = xl.parse('Sheet1')


model = Sequential()
model.add(Dense(64, input_shape=(None, 4), activation='relu'))
model.add(Dense(10, activation='linear'))
model.add(Dense(5, activation='linear'))
model.add(Dense(1, activation='linear'))

# Обучаем нейронную сеть
model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
model.fit(df[['Airline', 'Source', 'Destination', 'Duration']], df['Price'], epochs=50, batch_size=93)

# Делаем прогноз
print(model)
print(model.predict([[1, 1, 2, 170]]))