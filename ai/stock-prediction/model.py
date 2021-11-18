import math
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense, Dropout

# It's a time series... Consider using Seglearn

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

# # Linear Regression
# linreg = LinearRegression()
# linreg.fit(X_train, y_train)
# y_pred_lr = linreg.predict(X_test)
# print(y_pred_lr)
# print(f"Mean squared error of LinReg: {mean_squared_error(y_test, y_pred_lr)}")

# # Neural network
# clf_nn = Pipeline([
#     ('scaler', StandardScaler()),
#     ('neuralNet', MLPRegressor())
# ])

# clf_nn.fit(X_train, y_train)
# y_pred_nn = clf_nn.predict(X_test)
# print(y_pred_nn)
# print(f"Mean squared error of MLPRegressor: {mean_squared_error(y_test, y_pred_nn)}")

# Keras models
scaler = MinMaxScaler(feature_range=(0,1))
scaled_prices = scaler.fit_transform(all_prices)
X_scaled, y_scaled = createDatasets(scaled_prices)
X_train_scaled, X_test_scaled, y_train_scaled, y_test_scaled = train_test_split(X_scaled, y_scaled, test_size=0.25, random_state=42)

# Make 3D arrays
X_train_scaled = np.reshape(X_train_scaled, (X_train_scaled.shape[0], X_train_scaled.shape[1], 1))
X_test_scaled = np.reshape(X_test_scaled, (X_test_scaled.shape[0], X_test_scaled.shape[1], 1))

# # Sequential model
# model = Sequential()
# model.add(LSTM(units=96, return_sequences=True, input_shape=(X_train_scaled.shape[1], 1)))
# model.add(Dropout(0.2))
# model.add(LSTM(units=96,return_sequences=True))
# model.add(Dropout(0.2))
# model.add(LSTM(units=96,return_sequences=True))
# model.add(Dropout(0.2))
# model.add(LSTM(units=96))
# model.add(Dropout(0.2))
# model.add(Dense(units=1))

# Reshape before the LSTM layer
X_train_scaled = np.reshape(X_train_scaled, (X_train_scaled.shape[0], X_train_scaled.shape[1], 1))
X_test_scaled = np.reshape(X_test_scaled, (X_test_scaled.shape[0], X_test_scaled.shape[1], 1))

# # Compile the model
# model.compile(loss='mean_squared_error', optimizer='adam')
# model.fit(X_train_scaled, y_train_scaled, epochs=50, batch_size=32)
# model.save('stock_prediction.h5')

# Predict and reverse the transform using the same scaler
model = load_model('ai/stock-prediction/stock_prediction.h5')
y_pred_LSTM = model.predict(X_test_scaled)
y_pred_LSTM = scaler.inverse_transform(y_pred_LSTM)
# y_test = scaler.inverse_transform(y_test_scaled.reshape(-1, 1))

# Print some results
print(y_pred_LSTM)
print(f"Mean squared error of LSTM: {mean_squared_error(y_test, y_pred_LSTM)}")

#TODO
#   - Try this script on old mac
#   - Write the function assuming the model is valid and submit on hackerrank

def printTransactions(m, k, d, name, owned, prices):
    # If the price will go down, you SELL
    # If the price will go up, you BUY
    # Biggest delta for both gets everything

    def predictTommorow(model, stock_prices):
        prediction = model.predict(stock_prices)
        return prediction
    
    nr_transactions = 0
    print_transactions = ""
    predictions = []

    for stock_prices in prices:
        delta = predictTommorow(model, stock_prices)
        predictions.append(delta)
    
    # What to sell?
    # The biggest loss will depend on the number of shares you own
    wallet_changes = []

    for n1, n2 in zip(predictions, owned):
        wallet_changes.append(n1 * n2)

    biggest_drop = min(wallet_changes)
    if biggest_drop < 0:
        nr_transactions += 1
        sell_index = wallet_changes.index(biggest_drop)
        sell_stock = name[sell_index]
        sell_quantity = owned[sell_index]
        owned[sell_index] = 0 # not needed probable since we don't have to output it
        sell_output = f"\n{sell_stock} SELL {sell_quantity}"
        print_transactions += sell_output

    # What to buy?
    biggest_rise = max(predictions)
    if biggest_rise > 0:
        nr_transactions += 1
        buy_index = predictions.index(biggest_rise)
        buy_stock = name[buy_index]
        buy_price = prices[buy_index][-1]
        buy_quantity = math.floor(m / buy_price)
        owned[buy_index] += buy_quantity # not necessary since we don't need to output it
        buy_output = f"\n{buy_stock} BUY {buy_quantity}"   
        print_transactions += buy_output 

    print(str(nr_transactions) + print_transactions)

    return None