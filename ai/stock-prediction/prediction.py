# Predict and reverse the transform using the same scaler
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
    return None
