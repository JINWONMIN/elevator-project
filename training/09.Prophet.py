import pandas as pd
import numpy as np
from fbprophet import Prophet
import matplotlib.pyplot as plt

dataset = pd.read_csv('09.csv')
#dataset['y'] = np.log(dataset['y'])

# split into train and test sets
train_size = int(len(dataset) * 0.7)
test_size = len(dataset) - train_size
train, test = dataset.iloc[0:train_size,:], dataset.iloc[train_size:,:]

model = Prophet().fit(train)

future = model.make_future_dataframe(periods=test_size, freq='M')
testPredict = model.predict(future)
model.plot(testPredict)
fig2 = model.plot_components(testPredict)

# plot baseline and predictions

#plt.plot(testPredict)
#plt.show()
#plt.savefig('10.result.png')
