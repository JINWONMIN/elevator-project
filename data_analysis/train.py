#%%
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA
from pandas.core import datetools

series = pd.read_csv(r'./seq.csv', header=0, index_col=0, squeeze=True)

#series.plot()
plot_acf(series)
plot_pacf(series)
#plt.show()
"""

diff_1=series.diff(periods=1).iloc[1:]
#diff_1.plot()
plot_acf(diff_1)
plot_pacf(diff_1)
#plt.show()

"""

model = ARIMA(series, order=(0,0,2))
model_fit = model.fit(trend='nc',full_output=True, disp=1)
print(model_fit.summary())
fore = model_fit.forecast(steps=3)
model_fit.plot_predict()
print(fore)