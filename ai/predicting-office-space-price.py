# input() --> Consumes one line of the input in the terminal at the time. 
#             So the first input() = the first input line, use it again and input() will be the second, and so on.

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Set the intial data
features, rows = map(int, input().split())

# Set the training data
X_train = np.empty((rows, features))
y_train = []

for i in range(rows):
    row = list(map(float, input().split()))
    for j, data in enumerate(row):
        if j < features:    
            X_train[i,j] = data
        else:
            y_train.append(data)

# Set the test data
test_rows = int(input())
X_test = []

for i in range(test_rows):
    new_row = list(map(float, input().split()))
    X_test.append(new_row)

X_test = np.array(X_test)

# Fitting Polynomial Regression to the dataset
poly_reg = PolynomialFeatures(degree=3)
X_poly = poly_reg.fit_transform(X_train)
pol_reg = LinearRegression()
pol_reg.fit(X_poly, y_train)

# Predicting the outcome of the test set
y_test = pol_reg.predict(poly_reg.fit_transform(X_test))

for i, row in enumerate(y_test):
    print(round(row, 2))