import numpy as np
from keras.layers import Dense, Activation
from keras.layers.recurrent import LSTM
from keras.models import Sequential

file_path = './03.dataset.csv'

raw_data = np.loadtxt(file_path, delimiter=',')
X = raw_data[:, 0:-1]
Y = raw_data[:,[-1]]
trX = X[0:500]#np.reshape(X[0:500], (500,1,3))
print(trX)
trY = Y[0:500]
teX = X[500:]#np.reshape(X[500:], (289,1,3))
teY = Y[500:]

model = Sequential()
model.add(Dense(3, input_dim=3))
model.add(Dense(1))
model.add(Activation('linear'))
model.summary()

model.compile(optimizer='adam', loss='mse')
model.fit(x=trX, y=trY, epochs=100, verbose=2)
