import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout

# Load the input data to build the model
data = open('ai/stock-prediction/stock-prediction.txt')

# Initial data
m = 100 # dollar
k = 10 # stocks

name = []
owned = []
all_prices = []

for i in range(10):
    newline = data.readline().split()
    name.append(newline[0])
    all_prices.append(list(map(float, newline[1:])))

d =  len(all_prices[0]) # days remaining



# Features are every subgroup of 5 prices
# y = the price on day 6 - the price on day 5
# Lets pool all stocks for now, the stocks given in the test won't be all the same

def createDatasets(all_prices):
    # Create X and y
    X = []
    y = []
    for prices in all_prices:
        for i, _ in enumerate(prices):
            if i == 499:
                break
            X.append(prices[i:i+5])
            y.append(prices[i+6] - prices[i+5])

    X = np.array(X)
    y = np.array(y)
    return X, y

X, y = createDatasets(all_prices)
print(X)
print(y)

# Split the training set in training and validation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

linreg = LinearRegression()
linreg.fit(X_train, y_train)
y_pred_lr = linreg.predict(X_test)
print(y_pred_lr)
print(f"Mean squared error of LinReg: {mean_squared_error(y_test, y_pred_lr)}")

# Neural network
clf_nn = Pipeline([
    ('scaler', StandardScaler()),
    ('neuralNet', MLPRegressor())
])

clf_nn.fit(X_train, y_train)
y_pred_nn = clf_nn.predict(X_test)
print(y_pred_nn)
print(f"Mean squared error of MLPRegressor: {mean_squared_error(y_test, y_pred_nn)}")

# Keras models
scaler = MinMaxScaler(feature_range=(0,1))
scaled_prices = scaler.fit_transform(all_prices)
X_scaled, y_scaled = createDatasets(scaled_prices)
X_train_scaled, X_test_scaled, y_train_scaled, y_test_scaled = train_test_split(X_scaled, y_scaled, test_size=0.25, random_state=42)

# Make 3D arrays
X_train_scaled = np.reshape(X_train_scaled, (X_train_scaled.shape[0], X_train_scaled.shape[1], 1))
X_test_scaled = np.reshape(X_test_scaled, (X_test_scaled.shape[0], X_test_scaled.shape[1], 1))

# Sequential model
model = Sequential()
model.add(LSTM(units=96, return_sequences=True, input_shape=(X_train_scaled.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=96,return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=96,return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=96))
model.add(Dropout(0.2))
model.add(Dense(units=1))

# Reshape before the LSTM layer
X_train_scaled = np.reshape(X_train_scaled, (X_train_scaled.shape[0], X_train_scaled.shape[1], 1))
X_test_scaled = np.reshape(X_test_scaled, (X_test_scaled.shape[0], X_test_scaled.shape[1], 1))

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(X_train_scaled, y_train_scaled, epochs=50, batch_size=32)
model.save('stock_prediction.h5')